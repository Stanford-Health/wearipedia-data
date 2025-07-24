<div class="siteWrapper">

<div class="sidebar">

<div class="sidebarLogo text-center">

<img
src="https://static.ouraring.com/images/oura-developer-logo-black.svg"
width="70" height="160" />

</div>

- <a href="/oauth/applications" class="sidebarMenuLink">My
  Applications</a>
- <a href="/personal-access-tokens" class="sidebarMenuLink">Personal
  Access Tokens</a>
- <a href="/docs" class="sidebarMenuLink sidebarMenuActiveItem">API
  Documentation</a>

<div id="sidebar-popup">

- <a href="/" class="sidebarMenuLink">« Back to Oura</a>

</div>

</div>

<div class="helpContentArea">

<div class="container-fluid mainContent noNavBar">

# API Documentation

<div class="row row-eq-height row--bottomMargin">

<div class="col-xs-12 col-sm-3 col-md-3 col-lg-2">

<div class="blockContent blockContent--bottomMargin help-menu">

<div class="list-group help-list">

<a href="/docs/" class="list-group-item">Getting Started</a>
<a href="/v2/docs" class="list-group-item">V2 API</a>
<a href="/docs/authentication"
class="list-group-item active">Authentication</a>
<a href="/docs/error-handling" class="list-group-item">Error
Handling</a>

</div>

</div>

</div>

<div class="col-xs-12 col-sm-9 col-md-9 col-lg-10">

<div class="blockContent blockContent--bottomMargin">

# Authentication

<div class="content-segment">

The Oura Cloud API offers two methods for Authentication. Oura offers an
industry standard OAuth2 protocol as well as Personal Access Tokens.

