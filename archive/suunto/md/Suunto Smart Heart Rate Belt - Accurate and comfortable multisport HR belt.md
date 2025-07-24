<div class="iframe">

</div>

<div style="background-color: #ffced4; padding: 2em; text-align: center; font-size: 18px;">

For full functionality, please enable Javascript.

</div>

<div style="position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0, 0, 0, 0); border: 0;">

Suunto is committed to achieving Level AA conformance for this website
in conformance with the Web Content Accessibility Guidelines (WCAG) 2.0
and achieving compliance with other accessibility standards. Please
contact Customer Service at USA +1 855 258 0900 (toll free), if you have
any issues accessing information on this website.

</div>

<div id="app" v-cloak="">

<div class="notification-container">

</div>

<div class="header u-width-100" role="banner"
:class="['', { 'mobile' : !$mq.laptop }]">

<div class="notification-bar" v-if="$mq.laptop &amp;&amp; !false">

<div class="notification-bar__wrapper f-center">

</div>

</div>

<div class="container-fluid wrapper" v-show="$mq.laptop">

<div class="navigation__logo-container">

</div>

<div class="u-flex u-flex-1 u-flex-valign-baseline">

- <div v-if="!loginScope.isLoading">

  <div v-if="loginScope.isVipLoginVisible"
  @click.prevent.stop="slotScope.toggleSubMenu('Profile')">

  </div>

  <div v-else="">

  </div>

  </div>

  <div class="u-flex m-md" v-if="!loginScope.isVipLoginVisible">

  <a href="#login-modal"
  class="header__signin u-flex u-flex-valign-center u-flex-center"
  data-header-mobile-signin=""
  data-@click.prevent.stop="loginScope.openLoginModal()"><span
  class="f-13 f-black f-uppercase f-bold">Sign in</span></a>

  </div>

</div>

</div>

<div class="navigation-mobile__wrapper u-flex">

<div class="navigation-mobile__header u-flex u-flex-valign-center"
:class="{ 'is-active': slotScope.isMenuOrSearchOpen }">

<div class="hamburger-box">

<div class="hamburger-inner">

</div>

</div>

<div class="u-flex u-width-100 u-flex-center">

</div>

</div>

<div class="sidebar-panel" v-if="slotScope.isOpenSearch">

<div class="navigation-mobile__menu"
:class="{ 'is-open': slotScope.isOpenSearch }">

Search

</div>

</div>

<div class="sidebar-panel" v-if="slotScope.isOpenProfile">

<div class="navigation-mobile__menu"
:class="{ 'is-open': slotScope.isOpenProfile }">

<div class="u-flex u-flex-dir-column"
v-if="!loginScope.isVipLoginVisible">

<div class="m-md">

<a href="#login-modal"
class="header__signin u-flex u-flex-valign-center u-flex-center"
data-header-mobile-signin=""
data-@click.prevent.stop="loginScope.openLoginModal(slotScope.toggleProfile)"><span
class="f-13 f-black f-uppercase f-bold">Sign in</span></a>

</div>

</div>

</div>

</div>

<div class="sidebar-panel" v-if="slotScope.isOpen">

<div class="navigation-mobile__menu">

</div>

</div>

</div>

</div>

<div class="product-page" product-page-loader=""
style="background-color: #ffffff">

<div class="product-page__breadcrumb container-fluid wrapper">

<div class="row">

<div class="col-xs-12 breadcrumb breadcrumb--top"
style="background-color: #ffffff">

- [Home](/)
- [Heart Rate Belts](/Product-search/heart-rate-belts/)
- <a href="/Products/Heart-Rate-Belts/suunto-smart-heart-rate-belt/"
  id="js-product-page-link" data-product-page-link="">Suunto Smart Heart
  Rate Belt</a>

</div>

</div>

</div>

<div class="product-page__info-blocks container-fluid wrapper">

<div class="row">

<div class="u-relative col-xs-12 col-md-8 col-lg-8 xs-pt-0 xs-pr-0 xs-pl-0 xs-pb-24 md-p-24 lg-pt-64 lg-pb-64 lg-pl-64 lg-pr-0"
epi-block-id="413688">

</div>

<div class="product-info__content" product-info="">

<div class="product-info__loader u-height-100 u-width-100 u-absolute f-center"
v-show="slotScope.loading">

</div>

