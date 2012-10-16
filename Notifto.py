import urllib, urllib2, json

class Notifo:
    """
    Class to send notification from Notifo.com
    """
    def __init__(self):
        self.apiusername = "cappie013"
        self.apikey = "x37f52133a817527676864a5c84db2d8df66d44dc"
        self.url = "https://api.notifo.com/v1/send_notification"   

    def sendNotification(self, to = None, msg = None, label = None, title = None, uri = None):
        """
        Send message to a user
        to      -> user
        msg     -> msg to send
        label   -> application description
        title   -> event's name
        uri     -> callback uri
        """
        data = {}
        if to is not None:
            data["to"] = to
        if msg is not None:
            data["msg"] = msg
        if label is not None:
            data["label"] = label
        if title is not None:
            data["title"] = title
        if uri is not None:
            data["uri"] = uri
        params = urllib.urlencode(data)   
        return self.sendRequest(params)

    def sendRequest(self, data):
        credentials = "%(user)s:%(key)s" % {"user": self.apiusername, "key": self.apikey}
        basic = "Basic %s" % credentials.encode("base64").strip()
        headers = {"Authorization": basic}

        request = urllib2.Request(self.url, data, headers)
        try:
            response = urllib2.urlopen(request)
        except IOError, e:
            return {"status" : "error",
                    "response_code" : e.code,
                    "response_message" : e.msg
                   }
        return json.loads(response.read())
            

values = {}
values["to"] = "cappie013"
values["label"] = "DownloadSubtitle"
values["title"] = "Error"
values["msg"] = "caca"
notifo = Notifo()
print notifo.sendNotification("cappie013", "toto")
