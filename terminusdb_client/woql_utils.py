import urllib.parse

# TODO: it's not constant anymore
# need to add addURLPrefix
STANDARD_URLS = {
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "tcs": "http://terminusdb.com/schema/tcs#",
    "xdd": "http://terminusdb.com/schema/xdd#",
    "v": "http://terminusdb.com/woql/variable/",
    "terminus": "http://terminusdb.com/schema/terminus#",
    "vio": "http://terminusdb.com/schema/vio#",
}


def encode_uri_component(value):
    return urllib.parse.urlencode(value, doseq=True)


def uri_encode_payload(payload):
    if isinstance(payload, str):
        return self.encodeURIComponent(payload)
    payload_arr = []
    if isinstance(payload, dict):
        for key, value in payload.items():
            """
                if dictionary inside dictionary
            """
            if isinstance(value, dict):
                # for keyElement,valueElement in value.items():
                payload_arr.append(self.encodeURIComponent(value))
            else:
                payload_arr.append(self.encodeURIComponent({key: value}))

    return "&".join(payload_arr)


def add_params_to_url(url, payload):
    if payload:
        params = self.URIEncodePayload(payload)
        if params:
            url = "{}?{}".format(url, params)
    return url


# below are utils for WOQLQuery


def add_namespaces_to_variable(var):
    if var[:2] != "v:":
        return "v:" + var
    return var


def add_namespaces_to_variables(variables):
    nvars = []
    for v_item in variables:
        nvars.append(self.addNamespacesToVariable(v_item))
    return nvars


def empty(obj):
    """ * is the object empty?
     * returns true if the json object is empty
     """
    if not obj:
        # Assume if it has a length property with a non-zero value
        # that that property is correct.
        return True
    if len(obj) > 0:
        return False
    if len(obj) == 0:
        return True
    # Otherwise, does it have any properties of its own?
    # if type(obj) == dict:
    #     for key in obj.keys():
    #         if hasattr(obj,key):
    #             return False
    return True


def shorten(url, prefixes=None):
    prefixes = prefixes if prefixes else STANDARD_URLS
    for pref, val in prefixes.items():
        short_url = url[: len(val)]
        if val == short_url:
            return f"{pref}:{short_url}"
    return url


def is_data_type(stype):
    sh = shorten(stype)
    if sh and (sh[:4] == "xsd:" or sh[:4] == "xdd:"):
        return True
    return False


def valid_url(string):
    if string and (string[:7] == "http://" or string[:8] == "https://"):
        return True
    return False


def url_fraqment(url):
    bite = url.split("#")
    if len(bits) <= 1:
        if not valid_url(url):
            bits = url.split(":")


def label_from_url(url):
    nurl = url_fraqment(url)
    nurl = nurl if nurl else url
    last_char = nurl.rfind("/")
    if last_char < len(nurl) - 1:
        nurl = nurl[last_char + 1 :]
    nurl = nurl.replace("_", " ")
    return nurl[0].upper() + nurl[1:]