<div class="product-info__product">

# {{ slotScope.selectedHrOptionData.PageName }}

# {{ slotScope.selectedHrOptionData.ProductLineName }}

</div>

<div class="product-info__product-description md-f-20 xs-f-18 xs-pt-8 md-pt-8 xs-pb-16 md-pb-16"
product-description=""
v-html="slotScope.selectedHrOptionData.Description">

</div>

<div class="product-info__content-area xs-p-16 xs-mb-16">

<div v-if="slotScope.productSizes">

<div class="product-variants list list--unstyled u-flex u-flex-dir-column">

<div class="product-sizes__group">

<div class="product-sizes__group-title">

<div class="xs-f-20">

Size

</div>

<div class="xs-f-16">

Watch diameter

</div>

</div>

<div class="product-sizes__wrapper u-flex">

<span v-for="(item, index) in slotScope.productSizes" :href="item.Url"
:class="['product-sizes u-flex u-flex-dir-column u-flex-wrap btn--secondary', {'selected':(slotScope.isSelectedSize(item.Url)) }]"></span>

<div class="relative u-flex u-flex-valign-center">

<span class="suunto-icon suunto-icon-check-large xs-f-30 f-near-black f-bold"
v-if="slotScope.isSelectedSize(item.Url)"></span>

<div class="u-flex-1">

<div class="product-sizes__title xs-f-12">

{{item.Name}}

</div>

<div class="product-sizes__subtitle xs-f-20">

{{item.Width}} mm

</div>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="product-info__variants" v-if="slotScope.hasVariantsData">

<div class="row">

<div class="col-xs-12 col-sm-12 col-md-12">

<div class="product-variants list list--unstyled u-flex u-flex-dir-column">

<div class="product-variants__group"
v-for="(group, index) in slotScope.groupedAllVariantsList">

<div class="product-variants__group-title"
v-if="group.name &amp;&amp; group.name.length &gt; 0">

<div class="xs-f-20">

{{group.name}}

</div>

<div class="xs-f-16">

</div>

</div>

<div class="u-flex u-flex-wrap product-variants__group-color">

<div v-for="(variant, index) in group.products" :key="variant.Ssid">

<div class="product-variants__variant u-flex u-flex-wrap"
v-if="!variant.ColorCode">

</div>

<div v-else="">

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="product-variants list list--unstyled u-flex u-flex-dir-column">

<div class="product-variant-info__group">

## {{ slotScope.selectedHrOptionData.ProductVariantName }}

<span class="product-variant-info__ssid u-inline-block f-16">{{
slotScope.selectedHrOptionData.Ssid }}</span>

</div>

<div class="product-variant-info__materials-description f-near-black u-inline-block f-16"
v-if="slotScope.selectedProductData.MaterialsDescriptionText"
v-html="slotScope.selectedProductData.MaterialsDescriptionText">

</div>

</div>

<div class="product-info__price-availability row u-flex-1">

<div class="col-xs-12">

<div class="u-flex u-flex-valign-center"
v-if="slotScope.pricesLoading || slotScope.loading">

<span class="dots-loader f-gray">Loading price and stock
information</span>

</div>

</div>

<div class="product-info__price-information col-xs-12">

<div class="u-flex product-info__price-container u-flex-dir-column">

<div class="product-info__detail-item"
v-if="slotScope.isGlobal &amp;&amp; !slotScope.selectedHrOptionData.HideBuyNowButtonOnGlobalSite">

Buy now

</div>

<div class="product-info__price-wrapper">

<div class="product-info__price-availability-wrapper product-info__detail-item u-flex u-flex-dir-column u-flex-h-center">

<div v-if="!slotScope.pricesLoading &amp;&amp; !slotScope.loading">

<div class="u-flex u-flex-dir-column"
v-if="slotScope.hasPrice || (slotScope.priceAvailable &amp;&amp; slotScope.selectedHrOptionData.IsPromoPrice)">

<div class="u-flex u-flex-valign-center">

<span id="price" v-if="slotScope.hasPrice"
:class="['xs-f-30 f-extra-bold', { 'f-monza': slotScope.selectedHrOptionData.IsPromoPrice }]">
{{ slotScope.selectedHrOptionData.Price }} </span> <span class="xs-pl-8"
v-if="slotScope.selectedHrOptionData.IsOmnibus">
<span class="xs-f-18">{{slotScope.selectedHrOptionData.OmnibusPriceTooltipText}}</span>
<span class="xs-f-30"> {{slotScope.selectedHrOptionData.OmnibusPrice}}
</span> </span>

