#### How to setup webhooks

**Adding webhooks**

1. Create a free Shippo account at [goshippo.com](https://goshippo.com/)
2. Head to [the API section](https://goshippo.com/user/apikeys/), and add your webhook URL.

**Activating webhooks**

To activate webhook updates for a shipment, send a POST request to the same Tracking endpoint: `http://hackers-api.goshippo.com/v1/tracks/<CARRIER>/<TRACKING-NUMBER>/`

You should expect the same json response as the GET request.

*Webhook updates are free for applications created at the hackathon.*

**Expected webhook behaviour**

Shippo expects your webhook to return a response with a 2XX HTTP status code, indicating that the webhook has been received successfully. 

If we don’t receive a successful response, we will re-try our POST request up to 5 times, with a 10 second delay between each - for a total of 6 messages within 1 minute.

If at the end of our 5th try, we still do not receive a successful response, we will disable your webhook. To re-enable your webhook, go back into your Shippo dashboard and add it again. 

