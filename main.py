import sendgrid
import os
try:
        # Python 3
            import urllib.request as urllib
except ImportError:
        # Python 2
            import urllib2 as urllib

            sg = sendgrid.SendGridAPIClient(apikey="get_this_key_from_sendgrid")
            data = {
                      "personalizations": [
                              {
                                        "to": [
                                                    {
                                                                  "email": "srivastavadi12@xxxxx.com"
                                                                          }
                                                          ],
                                              "substitutions": {
                                                          "-name-": "Example User",
                                                                  "-city-": "Denver",
                                                                          "-first_name-": "Divyanshu",
                                                                                  "-match-": "Rahul",
                                                                                          "-surname-" : "srivastava"
                                                                                                },
                                                    "subject": "Testing is still going on my friend",

                                                        },
                                ],
                        "from": {
                                "email": "divyanshu@xxxxxx.com"
                                  },
                          "content": [
                                  {
                                            "type": "text/html",
                                                  "value": "I'm replacing the <strong>body tag</strong>"
                                                      }
                                    ],
                            "template_id": "a4c74d0a-b099-4711-ab81-39bc04315c53"
                            }
            try:
                    response = sg.client.mail.send.post(request_body=data)
            except urllib.HTTPError as e:
                    print (e.read())
                        exit()
                        print(response.status_code)
                        print(response.body)
                        print(response.headers)