</div>

<div class="product-info__price-discount"
v-if="slotScope.priceAvailable &amp;&amp; slotScope.selectedHrOptionData.IsPromoPrice">

<span class="f-bold f-line-through xs-f-16">{{
slotScope.selectedHrOptionData.OriginalPrice }}</span> / 
<span class="f-near-black xs-f-16"
v-text="slotScope.selectedHrOptionData.SavingsInfo"></span>

</div>

</div>

</div>

</div>

<div v-if="slotScope.statusAvailable &amp;&amp; !slotScope.loading &amp;&amp; !slotScope.pricesLoading">

<span :class="[
                                        { 'f-sushi' : slotScope.isInStock || slotScope.preOrderOnly || slotScope.notInStockButCustomizable },
                                        { 'f-monza' : !slotScope.isInStock &amp;&amp; !slotScope.preOrderOnly &amp;&amp; !slotScope.notInStockButCustomizable },
                                        'product-info__stock'
                                    ]"
:data-stockinfo="slotScope.selectedHrOptionData.Ssid"> {{
slotScope.selectedHrOptionData.StockInfo }} </span>

</div>

</div>

<div class="product-info__detail-item"
v-if="slotScope.selectedHrOptionData.ProductDisclaimerContent">

<div class="xs-f-16"
v-if="slotScope.selectedHrOptionData.ProductDisclaimerContent"
v-html="slotScope.selectedHrOptionData.ProductDisclaimerContent">

</div>

</div>

<div class="product-info__detail-item"
v-if="!slotScope.loading &amp;&amp; slotScope.selectedHrOptionData.ShippingEstimation &amp;&amp; slotScope.selectedHrOptionData.ShippingEstimation.length &gt; 0">

<div class="f-16">

{{ slotScope.selectedHrOptionData.ShippingEstimation }}

</div>

</div>

<div class="product-info__detail-item"
v-if="slotScope.showAddToCartButton &amp;&amp; !slotScope.errorAddingProductToCart &amp;&amp; !slotScope.errorPricesLoading">

<div id="add-to-cart" class="product-info__buttons"
v-if="!slotScope.loading &amp;&amp; slotScope.showAddToCartButton &amp;&amp; !slotScope.errorAddingProductToCart &amp;&amp; !slotScope.errorPricesLoading"
anchor-id="add-to-cart">

{{ slotScope.addToCartButtonText }}

<div class="alert alert--danger m-b-sm f-center"
v-if="slotScope.errorAddingProductToCart">

{{ slotScope.errorAddingProductToCart }}

</div>

</div>

</div>

<div class="user-error-message f-16 xs-p-16"
v-if="slotScope.userErrorMessage">

<div class="icon-container">

</div>

<div>

{{ slotScope.userErrorMessage }}

</div>

</div>

<div class="product-info__detail-item"
v-if="!slotScope.loading &amp;&amp; !slotScope.showAddToCartButton &amp;&amp; slotScope.priceAvailable &amp;&amp; !slotScope.isInStock &amp;&amp; !slotScope.preOrderOnly &amp;&amp; !slotScope.customizable">

{{ slotScope.sendNotificationLinkText }}

</div>

<div class="u-flex product-info__find-dealers"
v-if="slotScope.customizable &amp;&amp; !slotScope.notInStockButCustomizable">

<span class="btn btn--default u-flex u-flex-center u-width-100"
v-if="slotScope.customizable &amp;&amp; !slotScope.notInStockButCustomizable"
:href="slotScope.selectedProductData.CustomizerUrl">Customize and
buy</span>

</div>

</div>

</div>

</div>

<div if="slotScope.isKlarnaEnabled &amp;&amp; slotScope.selectedHrOptionData.PriceNumeric &amp;&amp; (slotScope.hasPrice || (slotScope.priceAvailable &amp;&amp; slotScope.selectedHrOptionData.IsPromoPrice))">

</div>

<div class="product-info__bullet-list-container">

<div class="product-info__bullet-list-wrapper">

<div>

