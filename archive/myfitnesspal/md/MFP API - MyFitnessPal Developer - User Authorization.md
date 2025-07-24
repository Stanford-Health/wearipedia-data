<div class="site-header">

<a href="/" class="site-logo"></a>

# <img src="/assets/images/mfp-wordmark.svg" class="site-logo-img"
alt="MyFitnessPal" />

<div class="site-nav-button">

<span class="site-nav-button-text">Menu</span>
<img src="/assets/images/menu.svg" class="site-nav-button-icon"
width="20" height="20" />

</div>

- [DOCS](/docs)
- [Blog](/blog)

</div>

<div class="section container two-cols">

<div class="sidebar col-1">

<div class="sidenav">

### Architecture

[About this API](/docs/about) [Domains](/docs/domains)
[Versioning](/docs/versioning) [Example URLs](/docs/example-urls)

### General

[Identifiers](/docs/identifiers) [Supported Data
Formats](/docs/supported-data-formats) [Data Types](/docs/data-types)

##### Requests

[Access Token and Related Information](/docs/access-tokens)
[Localization](/docs/localization) [GET Request Query
Parameter](/docs/get-request-query-param) [Collection
Requests](/docs/collection-requests)

##### Responses

[Content Type](/docs/content-type) [Response
Codes](/docs/response-codes) [Response Body](/docs/response-body) [Error
Responses](/docs/error-responses) [Standard
Responses](/docs/standard-responses)

### Authentication and Authorization

[Partner Authentication](/docs/partner-authentication) [User
Authorization](/docs/user-authentication)

##### Authorization Code Grant (GET /oauth2/auth)

[Request query parameters](/docs/request-query-parameters) [Example 1:
Requesting the diary scope](/docs/auth-example-1) [Example 2: Requesting
all available scopes](/docs/auth-example-2)
[Response](/docs/auth-response) [Authorization
Errors](/docs/auth-errors)

##### Access Token Request (POST /oauth2/token)

[Request body form parameters](/docs/request-body-form-parameters)
[Response](/docs/post-response) [Access Token
Errors](/docs/access-token-errors)

##### Refreshing Access Tokens (POST /oauth2/token)

[Request body form
parameters](/docs/refresh-request-body-form-parameters)
[Response](/docs/refresh-post-response) [Refresh Token
Errors](/docs/refresh-token-errors) [Making
Requests](/docs/making-requests)

##### Revoking Tokens (POST /oauth2/revoke)

[Request body form
parameters](/docs/revoke-request-body-form-parameters)
[Response](/docs/revoke-response)

### Users

##### Resources GET /users/:userId

[Example Response with no fields
parameter](/docs/example-response-no-fields-parameter) [Example Response
with fields elements](/docs/example-response-with-fields-parameter)

##### Resources PATCH /users/:userId

[Request Example](/docs/patch-request-example)

### Measurements

##### Resources

[GET /measurements/](/docs/measurements-get) [POST
/measurements/](/docs/measurements-post)

### Diary

##### Resources

[GET /diary/](/docs/diary-get) [POST /diary/](/docs/diary-post) [PATCH
/diary/](/docs/diary-patch) [DELETE /diary/](/docs/diary-delete)

### Exercises

##### Resources

[GET /exercises/](/docs/exercises-diary-get)

### Subscriptions

##### Management

[POST /subscription/](/docs/subscription-post) [GET
/subscription/](/docs/subscription-get) [DELETE
/subscription/](/docs/subscription-delete)

##### Notifications

[Example Request Body](/docs/subscription-request-body) [Best Design
Practices](/docs/subscription-design)

### Appendix

##### Data Structures

[User](/docs/appendix-data-structures-user) [Measured
Value](/docs/appendix-data-structures-measured-value) [User
Profile](/docs/appendix-data-structures-user-profile)
[Account](/docs/appendix-data-structures-account) [Privacy
Preferences](/docs/appendix-data-structures-privacy-preferences) [Goal
Preferences](/docs/appendix-data-structures-goal-preferences) [Location
Preferences](/docs/appendix-data-structures-location-preferences) [Diary
Preferences](/docs/appendix-data-structures-diary-preferences)
[Nutritional
Contents](/docs/appendix-data-structures-nutritional-contents)
[Exercise](/docs/appendix-data-structures-exercise)
[Measurement](/docs/appendix-data-structures-measurement)
[Diary](/docs/appendix-data-structures-diary)
[Subscription](/docs/appendix-data-structures-subscription)