- [OAuth2 Authentication](#oauth2)
  1.  [Authorization and Access Token URLs](#oauth2-urls)
  2.  [Scopes](#oauth2-scopes)
  3.  [The Server-Side Flow](#oauth2-the-server-side-flow)
      1.  [Direct Users To Log Into Oura and Authorize Your
          App](#oauth2-directing-users)
      2.  [Oura Redirects Back To Your
          Site](#oauth2-redirecting-to-your-site)
      3.  [Exchange Code For Access
          Token](#oauth2-exchange-code-for-access-token)
      4.  [Get New Access Token Using The Refresh
          Token](#oauth2-get-new-access-token-for-refresh-token)
  4.  [The Client-Side Only Flow](#oauth2-the-client-side-only-flow)
      1.  [Direct Users To Log Into Oura and Authorize Your
          App](#oauth2-client-only-direct-users-to-login)
      2.  [Oura Redirects Back To Your
          Site](#oauth2-client-only-redirecting-to-your-site)
  5.  [Using The Access Token](#oauth2-using-the-access-token)
  6.  [Further Reading](#oauth2-further-reading)
- [Personal Access Tokens](#personal-access-tokens)
  1.  [Create A Personal Access Token](#create-a-personal-access-token)
  2.  [Using A Personal Access Token](#using-a-personal-access-token)

------------------------------------------------------------------------

</div>

<div id="oauth2" class="content-segment">

<span id="oauth2"></span>

## OAuth2 Authentication

Oura offers an industry standard OAuth2 protocol. In most cases, you
should not implement the OAuth2 protocol yourself – instead, using a
ready-made OAuth2 [client
library](https://oauth.net/code/#client-libraries) for your programming
language or platform is recommended.

If you intend to only pull your own personal data, [Personal Access
Tokens](#personal-access-tokens) may fit your needs better.

<div id="oauth2-content" class="content-inset">

<div id="oauth2-urls" class="content-segment">

<span id="oauth2-urls"></span>

### Authorization and access token URLs

<div class="content-segment">

If you are using an existing OAuth2 library, you may need to configure
the following URLs.

- **Authorize:** `https://cloud.ouraring.com/oauth/authorize`
- **Access Token URL:** `https://api.ouraring.com/oauth/token`

</div>

------------------------------------------------------------------------

</div>

<div id="oauth2-scopes" class="content-segment">

<span id="oauth2-scopes"></span>

### Scopes

<div class="content-segment">

You can request access to 8 different scopes of user data:

- `email` Email address of the user
- `personal` Personal information (gender, age, height, weight)
- `daily` Daily summaries of sleep, activity and readiness
- `heartrate` Time series heart rate for Gen 3 users
- `workout` Summaries for auto-detected and user entered workouts
- `tag` User entered tags
- `session` Guided and unguided sessions in the Oura app
- `spo2`Daily SpO2 Average recorded during sleep

When an Oura user authorizes access to your application, she can enable
and disable scopes based on her preferences. Require only access to the
scopes that your application needs. For example, if your application
doesn't require the email address of the user, leave it out.

</div>

------------------------------------------------------------------------

</div>

<div id="oauth2-the-server-side-flow" class="content-segment">

<span id="oauth2-the-server-side-flow"></span>

<div class="content-segment">

### The Server-side Flow

</div>

<div id="oauth2-directing-users">

<span id="oauth2-directing-users"></span>

#### i. Direct Users To Log Into Oura and Authorize Your App

<div class="content-inset">

#### `GET /oauth/authorize`

| Parameter | Required? | Description |
|----|----|----|
| response_type | Required | Value must be `code` |
| client_id | Required | Your developer application's client ID. You can find the client ID on the application's page, which is listed under [My Applications](/oauth/applications). |
| redirect_uri | Optional | The URL in your app where users will be sent after authorization (see below). This value needs to be URL-encoded. The redirect URIs listed for your application act as a whitelist of allowed values, meaning this parameter must match one of the URIs exactly. If your application has been configured with exactly one redirect URI, this parameter can be left out and the configured redirect URI will be used. However, it is adivisable to always include the redirect URI parameter. |
| state | Optional | Arbitrary string that will be sent back to your service as a parameter in the redirect URL after a succesful or unsuccesful authorization. This is typically used to identify the user or session that the authorization will be tied to. It should also contain a random string to protect against cross-site request forgery attacks. |
| scope | Optional | Space-separated list of permissions (scopes) your application requests access to. See [Scopes](#scopes). If left blank, the application will request *all* available scopes. |

Example authorization request:

` https://cloud.ouraring.com/oauth/authorize?response_type=code&client_id=E55QJ2DGMZUXK6TN&redirect_uri=https%3A%2F%2Fexample.com%2Fcallback&scope=email+personal&state=3PgHyjNECEu5YgTQP33NC5tZJ0onm2 `

</div>

------------------------------------------------------------------------

</div>

<div id="oauth2-redirecting-to-your-site">

<span id="oauth2-redirecting-to-your-site"></span>

#### ii. Oura Redirects Back To Your Site

<div class="content-inset">

When the user grants access to your application, Oura will redirect them
to your redirect URL with a `code`, `scope` and optional `state` query
parameter. Note that the space-separated list of scopes may be different
than the scopes that were requested. The redirect call format is:

`GET redirect_uri?code=XXX&scope=SCOPES&state=YYY`

If the user authorizes the application, the example authorization
request above will result in the following redirect:

` https://example.com/callback?code=TRUQR7C6PRIYDRXMCQLAMW4V5LFFZVFO&scope=email%20personal&state=3PgHyjNECEu5YgTQP33NC5tZJ0onm2 `

(The code parameter will be different each time, of course.)

<div class="alert alert-danger">

#### **If The User Denies Access**

If the user denies the request for authorization, the redirect will be
to the same redirect URI, but with the parameter `error=access_denied`
instead of the `code` parameter. Any supplied state parameter will be
included as well. For example:
`https://example.com/callback?error=access_denied&state=3PgHyjNECEu5YgTQP33NC5tZJ0onm2`

</div>

</div>

------------------------------------------------------------------------

</div>

<div id="oauth2-exchange-code-for-access-token">

<span id="oauth2-exchange-code-for-access-token"></span>

#### iii. Exchange Code For Access Token

<div class="content-inset">

#### `POST /oauth/token`

| Parameter | Required? | Description |
|----|----|----|
| grant_type | Required | Value must be `authorization_code` |
| code | Required | The authorization code received in the previous step as the `code` parameter to the redirect URI. |
| redirect_uri | Optional | The exact same redirect URI that was included in the authorization request that provided the code. If no URI was given in the authorization request, then this parameter must also be left out of this request. |
| client_id | Required if not using Basic Authorization | Your developer application's client ID. You can find the client ID on the application's page, which is listed under [My Applications](/oauth/applications). |
| client_secret | Required if not using Basic Authorization | Your developer application's client secret. You can find the client secret on the application's page, which is listed under [My Applications](/oauth/applications). |

------------------------------------------------------------------------

Instead of providing client_id and client_secret as parameters, they can
be given using the HTTP Basic Authorization, with client_id as username
and client_secret as password.

The parameters must be passed in the request body, using the
"application/x-www-form-urlencoded" format and UTF-8 encoding.

The reply to the request, provided that it is valid, is a JSON object
with the following properties:

| Property | Description |
|----|----|
| token_type | `bearer` |
| access_token | An alphanumerical string. This is a new access token that can be used to access the user's data through the Oura API. |
| expires_in | Number of seconds that the access token is valid for. |
| refresh_token | An alphanumerical string. A refresh token that can be used to acquire a new access token (and refresh token) after this access token expires. The refresh token is single-use, meaning it is invalidated after being used. |

</div>

------------------------------------------------------------------------

</div>

<div id="oauth2-get-new-access-token-for-refresh-token">

<span id="oauth2-get-new-access-token-for-refresh-token"></span>

#### iv. Get New Access Token Using The Refresh Token

<div class="content-inset">

#### `POST /oauth/token`

| Parameter | Required? | Description |
|----|----|----|
| grant_type | Required | Value must be `refresh_token` |
| refresh_token | Required | The refresh_token received when exchanging a `code` or older `refresh_token` for an access token. |
| client_id | Required if not using Basic Authorization | Your developer application's client ID. You can find the client ID on the application's page, which is listed under [My Applications](/oauth/applications). |
| client_secret | Required if not using Basic Authorization | Your developer application's client secret. You can find the client secret on the application's page, which is listed under [My Applications](/oauth/applications). |

Instead of providing client_id and client_secret as parameters, they can
be given using the HTTP Basic Authorization, with client_id as username
and client_secret as password.

The parameters must be passed in the request body, using the
"application/x-www-form-urlencoded" format and UTF-8 encoding.

The reply to the request, provided that it is valid, is a JSON object
with the following properties:

| Property | Description |
|----|----|
| token_type | `bearer` |
| access_token | An alphanumerical string. This is a new access token that can be used to access the user's data through the Oura API. |
| expires_in | Number of seconds that the access token is valid for. |
| refresh_token | An alphanumerical string. A refresh token that can be used to acquire a new access token (and refresh token) after this access token expires. The refresh token is single-use, meaning it is invalidated after being used. |

</div>

------------------------------------------------------------------------

</div>

</div>

<div id="oauth2-the-client-side-only-flow" class="content-segment">

<span id="oauth2-the-client-side-only-flow"></span>

<div class="content-segment">

### The Client-Side Only Flow

Note that the client-side only flow does not support refresh tokens.
Once a token expires (currently set to 30 days), the user will need to
re-authenticate your app.

</div>

<div id="oauth2-client-only-direct-users-to-login">

<span id="oauth2-client-only-direct-users-to-login"></span>

#### i. Direct Users To Log Into Oura and Authorize Your App

<div class="content-inset">

#### `GET /oauth/authorize`

| Parameter | Required? | Description |
|----|----|----|
| response_type | Required | Value must be `token` |
| client_id | Required | Your developer application's client ID. You can find the client ID on the application's page, which is listed under [My Applications](/oauth/applications). |
| redirect_uri | Optional | The URL in your app where users will be sent after authorization (see below). This value needs to be URL-encoded. The redirect URIs listed for your application act as a whitelist of allowed values, meaning this parameter must match one of the URIs exactly. If your application has been configured with exactly one redirect URI, this parameter can be left out and the configured redirect URI will be used. However, it is adivisable to always include the redirect URI parameter. |
| state | Optional | Arbitrary string that will be sent back to your service as a parameter in the redirect URL after a succesful or unsuccesful authorization. This is typically used to identify the user or session that the authorization will be tied to. It should also contain a random string to protect against cross-site request forgery attacks. |
| scope | Optional | Space-separated list of permissions (scopes) your application requests access to. See [Scopes](#scopes). If left blank, the application will request *all* available scopes. |

Example authorization request:

` https://cloud.ouraring.com/oauth/authorize?response_type=token&client_id=E55QJ2DGMZUXK6TN&redirect_uri=https%3A%2F%2Fexample.com%2Fcallback&scope=email+personal&state=MZJMwJIqPLdQ3I69z5zIFNuD99YJcm `

</div>

------------------------------------------------------------------------

</div>

<div id="oauth2-client-only-redirecting-to-your-site">

<span id="oauth2-client-only-redirecting-to-your-site"></span>

#### ii. Oura redirects back to your site

<div class="content-inset">

When the user grants access to your application, Oura will redirect them
to your redirect URL. The following properties are included in the
fragment part of the redirect URL, encoded using the
"application/x-www-form-urlencoded" format:

| Property | Description |
|----|----|
| token_type | `bearer` |
| access_token | An alphanumerical string. This is a new access token that can be used to access the user's data through the Oura API. |
| expires_in | Number of seconds that the access token is valid for. |
| scope | Space-separated list of scopes that the access token is valid for. Note that this may be a subset of the requested scopes if the user chose not to give access to some of the requested scopes. |
| state | The state parameter, returned back as-is, if it was included in the authorization request. |

The example authorization request above will result in the following
redirect if the user authorizes the application:

` https://example.com/callback#token_type=bearer&access_token=PHCW3OVMXQZX5FJUR6ZK4FAA2MK2CWWA&expires_in=2592000&scope=email+personal&state=MZJMwJIqPLdQ3I69z5zIFNuD99YJcm `

(The access_token will be different each time, of course.)

<div class="alert alert-danger">

#### **If The User Denies Access**

If the user denies the request for authorization, the redirect will be
to the same redirect URI, but with the parameter `error=access_denied`
instead of the `access_token` parameter. Any supplied state parameter
will be included as well. For example:
`https://example.com/callback?error=access_denied&state=3PgHyjNECEu5YgTQP33NC5tZJ0onm2`

</div>

</div>

------------------------------------------------------------------------

</div>

</div>

<div id="oauth2-using-the-access-token">

<span id="oauth2-using-the-access-token"></span>

<div class="content-segment">

### Using The Access Token

Once your application has acquired an access token using either of the
authorization flows, the token can be used to access the Oura API by
including the access token in the Authorization header:

```
GET /v2/usercollection/sleep HTTP/1.1
Host: api.ouraring.com
Authorization: Bearer PHCW3OVMXQZX5FJUR6ZK4FAA2MK2CWWA
```

</div>

------------------------------------------------------------------------

</div>

<div id="oauth2-using-the-access-token">

<span id="oauth2-using-the-access-token"></span>

<div class="content-segment">

### Revoking The Access Token

When you need to revoke access for a specific token use the following
API call format:

**URL parameter:** Replace `client_id` and `access_token` with the
corresponding values the API call:  
`https://api.ouraring.com/oauth/revoke?access_token={access_token}`

</div>

------------------------------------------------------------------------

</div>

<div id="oauth2-further-reading">

<span id="oauth2-further-reading"></span>

<div class="content-segment">

### Further reading

For features of OAuth2 not described in this document, see the
documentation on [Oauth.net](https://oauth.net/2/) and [RFC
6749](https://tools.ietf.org/html/rfc6749).

</div>

------------------------------------------------------------------------

</div>

</div>

</div>

<div id="personal-access-tokens" class="content-segment">

<span id="personal-access-tokens"></span>

## Personal Access Tokens

Oura offers Personal Access Tokens for Authentication. Personal access
tokens (PATs) may be used for retrieving your own personal data from the
Oura Cloud API.

If you wish to build an integration allowing multiple Oura Users to
share their data, using [OAuth2](#oauth2) may fit your needs better.

<div class="content-inset">

<div id="create-a-personal-access-token" class="content-segment">

<span id="create-a-personal-access-token"></span>

<div class="content-segment">

</div>

</div>

<div id="create-a-personal-access-token" class="content-segment">

<span id="create-a-personal-access-token"></span>

<div class="content-segment">

### Create A Personal Access Token

1.  Navigate to the Personal Access Tokens page
    - [https://cloud.ouraring.com/personal-access-tokens](/personal-access-tokens)
2.  In the upper-right corner of the page click the "Create A New
    Personal Access Token" Button
3.  Enter a unique note for the new Personal Access Token you are about
    to generate
    - This note is just a reminder for yourself about what the token is
      being used for
4.  Click "Create Personal Access Token" to submit the form and create
    your new Personal Access Token
5.  You should now have a new access token listed on the Personal Access
    Tokens page

<div class="alert alert-danger">

Be sure to copy this new token as you will not be able to view the token
once navigating away. Use the convenient "Copy" button to copy the token
value into your clipboard.

</div>

------------------------------------------------------------------------

</div>

</div>

<div id="using-a-personal-access-token" class="content-segment">

<span id="using-a-personal-access-token"></span>

<div class="content-segment">

### Using A Personal Access Token

Once you have acquired a Personal Access Token, the token can be used to
access the Oura API by including the Personal Access Token in the
Authorization header:

```
GET /v2/usercollection/sleep HTTP/1.1
Host: api.ouraring.com
Authorization: Bearer PHCW3OVMXQZX5FJUR6ZK4FAA2MK2CWWA
```

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="copyrightFooter">

©2021 Ōura Health Oy. All Rights Reserved. ŌURA and OURA and Ō are
trademarks of Ōura Health Oy and may not be used without permission.

</div>

</div>

</div>