- <div class="u-flex u-flex-valign-center">

  <span class="xs-f-16" v-if="info &amp;&amp; info.Title" :key="index">
  {{ info.Title }} </span>

  </div>

<div class="m-t-sm u-flex-align-self-center"
v-if="slotScope.isB2xCustomer">

</div>

</div>

</div>

</div>

</div>

</div>

<div class="p-md u-flex u-flex-valign-center u-flex-justify-space-between">

<span class="f-bold f-16">Please alert me when this product is back in
stock</span>

</div>

<div class="p-md">

<div class="form-group"
:class="{ 'has-error': slotScope.emailAddressNotValid }">

<div class="form-group__error m-t-sm">

This email address is not valid

</div>

</div>

<div class="form-group switch">

<span class="slider"></span> I want to receive updates about new product
releases, exclusive offers and more.

</div>

<div :class="['product-info__alert-subscribe', { active: slotScope.modalForm.newsletterSubscription }]">

<div class="form-group m-0">

Your country or region: <span class="f-monza">\*</span>

<div class="select-element">

Afghanistan Åland Islands Albania Algeria American Samoa Andorra Angola
Anguilla Antarctica Antigua & Barbuda Argentina Armenia Aruba Ascension
Island Australia Austria Azerbaijan Bahamas Bahrain Bangladesh Barbados
Belarus Belgium Belize Benin Bermuda Bhutan Bolivia Bosnia & Herzegovina
Botswana Bouvet Island Brazil British Indian Ocean Territory British
Virgin Islands Brunei Bulgaria Burkina Faso Burundi Cambodia Cameroon
Canada Canary Islands Cape Verde Caribbean Netherlands Cayman Islands
Central African Republic Ceuta & Melilla Chad Chile Christmas Island
Clipperton Island Cocos \[Keeling\] Islands Colombia Comoros Congo -
Brazzaville Congo - Kinshasa Cook Islands Costa Rica Côte d’Ivoire
Croatia Cuba Curaçao Cyprus Czechia Denmark Diego Garcia Djibouti
Dominica Dominican Republic Ecuador Egypt El Salvador Equatorial Guinea
Eritrea Estonia Ethiopia Falkland Islands Faroe Islands Fiji Finland
France French Guiana French Polynesia French Southern Territories Gabon
Gambia Georgia Germany Ghana Gibraltar Greece Greenland Grenada
Guadeloupe Guam Guatemala Guernsey Guinea Guinea-Bissau Guyana Haiti
Heard & McDonald Islands Honduras Hong Kong Area Hungary Iceland India
Indonesia Iran Iraq Ireland Isle of Man Israel Italy Jamaica Japan
Jersey Jordan Kazakhstan Kenya Kiribati Kosovo Kuwait Kyrgyzstan Laos
Latvia Lebanon Lesotho Liberia Libya Liechtenstein Lithuania Luxembourg
Macau China Macedonia Madagascar Malawi Malaysia Maldives Mali Malta
Marshall Islands Martinique Mauritania Mauritius Mayotte Mexico
Micronesia Moldova Monaco Mongolia Montenegro Montserrat Morocco
Mozambique Myanmar \[Burma\] Namibia Nauru Nepal Netherlands New
Caledonia New Zealand Nicaragua Niger Nigeria Niue Norfolk Island North
Korea Northern Mariana Islands Norway Oman Pakistan Palau Palestinian
Territories Panama Papua New Guinea Paraguay Peru Philippines Pitcairn
Islands Poland Portugal Puerto Rico Qatar Réunion Romania Russia Rwanda
Samoa San Marino São Tomé & Príncipe Saudi Arabia Senegal Serbia
Seychelles Sierra Leone Singapore Sint Maarten Slovakia Slovenia So.
Georgia & So. Sandwich Isl. Solomon Islands Somalia South Africa South
Korea South Sudan Spain Sri Lanka St. Barthélemy St. Helena St. Kitts &
Nevis St. Lucia St. Martin St. Pierre & Miquelon St. Vincent &
Grenadines Sudan Suriname Svalbard & Jan Mayen Swaziland Sweden
Switzerland Syria Taiwan Area Tajikistan Tanzania Thailand Timor-Leste
Togo Tokelau Tonga Trinidad & Tobago Tristan da Cunha Tunisia Turkey
Turkmenistan Turks & Caicos Islands Tuvalu U.S. Outlying Islands U.S.
Virgin Islands Uganda Ukraine United Arab Emirates United Kingdom United
States Uruguay Uzbekistan Vanuatu Vatican City Venezuela Vietnam Wallis
& Futuna Western Sahara Yemen Zambia Zimbabwe