##### Error Codes

[Error Codes](/docs/appendix-error-codes)

##### Migrating from MyFitnessPal API v1 to v2

[v1 action:
log_cardio_exercise](/docs/appendix-migrate-log_cardio_exercise) [v1
action:
remove_cardio_exercise](/docs/appendix-migrate-remove_cardio_exercise)
[v1 action: log_weight](/docs/appendix-migrate-log_weight) [v1 action:
log_expended_energy](/docs/appendix-migrate-log_expended_energy) [v1
action: get_food_summary](/docs/appendix-migrate-get_food_summary) [v1
action:
get_cardio_exercises](/docs/appendix-migrate-get_cardio_exercises) [v1
action: get_weight](/docs/appendix-migrate-get_weight) [v1 action:
fetch_user_info](/docs/appendix-migrate-fetch_user_info) [v1 action:
subscribe_to_user_updates](/docs/appendix-migrate-subscribe_to_user_updates)
[v1 action:
unsubscribe_from_user_updates](/docs/appendix-migrate-unsubscribe_from_user_updates)

##### Tracking all­day steps activity

[Tracking all-day steps activity](/docs/appendix-tracking-all-day-steps)
[Recommended approach for tracking
steps](/docs/appendix-tracking-recommended-approach) [Determining daily
totals](/docs/appendix-tracking-determining-daily-totals) [Calorie
Adjustments](/docs/appendix-tracking-calorie-adjustments)

##### MyFitnessPal exercises and their identifiers

[MyFitnessPal exercises and their
identifiers](/docs/appendix-mfp-exercises-identifiers)

##### Full request and response examples

[POST and GET request and
response](/docs/appendix-full-request-examples)

</div>

</div>

<div class="main col-2 documentation">

# User Authorization

MyFitnessPal API user authorization is based on the OAuth 2.0 protocol.
(See: <http://oauth.net/2/>​) In order to use the API to interact with a
user’s MyFitnessPal account, these steps must be followed:

1.  Obtain permission from the user to link their account to your
    application. To do this, create a link on your website to the
    Authorization Code Grant URL hosted by MyFitnessPal. When the user
    follows this link, they will be presented with the option to grant
    access to your application. (If they do not already have a session
    in MyFitnessPal, they will first be presented with a login form.)

2.  If the user grants access to your application, the MyFitnessPal
    servers will redirect the user back to your site. Along with this
    redirect you will be passed an ​authorization code which represents
    the link between your application and the user.

3.  Immediately exchange the authorization code for an access token and
    a refresh token from MyFitnessPal. As part of this request, you will
    pass along your ​client id​ and ​client secret​, which serve to
    authenticate your application to the MyFitnessPal API. MyFitnessPal
    will provide you with the c​lient id​ and ​client secret​ when you set
    up your API account.

4.  The provided access token represents a fully authenticated token
    that must be used to make API requests on behalf of the linked user
    account. Every API request must contain a valid access token. The
    access token will expire after a certain period. A client app may
    request a new access token at any time using the refresh token. The
    refresh token remains valid until revoked by either your application
    or the user.

5.  Once a user has authorized your app to make requests to the
    MyFitnessPal API on their behalf, you may use the API methods
    documented below, including the access token with each request.

Each step in this process is described in more detail in the following
sections.

</div>

</div>

<div class="site-footer-logo">

<img src="/assets/images/mfp-wordmark.svg" class="site-footer-logo-img"
alt="MyFitnessPal" />

</div>

[Terms](https://www.myfitnesspal.com/terms-of-service)
[Privacy](https://www.myfitnesspal.com/privacy-policy) [Support](/faq/)
[Status](https://status.myfitnesspal.com/)
[Licensing](mailto:partners@myfitnesspal.com)
