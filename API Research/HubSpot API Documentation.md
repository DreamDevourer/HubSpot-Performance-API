# [CMS Performance](https://developers.hubspot.com/docs/api/cms/performance)

The CMS Performance API enables teams to monitor their HubSpot hosted pages for issues that may impact the experience of visitors on the website. These metrics include things like uptime, status, 1xx- 5xx errors, cache hits, total requests, and median response times, making it easy for administrators to take action quickly in the event of a problem.

Please note that metrics may not be updated in real-time, as there may be a 20-30 minute delay in the data.

This data is purged over time, depending on the resolution of the data:

1 minute - 5 minutes: purged after 1 week
10 minutes - 30 minutes: purged after 1 month
1 hour - 12 hours: purged after 6 months
1 day - 1 week: purged after 2 years

**Example use case:** You want to pull a list of pages that are resulting in 404 errors.

# Endpoints

### GET /cms/v3/performance/

View your website's performance.
Returns time series data website performance data for the given domain and/or path.

<div class="m-bottom-6"><h5 aria-level="2" class="Heading-sc-1hkwu4q-0 H5-sc-1ovzlng-0 jKVpfo"><i18n-string data-locale-at-render="en-us" data-key="requirements.header">Requirements</i18n-string></h5><div class="UISection__ScrollWrapper-km1xsp-0 hhzzde is--module namespaced-hack-section table-responsive private-scroll__wrapper--tables"><div class="UIScrollOverhang__Wrapper-sc-14qth5k-0 jUObZg UITable__TableScrollContainer-hews7f-0 vCoKA"><div class="UIScrollContainer__DefaultScrollContainer-sc-16o182o-0 axDBA"><table class="UITable__Table-hews7f-1 bDlFnc table private-table Requirements__StyledTable-sc-1imfjth-0 hDgksK table-condensed private-table--condensed"><colgroup><col style="width: 152px;"><col></colgroup><tbody><tr><th class="Requirements__StyledScopeTH-sc-1imfjth-2 cefDgE"><i18n-string data-locale-at-render="en-us" data-key="requirements.scopes.header.scopes">Scopes</i18n-string></th><td class="Requirements__StyledTD-sc-1imfjth-3 iXOUeX"><i18n-string data-locale-at-render="en-us" data-key="requirements.scopes.noScopes">None</i18n-string></td></tr><tr><th class="Requirements__StyledTH-sc-1imfjth-1 hesbgN"><i18n-string data-locale-at-render="en-us" data-key="requirements.limits.header">Limits</i18n-string></th><td class="Requirements__StyledTD-sc-1imfjth-3 iXOUeX"><span><a class="private-link uiLinkWithoutUnderline uiLinkDark" href="https://developers.hubspot.com/docs/api/usage-details#rate-limits" rel="noopener noreferrer" tabindex="0" target="_blank">Standard API rate limits<span aria-label="Link opens in a new window" class="private-icon private-icon__low UILink__DefaultExternalIcon-sc-1sve251-0 efvTeE private-link--external__icon" data-icon-name="externalLink"><span aria-hidden="true" class="UIIcon__IconContent-sc-19xvtk3-0 jJMfbx"></span></span></a></span></td></tr></tbody></table></div><div size="14" opacity="0" class="UIOverhang-ov2xiu-0 bwcqyM"></div><div size="14" opacity="0" class="UIOverhang-ov2xiu-0 ggOkEQ"></div><div size="14" opacity="0" class="UIOverhang-ov2xiu-0 coKpEJ"></div><div size="14" opacity="0" class="UIOverhang-ov2xiu-0 jLsyzC"></div></div></div></div>