</div>

</div>

</div>

<div class="form-group m-b-0"
:class="{ 'has-error': slotScope.modalForm.formError, 'success': slotScope.modalForm.success }">

Send notification

<div class="form-group__error m-t-lg"
v-show="slotScope.modalForm.formError">

{{ slotScope.modalForm.formError }}

</div>

<div class="form-group__success m-t-lg"
v-show="slotScope.modalForm.success">

{{ slotScope.modalForm.success }}

</div>

</div>

</div>

</div>

</div>

<div class="product-page__related-blocks u-width-100">

<div id="Keyfeatures" anchor-id="Keyfeatures">

</div>

<div class="u-relative u-width-100" epi-block-id="35542">

</div>

<div id="key-features-2" anchor-id="key-features-2">

</div>

<div id="compatible-products" anchor-id="compatible-products">

</div>

<div class="u-relative u-width-100 u-bg-light-gray"
epi-block-id="35548">

<div class="row">

<div class="col-xs-12">

## {{ slotScope.blockTitle }}

<div class="product-block col-lg-3 col-md-4 p-0 col-xs-12 col-sm-6 u-relative"
v-for="(product, index) in slotScope.items" :key="index"
:data-product-id="product.Ssid">

</div>

<div class="f-center" v-if="slotScope.loading">

</div>

</div>

</div>

</div>

<div id="compatible-products-accessory-page"
anchor-id="compatible-products-accessory-page">

</div>

<div class="u-relative u-width-100 u-bg-light-gray"
epi-block-id="119444">

<div class="row">

<div class="col-xs-12">

## {{ slotScope.blockTitle }}

<div class="product-block col-lg-3 col-md-4 p-0 col-xs-12 col-sm-6 u-relative"
v-for="(product, index) in slotScope.items" :key="index"
:data-product-id="product.Ssid">

</div>

<div class="f-center" v-if="slotScope.loading">

</div>

</div>

</div>

</div>

</div>

<div class="product-page__bottom u-width-100">

<div id="support" anchor-id="support">

</div>

<div class="full-width-container full-width-container--bg-image"
epi-block-id="118183">

<div class="u-relative">

<div class="lazy-full-width lazyload"
:data-bg="!$mq.maxWidthPhone ? '/globalassets/new-product-page/support-block-for-product-pages/product-support-block-image-1440x400px-05.jpg?mode=min&amp;width=1440&amp;format=jpg' : '/globalassets/new-product-page/support-block-for-product-pages/product-support-block-image-1440x400px-05.jpg?mode=min&amp;width=1440&amp;format=jpg'">

</div>

<div class="full-width-container__content">

<div class="container-fluid wrapper">

<div class="row">

<div class="col-xs-12 f-center">

## Do you have questions or need help?

<a href="/link/541309f8eed941fcbe80e50f7a13f256.aspx"
class="f-16 btn btn--brand btn--ib">Find support here</a>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="footer__social-networks container-fluid wrapper p-v-xxl">

Follow us

