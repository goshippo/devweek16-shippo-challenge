#### How to get tracking numbers
Simply send a GET request to the tracking number endpoint: 
`http://hackers-api.goshippo.com/v1/tracking_numbers/`

We will return: 
* The URL to the next page
* Four tracking numbers, along with the carriers they are shipped with. 


#### Example Input
```shell
$ curl http://hackers-api.goshippo.com/v1/tracking_numbers/
```
#### Response:

```json
{
    "count": ​4279,
    "next": "http://hackers-api.goshippo.com/v1/tracking_numbers",
    "previous": null,
    "results": 
    [
      {
          "carrier": "canada_post",
          "tracking_number": "0003000074518873637194103296551"
      },
      {
          "carrier": "usps",
          "tracking_number": "0004000074518873637194103296551"
      },
      {
          "carrier": "usps",
          "tracking_number": "0004012345612345678912345"
      },
    ]
}
```
