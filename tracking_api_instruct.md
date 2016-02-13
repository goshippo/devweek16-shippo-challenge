#### How to use the Tracking API
Simply send a GET request to our Tracking Endpoint: 
`http://hackers-api.goshippo.com/v1/tracks/<CARRIER>/<TRACKING-NUMBER>/`

To see which carriers we support, sample responses, and how to setup webhooks, [head to our docs](http://r.goshippo.com/tracking-api-docs).


#### Example Input

```shell
$ curl http://hackers-api.goshippo.com/v1/tracks/usps/9400110898680009697924/
```
#### Response:

```json
{
"carrier": "usps",
"tracking_number": "9400110898680009697924",
"tracking_status": {
"object_created": "2015-11-16T16:57:16.058Z",
"object_updated": "2015-11-16T16:57:16.058Z",
"object_id": "a9a12961b47d4ca0a080c3d0d6bd9c6e",
"status": "DELIVERED",
"status_details": "Your shipment has been delivered at the destination mailbox.",
"status_date": "2015-10-15T12:12:00Z",
"location": {
"city": "Benton",
"state": "AR",
"zip": "72019",
"country": "US"
}
},
"tracking_history": [
{
"object_created": "2015-11-16T16:57:16.057Z",
"object_id": "857997b997684a11a5c5d9ee2979aa97",
"status": "UNKNOWN",
"status_details": "The shipping label has been created.",
"status_date": "2015-10-09T03:56:00Z",
"location": {
"city": "Hollywood",
"state": "FL",
"zip": "33020",
"country": "US"
}
},
{
"object_created": "2015-11-16T16:57:16.057Z",
"object_id": "39750b6980a14c498dd2e45f62a83021",
"status": "TRANSIT",
"status_details": "Your shipment has arrived at the USPS origin facility.",
"status_date": "2015-10-09T18:21:00Z",
"location": {
"city": "Opa Locka",
"state": "FL",
"zip": "33054",
"country": "US"
}
},
{
"object_created": "2015-11-16T16:57:16.058Z",
"object_id": "a563afb6d5f54f06b56c22f5a6ee5028",
"status": "DELIVERED",
"status_details": "Your shipment has been delivered at the destination mailbox.",
"status_date": "2015-10-15T12:12:00Z",
"location": {
"city": "Benton",
"state": "AR",
"zip": "72019",
"country": "US"
}
}
]
}
```