<a href="https://www.facebook.com/Suunto"
class="suunto-icon suunto-icon-facebook"
data-footer-some-link="Facebook" target="_blank"
rel="noreferrer nofollow" title="Facebook"></a>
<a href="https://instagram.com/suunto"
class="suunto-icon suunto-icon-instagram"
data-footer-some-link="Instagram" target="_blank"
rel="noreferrer nofollow" title="Instagram"></a>
<a href="https://www.youtube.com/suuntoTV"
class="suunto-icon suunto-icon-youtube" data-footer-some-link="Youtube"
target="_blank" rel="noreferrer nofollow" title="Youtube"></a>
<a href="https://www.tiktok.com/@suuntoglobal"
class="suunto-icon suunto-icon-tiktok" data-footer-some-link="TikTok"
target="_blank" rel="noreferrer nofollow" title="TikTok"><img
src="data:image/svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgd2lkdGg9IjQwIiBoZWlnaHQ9IjMyIiB2aWV3Ym94PSIwIDAgMzIgMzIiPgogICAgICAgICAgICAgICAgICAgIDxwYXRoIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lam9pbj0ibWl0ZXIiIHN0cm9rZS1saW5lY2FwPSJidXR0IiBzdHJva2UtbWl0ZXJsaW1pdD0iNCIgc3Ryb2tlLXdpZHRoPSIyIiBkPSJNMTYgMS4zMzNjOC4xIDAgMTQuNjY3IDYuNTY2IDE0LjY2NyAxNC42NjdzLTYuNTY2IDE0LjY2Ny0xNC42NjcgMTQuNjY3Yy04LjEgMC0xNC42NjctNi41NjYtMTQuNjY3LTE0LjY2N3M2LjU2Ni0xNC42NjcgMTQuNjY3LTE0LjY2N3oiIC8+CiAgICAgICAgICAgICAgICAgICAgPHBhdGggZD0iTTIxLjcxNCA4LjVoLTExLjQyOGMtMC40NzMgMC0wLjkyOCAwLjE4OS0xLjI2MyAwLjUyNHMtMC41MjQgMC43ODktMC41MjQgMS4yNjN2MTEuNDI4YzAgMC40NzMgMC4xODkgMC45MjggMC41MjQgMS4yNjNzMC43ODkgMC41MjMgMS4yNjMgMC41MjNoMTEuNDI4YzAuNDczIDAgMC45MjgtMC4xODkgMS4yNjMtMC41MjNzMC41MjMtMC43ODkgMC41MjMtMS4yNjN2LTExLjQyOGMwLTAuNDczLTAuMTg5LTAuOTI4LTAuNTIzLTEuMjYzcy0wLjc4OS0wLjUyNC0xLjI2My0wLjUyNHpNMjAuMjg3IDE1LjA0NGMtMC4wNzkgMC4wMDgtMC4xNjUgMC4wMTItMC4yNDcgMC4wMTMtMC40NDUgMC0wLjg4Mi0wLjExMS0xLjI3My0wLjMyMnMtMC43MjMtMC41MTctMC45NjctMC44ODl2NC4xMmMwIDAuNjAyLTAuMTc4IDEuMTkxLTAuNTEzIDEuNjkycy0wLjgxIDAuODkxLTEuMzY2IDEuMTIyYy0wLjU1NiAwLjIzLTEuMTY5IDAuMjkxLTEuNzU5IDAuMTczcy0xLjEzNC0wLjQwOC0xLjU1OS0wLjgzM2MtMC40MjYtMC40MjYtMC43MTYtMC45NjgtMC44MzMtMS41NTlzLTAuMDU3LTEuMjAzIDAuMTczLTEuNzU5YzAuMjMtMC41NTYgMC42Mi0xLjAzMiAxLjEyMS0xLjM2NnMxLjA4OS0wLjUxMyAxLjY5Mi0wLjUxM2MwLjA2NCAwIDAuMTI2IDAuMDA1IDAuMTg4IDAuMDA5djEuNWMtMC4yMS0wLjAyNi0wLjQyMy0wLjAwOS0wLjYyNyAwLjA1MHMtMC4zOTIgMC4xNi0wLjU1NiAwLjI5NWMtMC4xNjMgMC4xMzUtMC4yOTcgMC4zMDMtMC4zOTIgMC40OTFzLTAuMTUxIDAuMzk1LTAuMTY0IDAuNjA3Yy0wLjAxMyAwLjIxMSAwLjAxOCAwLjQyMyAwLjA5MCAwLjYyMnMwLjE4NCAwLjM4MiAwLjMzIDAuNTM2IDAuMzIxIDAuMjc3IDAuNTE1IDAuMzYxYzAuMTk0IDAuMDg0IDAuNDA0IDAuMTI2IDAuNjE2IDAuMTI2IDAuNDE3IDAuMDA3IDAuODE5LTAuMTUxIDEuMTIxLTAuNDM3czAuNDgtMC42ODEgMC40OTUtMS4wOTdsMC4wMTUtNi45OTdoMS40MzZjMC4wNjYgMC42MjQgMC4zNDkgMS4yMDUgMC43OTkgMS42NDJzMS4wNDAgMC43MDEgMS42NjYgMC43NDZ2MS42Njh6IiAvPgogICAgICAgICAgICAgICAgPC9zdmc+" /></a>
<a href="/suunto-rss-feeds/" class="suunto-icon suunto-icon-rss"
data-footer-some-link="RSS Feed" target="_blank"
rel="noreferrer nofollow" title="RSS Feed"></a>

