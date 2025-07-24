<div class="nav_wrap">

<div id="resizer">

</div>

</div>

<div id="main" tabindex="-1">

<div id="content">

# Module: Toybox.Authentication

## Overview

<div class="docstring">

<div class="discussion">

The Authentication Module provides tools for authentication.

With the Authentication module, Connect IQ apps will be able to make
OAuth requests redirected through Connect IQ mobile app.

</div>

</div>

<div class="tags">

Since:

<div class="since">

API Level 3.3.0

</div>

</div>

## Classes Under Namespace

**Classes:**
<span class="type">[Message](../Toybox/Authentication/Message.html)</span>,
<span class="type">[OAuthMessage](../Toybox/Authentication/OAuthMessage.html)</span>

## Constant Summary

### OAuthResultType

<div class="tags">

Since:

<div class="since">

API Level 3.3.0

</div>

</div>

Name

</div>

</div>

Value

Since

Description

See Also

OAUTH_RESULT_TYPE_URL

0

API Level 3.3.0

How the OAuth token will be returned in the final step.

### OAuthSigningMethod

<div class="tags">

Since:

<div class="since">

API Level 3.3.0

</div>

</div>

Name

Value

Since

Description

See Also

OAUTH_SIGNING_METHOD_HMAC_SHA1

0

API Level 3.3.0

How the OAuth request will be signed

## Instance Method Summary <span class="small"><a href="#" class="summary_toggle">collapse</a></span>

