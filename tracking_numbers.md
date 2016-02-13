#### How to get tracking numbers
Simply send a GET request to the tracking number endpoint: 
`http://hackers-api.goshippo.com/v1/tracking_numbers/`

We will return: 
* The URL to the next page
* Five tracking numbers, along with the carriers they are shipped with. 


#### Example Input
```shell
$ curl http://hackers-api.goshippo.com/v1/tracking_numbers/
```
#### Response:

```json
{
"count": 2000,
"next": "http://hackers-api.goshippo.com/v1/tracking_numbers/?page=2",
"previous": null,
"results": [
{
"carrier": "usps",
"tracking_number": "9400110898680015376677"
},
{
"carrier": "dhl_express",
"tracking_number": "JD014600002258214946"
},
{
"carrier": "usps",
"tracking_number": "9405510898680015455566"
},
{
"carrier": "usps",
"tracking_number": "9405510898680015455665"
},
{
"carrier": "dhl_express",
"tracking_number": "JD014600002398841684"
}
]
}
```