</div>

<div class="footer__links container-fluid wrapper">

<div class="row">

<div class="col-xs-12 col-lg-12">

<div class="row">

<div class="footer__links-container p-v-xl" v-if="!$mq.laptop">

- Country and language

- <div class="u-width-100">

  </div>

</div>

<div class="footer__links-container p-v-xl">

- Support
- <a
  href="/Support/Suunto-Webshop/faqsforsuuntowebshop/returns-and-refunds/"
  data-footer-support-link="">Returns and refunds</a>
- <a href="/Redirects/For-navigation/Contact-information/"
  data-footer-support-link="">Support main page</a>
- <a href="/Support/Software-updates/"
  data-footer-support-link="">Software updates</a>
- <a href="/Support/User-guides/" data-footer-support-link="">User
  guides</a>
- <a href="/Support/suunto-repair-center/"
  data-footer-support-link="">Suunto Repair Center</a>
- <a href="/Support/Service-Centers/suunto-service-centers/"
  data-footer-support-link="">Service Centers</a>
- <a href="/Redirects/For-navigation/Tutorial-Tuesday1/"
  data-footer-support-link="">Tutorial Tuesday</a>
- <a href="/Redirects/For-navigation/contact-us/"
  data-footer-support-link="">Contact us</a>

</div>

<div class="footer__links-container p-v-xl">

- Where to buy
- <a href="/Support/Suunto-Webshop/" data-footer-buy-link="">Suunto
  Webshop</a>
- <a href="/Support/Suunto-Webshop/faqsforsuuntowebshop/"
  data-footer-buy-link="">FAQs for Suunto Webshop</a>
- <a href="/suunto-pro-club/" data-footer-buy-link="">Suunto Pro Club</a>

</div>

<div class="footer__links-container p-v-xl">

- About Suunto
- <a href="/News/?category=news" data-footer-about-link="">News</a>
- <a href="/About-Suunto/Company-info/" data-footer-about-link="">Company
  info</a>
- <a href="/About-Suunto/Company-info/Careers/"
  data-footer-about-link="">Careers</a>
- <a href="/About-Suunto/heritage/" data-footer-about-link="">Heritage</a>
- <a href="/About-Suunto/Media/" data-footer-about-link="">Media</a>
- <a href="/About-Suunto/Sustainability/"
  data-footer-about-link="">Sustainability</a>
- <a href="/About-Suunto/eu-declarations-of-conformity/"
  data-footer-about-link="">EU Declarations of Conformity</a>
- <a href="/About-Suunto/whistleblowing/"
  data-footer-about-link="">Whistleblowing</a>

</div>

<div class="footer__links-container p-v-xl">

- Partners
- <a href="/partners/strava/" data-footer-partner-link="">Strava</a>
- <a href="/partners/trainingpeaks/"
  data-footer-partner-link="">TrainingPeaks</a>
- <a href="/partners/value-pack/" data-footer-partner-link="">Value
  Pack</a>
- <a href="/partners/welcome-partners/"
  data-footer-partner-link="">Welcome Partners</a>
- <a href="/partners/partners/" data-footer-partner-link="">Partners</a>

</div>

<div class="footer__links-container p-v-xl" v-if="$mq.laptop">

- Country and language

- <div class="u-width-100">

  </div>

</div>

</div>

</div>

</div>

</div>

<div class="footer__bottom-page container-fluid wrapper">

<div class="row">

<div class="col-xs-12 f-center">

<div class="f-uppercase f-12 f-center u-block">

<span class="u-inline-block">.</span>
<span class="u-inline-block">Copyright © 2025 Suunto.</span>
<span class="u-inline-block">All Rights Reserved. </span>

[Terms of use](/Terms-of-use/) \| [Privacy Policy](/Privacy-Policy/) \|
[SECURITY](/legal-pages/suunto-responsible-disclosure-policy/) \|
[Cookies](/legal-pages/cookies/) \|
<a href="#cookie-preference-center" id="ot-sdk-btn"
class="ot-sdk-show-settings cookie-preference-center">Cookie
Preferences</a> \| [\#YESsuunto terms](/legal-pages/yessuunto-terms/)

</div>

</div>

</div>

</div>

</div>