- <span class="summary_signature summary_signature_link">
  [**makeOAuthRequest**](#makeOAuthRequest-instance_function "makeOAuthRequest (Instance Function)")(requestUrl
  as
  <span class="type">[Lang.String](../Toybox/Lang/String.html)</span>,
  requestParams as
  <span class="type">[Lang.Dictionary](../Toybox/Lang/Dictionary.html)</span>\<<span class="type">[Lang.String](../Toybox/Lang/String.html)</span>,
  <span class="type">[Lang.String](../Toybox/Lang/String.html)</span>\>,
  resultUrl as
  <span class="type">[Lang.String](../Toybox/Lang/String.html)</span>,
  resultType as
  <span class="type">[Authentication.OAuthResultType](../Toybox/Authentication.html#OAuthResultType-module)</span>,
  resultKeys as
  <span class="type">[Lang.Dictionary](../Toybox/Lang/Dictionary.html)</span>\<<span class="type">[Lang.String](../Toybox/Lang/String.html)</span>,
  <span class="type">[Lang.String](../Toybox/Lang/String.html)</span>\>)
  as **Void** </span> <span class="summary_desc"> </span>
  <div class="inline">

  Request an OAuth sign-in through Garmin Connect IQ Mobile App A
  notification will trigger on the phone, that when clicked, provides a
  web view that shows `requestUrl`.

  </div>
- <span class="summary_signature summary_signature_link">
  [**registerForOAuthMessages**](#registerForOAuthMessages-instance_function "registerForOAuthMessages (Instance Function)")(method
  as
  <span class="type">[Lang.Method](../Toybox/Lang/Method.html)</span>(message
  as
  <span class="type">[Authentication.OAuthMessage](../Toybox/Authentication/OAuthMessage.html)</span>)
  as **Void**) as **Void** </span> <span class="summary_desc"> </span>
  <div class="inline">

  Register a callback for receiving OAuth messages.

  </div>

<div id="instance_method_details" class="method_details_list">

## Instance Method Details

<div class="method_details details">

### **makeOAuthRequest(requestUrl as <span class="type">[Lang.String](../Toybox/Lang/String.html)</span>, requestParams as <span class="type">[Lang.Dictionary](../Toybox/Lang/Dictionary.html)</span>\<<span class="type">[Lang.String](../Toybox/Lang/String.html)</span>, <span class="type">[Lang.String](../Toybox/Lang/String.html)</span>\>, resultUrl as <span class="type">[Lang.String](../Toybox/Lang/String.html)</span>, resultType as <span class="type">[Authentication.OAuthResultType](../Toybox/Authentication.html#OAuthResultType-module)</span>, resultKeys as <span class="type">[Lang.Dictionary](../Toybox/Lang/Dictionary.html)</span>\<<span class="type">[Lang.String](../Toybox/Lang/String.html)</span>, <span class="type">[Lang.String](../Toybox/Lang/String.html)</span>\>)** <span class="type"> as **Void**</span>

<div class="docstring">

<div class="discussion">

Request an OAuth sign-in through Garmin Connect IQ Mobile App

A notification will trigger on the phone, that when clicked, provides a
web view that shows `requestUrl`. If the user grants permission to the
app, then the callback registered by
[registerForOAuthMessages()](../Toybox/Authentication.html#registerForOAuthMessages-instance_function)
will be called with an
[OAuthMessage](../Toybox/Authentication/OAuthMessage.html) from the
OAuth response.

</div>

</div>

<div class="tags">

Parameters:

- <span class="name">requestUrl</span> —
  <span class="type">(<span class="type">[Lang.String](../Toybox/Lang/String.html)</span>)</span>
  —
  <div class="inline">

  The URL to load in the web view to begin authentication

  </div>
- <span class="name">requestParams</span> —
  <span class="type">(<span class="type">[Lang.Dictionary](../Toybox/Lang/Dictionary.html)</span>)</span>
  —
  <div class="inline">

  Non-URL encoded parameters for the `requestUrl`

  </div>
- <span class="name">resultUrl</span> —
  <span class="type">(<span class="type">[Lang.String](../Toybox/Lang/String.html)</span>)</span>
  —
  <div class="inline">

  The URL of the final page of authentication that contains the
  `resultKeys`

  </div>
- <span class="name">resultType</span> —
  <span class="type">(<span class="type">[Authentication.OAuthResultType](../Toybox/Authentication.html#OAuthResultType-module)</span>)</span>
  —
  <div class="inline">

  An OAUTH_RESULT_TYPE\_\* value that specifies the format of the result

  </div>
- <span class="name">resultKeys</span> —
  <span class="type">(<span class="type">[Lang.Dictionary](../Toybox/Lang/Dictionary.html)</span>)</span>
  —
  <div class="inline">

  The desired OAuth response values passed to the callback method. The
  keys map to the actual OAuth response keys, and the values map to the
  keys of the [OAuthMessage](../Toybox/Authentication/OAuthMessage.html)
  data.

  </div>

<div class="examples">

Example:

``` example
using Toybox.Authentication;
using Toybox.System;

const CLIENT_ID = "myClientID";
const OAUTH_CODE = "myOAuthCode";
const OAUTH_ERROR = "myOAuthError";

// register a callback to capture results from OAuth requests
Authentication.registerForOAuthMessages(method(:onOAuthMessage));

// wrap the OAuth request in a function
function getOAuthToken() {
   status = "Look at OAuth screen\n";
   Ui.requestUpdate();

   // set the makeOAuthRequest parameters
   var params = {
       "redirect_uri" => "connectiq://oauth",
       "response_type" => "code",
       "client_id" => $.CLIENT_ID
   };

   // makeOAuthRequest triggers login prompt on mobile device.
   // "responseCode" and "responseError" are the parameters passed
   // to the resultUrl. Check the oauth provider's documentation
   // to determine the correct strings to use.
   Auth.makeOAuthRequest(
       "https://requesturl.com",
       params,
       "http://resulturl.com",
       Auth.OAUTH_RESULT_TYPE_URL,
       {"responseCode" => $.OAUTH_CODE, "responseError" => $.OAUTH_ERROR}
   );
}

// implement the OAuth callback method
function onOAuthMessage(message) {
    if (message.data != null) {
        var code = message.data[$.OAUTH_CODE];
        var error = message.data[$.OAUTH_ERROR];
    } else {
        // return an error
    }
}
// the OAuth service can now be used with a makeWebRequest() call
```

</div>

Since:

<div class="since">

API Level 3.3.0

</div>

</div>

</div>

<div class="method_details details">

### **registerForOAuthMessages(method as <span class="type">[Lang.Method](../Toybox/Lang/Method.html)</span>(message as <span class="type">[Authentication.OAuthMessage](../Toybox/Authentication/OAuthMessage.html)</span>) as **Void**)** <span class="type"> as **Void**</span>

<div class="docstring">

<div class="discussion">

Register a callback for receiving OAuth messages.

The callback will be called once for each received OAuth message. If
there are messages waiting for the app when this function is called, the
callback will immediately be called once for each waiting message.

</div>

</div>

<div class="tags">

Parameters:

- <span class="name">method</span> —
  <span class="type">(<span class="type">[Lang.Method](../Toybox/Lang/Method.html)</span>)</span>
  —
  <div class="inline">

  A reference to a callback, which must receive a `data` argument of the
  type [OAuthMessage](../Toybox/Authentication/OAuthMessage.html).

  </div>

<div class="examples">

Example:

``` example
using Toybox.Authentication;

function onOAuthMessage(message) {
    if (message.data != null) {
        var code = message.data[OAUTH_CODE];
        var error = message.data[OAUTH_ERROR];
    } else {
        // return an error
    }
}
Authentication.registerForOAuthMessages(method(:onOAuthMessage));
```

</div>

Since:

<div class="since">

API Level 3.3.0

</div>

</div>

</div>

</div>

------------------------------------------------------------------------

Generated Jul 17, 2025, 3:57:17 PM
