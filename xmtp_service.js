const express = require('express');
const { Client } = require("@xmtp/xmtp-js");
const { Wallet } = require("ethers");

const app = express();
app.use(express.json());

const RECIPIENT_ADDRESS = '0x12DCfE5FF6b13974fE6822A331488d4c32b6C625';

async function sendProductPing(productName, price, amazonUrl, walmartUrl) {
  console.log('Received data:', { productName, price, amazonUrl, walmartUrl });

  const randomWallet = Wallet.createRandom();
  console.log('Sender address (random):', randomWallet.address);

  const xmtp = await Client.create(randomWallet, { env: "production" });

  const canMessage = await xmtp.canMessage(RECIPIENT_ADDRESS);
  if (!canMessage) {
    console.log("Cannot message this address. They may not have XMTP enabled.");
    return;
  }

  const conversation = await xmtp.conversations.newConversation(RECIPIENT_ADDRESS);
  const pingMessage = `Hi! Thanks for alerting product: "${productName}". Will ping you when price drops from ${price}`;
  await conversation.send(pingMessage);
  console.log("Ping message sent from", randomWallet.address, "to", RECIPIENT_ADDRESS);
  console.log("Message content:", pingMessage);

  // Send Walmart link after 10 seconds
  setTimeout(async () => {
    const walmartMessage = `We found a better price on Walmart! Here's the link: ${walmartUrl}`;
    await conversation.send(walmartMessage);
    console.log("Walmart message sent:", walmartMessage);
  }, 10000);
}

app.post('/send-ping', async (req, res) => {
  console.log('Received POST request to /send-ping');
  console.log('Request body:', req.body);

  const { productName, price, amazonUrl, walmartUrl } = req.body;
  try {
    await sendProductPing(productName, price, amazonUrl, walmartUrl);
    console.log('Ping sent successfully');
    res.status(200).send('Ping sent successfully');
  } catch (error) {
    console.error('Error sending ping:', error);
    res.status(500).send('Error sending ping');
  }
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`XMTP service running on port ${PORT}`);
});