<div class="params"><h5 aria-level="2" class="Heading-sc-1hkwu4q-0 H5-sc-1ovzlng-0 jKVpfo"><i18n-string data-locale-at-render="en-us" data-key="params.header.parameters">Parameters</i18n-string></h5><div><div class="params-block"><div class="params-row" data-test-id="schema-field-get-/cms/v3/performance/-domain"><div class="params-pair"><div class="params-descriptor-wrapper"><div class="params-descriptor"><label aria-describedby="get-/cms/v3/performance/_getPage-domain-description" for="get-/cms/v3/performance/_getPage-domain" class="private-form__label p-all-0">domain</label><small class="private-microcopy display-block is--text--help"><i18n-string data-locale-at-render="en-us" data-key="types.string">String</i18n-string></small><small class="private-microcopy display-block is--text--help"><i18n-string data-locale-at-render="en-us" data-key="params.body.schemaGroup.QueryParams">Query param</i18n-string></small></div></div><div class="params-content"><p><span id="get-/cms/v3/performance/_getPage-domain-description"><span class="markdown hyphens-none">The domain to search return data for.</span></span></p><small class="private-microcopy"><a data-test-id="set-test-value" class="private-link uiLinkWithoutUnderline uiLinkDark" role="button" tabindex="0"><i18n-string data-locale-at-render="en-us" data-key="params.body.setTestValue">+ Set test value</i18n-string></a></small></div></div></div><div class="params-row" data-test-id="schema-field-get-/cms/v3/performance/-path"><div class="params-pair"><div class="params-descriptor-wrapper"><div class="params-descriptor"><label aria-describedby="get-/cms/v3/performance/_getPage-path-description" for="get-/cms/v3/performance/_getPage-path" class="private-form__label p-all-0">path</label><small class="private-microcopy display-block is--text--help"><i18n-string data-locale-at-render="en-us" data-key="types.string">String</i18n-string></small><small class="private-microcopy display-block is--text--help"><i18n-string data-locale-at-render="en-us" data-key="params.body.schemaGroup.QueryParams">Query param</i18n-string></small></div></div><div class="params-content"><p><span id="get-/cms/v3/performance/_getPage-path-description"><span class="markdown hyphens-none">The url path of the domain to return data for.</span></span></p><small class="private-microcopy"><a data-test-id="set-test-value" class="private-link uiLinkWithoutUnderline uiLinkDark" role="button" tabindex="0"><i18n-string data-locale-at-render="en-us" data-key="params.body.setTestValue">+ Set test value</i18n-string></a></small></div></div></div><div class="params-row" data-test-id="schema-field-get-/cms/v3/performance/-pad"><div class="params-pair"><div class="params-descriptor-wrapper"><div class="params-descriptor"><label aria-describedby="get-/cms/v3/performance/_getPage-pad-description" for="get-/cms/v3/performance/_getPage-pad" class="private-form__label p-all-0">pad</label><small class="private-microcopy display-block is--text--help"><i18n-string data-locale-at-render="en-us" data-key="types.boolean">Boolean</i18n-string></small><small class="private-microcopy display-block is--text--help"><i18n-string data-locale-at-render="en-us" data-key="params.body.schemaGroup.QueryParams">Query param</i18n-string></small></div></div><div class="params-content"><p><span id="get-/cms/v3/performance/_getPage-pad-description"><span class="markdown hyphens-none">Specifies whether the time series data should have empty intervals if performance data is not present to create a continuous set.</span></span></p><small class="private-microcopy"><a data-test-id="set-test-value" class="private-link uiLinkWithoutUnderline uiLinkDark" role="button" tabindex="0"><i18n-string data-locale-at-render="en-us" data-key="params.body.setTestValue">+ Set test value</i18n-string></a></small></div></div></div></div></div></div>

## SAMPLE JSON RESPONSE
```json
{
  "data": [
    {
      "403": 0,
      "404": 0,
      "500": 0,
      "504": 0,
      "startTimestamp": 0,
      "endTimestamp": 0,
      "startDatetime": "string",
      "endDatetime": "string",
      "totalRequests": 0,
      "cacheHits": 0,
      "cacheHitRate": 0,
      "totalRequestTime": 0,
      "avgOriginResponseTime": 0,
      "responseTimeMs": 0,
      "100X": 0,
      "20X": 0,
      "30X": 0,
      "40X": 0,
      "50X": 0,
      "50th": 0,
      "95th": 0,
      "99th": 0
    }
  ],
  "domain": "string",
  "path": "string",
  "startInterval": 0,
  "endInterval": 0,
  "interval": "ONE_MINUTE",
  "period": "ONE_MINUTE"
}
```
## Error Response

```json
{
  "message": "Invalid input (details will vary based on the error)",
  "correlationId": "aeb5f871-7f07-4993-9211-075dc63e7cbf",
  "category": "VALIDATION_ERROR",
  "links": {
    "knowledge-base": "https://www.hubspot.com/products/service/knowledge-base"
  }
}
```
