# SOTI MobiControl API Documentation

# Table of Contents

1. [Introduction](#introduction)
2. [Authentication](#authentication)
3. [API Usage Guide](#api-usage-guide)
4. [Error Handling](#error-handling)
5. [API Endpoints](#api-endpoints)

   1. [Agents And Plugins](#agents-and-plugins)
   2. [Android Applications Package](#android-applications-package)
   3. [Android Configuration](#android-configuration)
   4. [Android Enrollment Configuration Qr Code](#android-enrollment-configuration-qr-code)
   5. [Android Enrollment Policies](#android-enrollment-policies)
   6. [Android Enterprise Certificates](#android-enterprise-certificates)
   7. [Android Firmware Upgrade Client](#android-firmware-upgrade-client)
   8. [Apns Configuration](#apns-configuration)
   9. [App Management Android Apps](#app-management-android-apps)
   10. [App Management Android Policies](#app-management-android-policies)
   11. [App Management Apple Policies](#app-management-apple-policies)
   12. [App Management Policies](#app-management-policies)
   13. [App Management Windows Apps](#app-management-windows-apps)
   14. [App Management Windows Policies](#app-management-windows-policies)
   15. [Apple Applications](#apple-applications)
   16. [Apple Automated Device Enrollment](#apple-automated-device-enrollment)
   17. [Apple Ios Wallpaper](#apple-ios-wallpaper)
   18. [Apple Redemption Codes](#apple-redemption-codes)
   19. [Apple Volume Purchase Program Account](#apple-volume-purchase-program-account)
   20. [Branding](#branding)
   21. [Catalogue Item Management](#catalogue-item-management)
   22. [Certificate Management](#certificate-management)
   23. [Compliance Policies](#compliance-policies)
   24. [Custom Attributes](#custom-attributes)
   25. [Custom Data](#custom-data)
   26. [Device Configuration](#device-configuration)
   27. [Device Group App Policy](#device-group-app-policy)
   28. [Device Groups](#device-groups)
   29. [Device Kind Schema](#device-kind-schema)
   30. [Device Script](#device-script)
   31. [Device Script Execution Status](#device-script-execution-status)
   32. [Devices](#devices)
   33. [Directories](#directories)
   34. [Email](#email)
   35. [Enrollment Configuration](#enrollment-configuration)
   36. [Enrollment Rules](#enrollment-rules)
   37. [External Services](#external-services)
   38. [Geofences](#geofences)
   39. [Google Domain Management](#google-domain-management)
   40. [Health Attestation](#health-attestation)
   41. [Identity Providers](#identity-providers)
   42. [Ios Enrollment Policies](#ios-enrollment-policies)
   43. [Jobs](#jobs)
   44. [License Management](#license-management)
   45. [Linux Enrollment Policies](#linux-enrollment-policies)
   46. [Locate Timeout](#locate-timeout)
   47. [Logs](#logs)
   48. [Mac Enrollment Policies](#mac-enrollment-policies)
   49. [Mac File Vault Certificate](#mac-file-vault-certificate)
   50. [Mail Servers](#mail-servers)
   51. [Managed Google Play Management](#managed-google-play-management)
   52. [Microsoft365 App Protection Policies](#microsoft365-app-protection-policies)
   53. [Microsoft365 Conditional Access](#microsoft365-conditional-access)
   54. [Microsoft365 Mobile Apps](#microsoft365-mobile-apps)
   55. [Packages](#packages)
   56. [Product](#product)
   57. [Profiles](#profiles)
   58. [Reports](#reports)
   59. [Role Management](#role-management)
   60. [Schedules](#schedules)
   61. [Search](#search)
   62. [Search Server](#search-server)
   63. [Security](#security)
   64. [Server Health](#server-health)
   65. [Servers](#servers)
   66. [Signal Health](#signal-health)
   67. [Signal Policies](#signal-policies)
   68. [Signal Schema](#signal-schema)
   69. [Smtp](#smtp)
   70. [Soti Assist Configuration](#soti-assist-configuration)
   71. [Soti Connect Configuration](#soti-connect-configuration)
   72. [Soti Snap Configuration](#soti-snap-configuration)
   73. [System Configuration](#system-configuration)
   74. [System Health](#system-health)
   75. [System Maintenance](#system-maintenance)
   76. [Terms And Conditions](#terms-and-conditions)
   77. [User Group Management](#user-group-management)
   78. [User Management](#user-management)
   79. [Webhook Credentials](#webhook-credentials)
   80. [Webhooks](#webhooks)
   81. [Windows Bit Locker Keys](#windows-bit-locker-keys)
   82. [Windows Modern Enrollment Policies](#windows-modern-enrollment-policies)
   83. [Windows Updates](#windows-updates)
   84. [Wns Configuration](#wns-configuration)
   85. [Zebra Android Firmware Upgrade Client Summary](#zebra-android-firmware-upgrade-client-summary)

## Introduction

Integration of common device lifecycle management functions within your organization’s mobility workflow is made possible with the MobiControl REST API that is exposed over HTTPS as a set of RESTful web services.

The MobiControl REST API is designed to have predictable resource-oriented URLs and standard HTTP response codes. The API is protected by OAuth2 and is swagger-specification compliant for integration with off-the-shelf HTTP clients.

This documentation provides you with detailed information on the MobiControl REST API available with your MobiControl environment, and gives you the ability to interact with the API calls on this page to test their functionality.

<b id="Warning1" >WARNING: API calls sent from this page are executed against your MobiControl environment. Exercise extreme caution when executing each API call against a production environment and/or device.\*\*

For consultation and/or support of your MobiControl integration please contact SOTI’s Professional Services and Support teams.
Please note that all API calls utilize double encoding, unless otherwise stated in the corresponding API call documentation.

**Authentication**

MobiControl API calls are protected by OAuth2 (RFC 6749), and support both Resource Owner, and Authorization Code grant types. In both scenarios the "Resource Owner" is a named MobiControl administrator account and the "authorization server" is MobiControl which will authenticate users locally, or if configured through a 3rd party identity provider.

To call the MobiControl API successfully, you must authenticate to the authorization server and receive an access token to use in subsequent API calls.

At a minimum you must: - &nbsp;&nbsp;&nbsp;Possess a MobiControl administrator’s username and password that is either provided directly to MobiControl, or to a configured identity provider- &nbsp;&nbsp;&nbsp;Have added your application as an API client, and possess its Client ID and Client secret.

**API Client**

An API client is a combination of a Client ID and a Client Secret that uniquely identifies your integrated application to MobiControl and authorizes it to make API calls. It is required in addition to the MobiControl administrator credentials when obtaining an access token to authenticate subsequent API calls.

SOTI recommends that you register each integrated application you develop independently so the application can be independently revoked if it is compromised.

**Adding an API Client**

To add an API client, you must have administrative access to the Windows server where MobiControl is hosted. If you are a MobiControl cloud customer, please contact SOTI support to add an API client.

You can add an API client by launching the MobiControl Administration Utility (MCAdmin) through the command line with additional parameters.- &nbsp;&nbsp;&nbsp;Launch a Windows command prompt with administrative privileges.- &nbsp;&nbsp;&nbsp;Navigate to the MobiControl installation directory.- &nbsp;&nbsp;&nbsp;Execute the following command where:<ul style="list-style-type:disc;">- &nbsp;&nbsp;&nbsp;_API client name_ is a reference to your integrated application- &nbsp;&nbsp;&nbsp;_API secret_ (optional) is the passphrase that will be used to protect the API. This should be stored securely and is irrecoverable if lost. An API secret will be generated for you if one was not provided.- &nbsp;&nbsp;&nbsp;_Redirect URL_ is the destination endpoint. The authorization server will return the user agent here

MCAdmin.exe APIClientAdd -n:{API client name} [-p:{API secret}] [-r:{Redirect URI}]```

If MCAdmin was started with the _APIClientAdd_ command and the correct parameters, a summary of the executed operation will be presented that reports the Client ID and Client ecret that were generated. For example:

API Client was added
Client ID: a9326fd5872f4a66b6bab3e2c8065e63
Client secret: 19DzUX7K7ObjwPRFbxZanwVQFsUcqMak```

**Removing an API Client**

If you want to revoke the ability for an API client to make API calls, you can use the _APIClientRemove_ command.

- &nbsp;&nbsp;&nbsp;Launch a Windows command prompt with administrative privileges.- &nbsp;&nbsp;&nbsp;Navigate to the MobiContorl installation directory.- &nbsp;&nbsp;&nbsp;Execute the following command where _client ID_ is the ID for your integrated application.

MCAdmin.exe APIClientRemove -i:{client id}```

If you started MCAdmin with the _APIClientRemove_ command and the correct parameters, a summary of the executed operation will be presented that reports whether the client was removed successfully.

**Access Token (Also Known As “bearer”)**

Before executing a resource-based API call, you must first obtain an access token by making a specific request to the authorization server.

For Resource Owner grant type, the authorization server for requesting access tokens is hosted at _/token_ and can be called directly with the administrative credentials.

For example: https://server.domain.tld/MobiControl/api/token.

For Authorization Code grant type you must first make a GET request to _/authorize_ that contains your Client ID. Your may preserve the state of your application in the state property of the request

For example:

GET
https://server.domain.tld/mobicontrol/oauth/authorize?response_type=code&client_id=abc&state=xyz

If an external identity provider is configured you will be redirected to their login page. Upon successful authentication you will be provided with an authorization code to exchange for an access token. If an external identity provider is not configured, you will be redirected to MobiControl's login page.

Access tokens are time sensitive with the validity contained in the response. In case of expiration, the value used by the client must be refreshed with another token request.

**Request an Access Token**

Make a POST request that includes an _Authorization_: header containing the API Client ID and Secret, and the body containing either MobiControl administrator credentials or an authorization code.

The Authorization header field must be constructed as follows:- &nbsp;&nbsp;&nbsp;Combine the _client ID_ and _client secret_ into a string separated by a colon. For example: _ClientID:ClientSecret_. Note that these fields cannot otherwise contain a colon.- &nbsp;&nbsp;&nbsp;Encode the resulting string using the RFC2045-MIME variant of Base64, except not limited to 76 characters per line.- &nbsp;&nbsp;&nbsp;Prefix _Basic_ before the encoded string.
The body of the request must contain the following parameters and will depend on your grant type.
For **Resource Owner** grant type:- &nbsp;&nbsp;&nbsp;_grant_type_: set to _password_- &nbsp;&nbsp;&nbsp;_username_: of the MobiControl administrator (_administrator_ in the example below)- &nbsp;&nbsp;&nbsp;_password_: of the MobiControl administrator (_1_ in the example below)

POST https://server.domain.tld/MobiControl/api/token HTTP/1.1
Host: server.domain.tld
Authorization: Basic QXBwbGljYXRpb24xOkFwcGxpY2F0aW9uMVBhc3N3b3Jk
Content-Type: application/x-www-form-urlencoded
Content-Length: 53
grant_type=password&username=Administrator&password=1```

For **Authorization Code** grant type:- &nbsp;&nbsp;&nbsp;_grant_type_: set to _authorization_code&=[authorization code]_

POST https://server.domain.tld/MobiControl/api/token HTTP/1.1
Host: server.domain.tld
Authorization: Basic QXBwbGljYXRpb24xOkFwcGxpY2F0aW9uMVBhc3N3b3Jk
Content-Type: application/x-www-form-urlencoded
Content-Length: 53
grant_type=authorization_code&code=[authorization code]```

In response, the output will contain the following properties:- &nbsp;&nbsp;&nbsp;_access_token_: The access token to be used in every subsequent API request.- &nbsp;&nbsp;&nbsp;_token_type_: The type of token. Will always be set to _bearer_.- &nbsp;&nbsp;&nbsp;_expires_in_: The value in seconds of the token validity. If the token is expired, the client needs to issue an additional token request to retrieve a new token value.
Example of the response:

{"access_token":"AAEAAK0OiDDPciqCR5sZ6Nu6c8wIvURVwCTxslETUGp
xDfmf6uzkXAg9MKzfJqm4k9ADBYIaOsT20wllKWQgQvH5sYkaIWxtOZ9OntAkxwPn
wBRO7rNqCGj9yfg-COpYCdr2GEMl5SzaAPx2_WBQ3SwhKuGWuuDxVMzRWdAW1r36J
Y6N9Fp-rYK3CtoNs4ibqswOs7qSPzuwo_K9l9_c5oCz7d6qJxJdhKoh3MC8vqFXxJ
SXIEAwXnL7KWtrhanIcj_m0abZWfvR7e5npIHDcHH-bfVmc6wp-SsKJ-FyG7_zg2F
d8HjvoqivTqRO5i1RSpaPpOa318g2FMIw-Lh6I5K0FAOUAQAAAAEAABW2-Dr_0-vr
bZGMubz8ZGqpo6Z67n3JqBIFPgMOPotNHVJSUc_2HbozYt7smfuCIeIvE0gd84ti3
LBJXSkiOBPJmxp-WhdC1IbB7y2W5G8D4l5MD3VbDTz6ov_VnZGpRc-h7Q9Knn1Vyk
QTHo4NknDUdVkqDe3VHQsjtn12QINEzb04Ch-RpudIHnKG-P-jhIIszo2M0_Po8_U
aHVwrpPtwhUCzqOU_Gus1nS694dP-8rXqjtbLxh_5GB1iQQBitMd-VgD8XzQrLqqH
a6HcK1C41ZyA1Ot2_47vOKNrf_Mg6Ig8quYMpUypOdwFl9_Nb815TN-eSuDwQsSKn
SnHDvTH8bSz9O0vHoiPexh2Weuf2N0KGZUlpC0OLy3oRb0d_aBOUdpnoIJ59Gc95H
7yTAnNPRuBnX0wDnvTFNkuN7ezKzfP2rNmfKPeoj0Xyf2FhGiSHgBJUuNpWwGJkz5
0tVX5nPl42Ow2ua9pLZqPg-GJQnmXwukVgV6w4dDoRsFVYbrRSdp-quU4pyNfj987
GWM","token_type":"bearer","expires_in":3600}```

**Using an Access Token**

After retrieving an access token it can be used to authenticate every other API call by including it in the Authorization: header of that call with the type Bearer.

Example of a subsequent API request:

GET https://server.domain.tld/MobiControl/api/devicegroups HTTP/1.1
Host: server.domain.tld
Authorization: Bearer AAEAAK0OiDDPciqCR5sZ6Nu6c8wIvURVwCTxslETUGp
xDfmf6uzkXAg9MKzfJqm4k9ADBYIaOsT20wllKWQgQvH5sYkaIWxtOZ9OntAkxwPn
wBRO7rNqCGj9yfg-COpYCdr2GEMl5SzaAPx2_WBQ3SwhKuGWuuDxVMzRWdAW1r36J
Y6N9Fp-rYK3CtoNs4ibqswOs7qSPzuwo_K9l9_c5oCz7d6qJxJdhKoh3MC8vqFXxJ
SXIEAwXnL7KWtrhanIcj_m0abZWfvR7e5npIHDcHH-bfVmc6wp-SsKJ-FyG7_zg2F
d8HjvoqivTqRO5i1RSpaPpOa318g2FMIw-Lh6I5K0FAOUAQAAAAEAABW2-Dr_0-vr
bZGMubz8ZGqpo6Z67n3JqBIFPgMOPotNHVJSUc_2HbozYt7smfuCIeIvE0gd84ti3
LBJXSkiOBPJmxp-WhdC1IbB7y2W5G8D4l5MD3VbDTz6ov_VnZGpRc-h7Q9Knn1Vyk
QTHo4NknDUdVkqDe3VHQsjtn12QINEzb04Ch-RpudIHnKG-P-jhIIszo2M0_Po8_U
aHVwrpPtwhUCzqOU_Gus1nS694dP-8rXqjtbLxh_5GB1iQQBitMd-VgD8XzQrLqqH
a6HcK1C41ZyA1Ot2_47vOKNrf_Mg6Ig8quYMpUypOdwFl9_Nb815TN-eSuDwQsSKn
SnHDvTH8bSz9O0vHoiPexh2Weuf2N0KGZUlpC0OLy3oRb0d_aBOUdpnoIJ59Gc95H
7yTAnNPRuBnX0wDnvTFNkuN7ezKzfP2rNmfKPeoj0Xyf2FhGiSHgBJUuNpWwGJkz5
0tVX5nPl42Ow2ua9pLZqPg-GJQnmXwukVgV6w4dDoRsFVYbrRSdp-quU4pyNfj987
GWM

````

**API Errors**


MobiControl uses conventional HTTP response codes to indicate the success or failure of an API request. In general, codes in the *2xx * range indicate success, codes in the *4xx* range indicate an error resulted from the information provided, and codes in the *5xx* range may indicate an error with MobiControl that cannot be resolved by changing the request.

For troubleshooting purposes, the following provides guidance on the conditions under which MobiControl will return a respective HTTP error code.


**HTTP 400**


This code is generally used to reflect a contract validation error. The data provided in the request was not compliant with the expected input of the method. Normally this is an integration error and can only be resolved programmatically on the client side. Check to ensure the parameters, values, and syntax conform to the expected model.

In addition to the HTTP 400 response, the body will contain a single error object that reports all the violations in the following format:
   - &nbsp;&nbsp;&nbsp;**ErrorCode** (mandatory): set to 0.- &nbsp;&nbsp;&nbsp;**ErrorMessage** (mandatory): the error message.- &nbsp;&nbsp;&nbsp;**Data[]** (optional): extra parameters needed to troubleshoot the problem.- &nbsp;&nbsp;&nbsp;**HelpLink** (optional): a link to possible troubleshooting steps.


**HTTP 401 / HTTP 403**


These codes are security errors. These errors are generated when the login failed, or is required, or if the user is not authorized to perform the action requested.

In addition to the HTTP 401 or HTTP 403 response, the body will contain a single error object to report an error message:- &nbsp;&nbsp;&nbsp;**ErrorMessage** (mandatory): the error message.Please note that the error message may be intentionally vague for security purposes. For additional information consult the environment’s Management Service log.


**HTTP 422**


This type of error is used to represent a business logic error, where the request is correct but it is not possible for the server to complete the request because it violates a logical condition. For example, trying to delete an object with dependencies that would prevent such an object from being deleted.

In addition to the HTTP 422 response, the body will contain a single error object in the following format:  - &nbsp;&nbsp;&nbsp;**ErrorCode** (mandatory): set to 0.- &nbsp;&nbsp;&nbsp;**ErrorMessage** (mandatory): the error message.- &nbsp;&nbsp;&nbsp;**Data[]** (optional): extra parameters needed to troubleshoot the problem.- &nbsp;&nbsp;&nbsp;**HelpLink** (optional): a link to possible troubleshooting steps.


**HTTP 500**


This type of error will be returned when the MobiControl server is unable to process a request.

In addition to the HTTP 500 response, the body will contain a single error object that reports an error message:- &nbsp;&nbsp;&nbsp;**ErrorMessage** (mandatory): set to “Internal Server Error”.For additional information consult the environment’s Management Service log. Report these errors by contacting the SOTI Support team, and include environmental details, the raw HTTP request, and Management Service logs.


**Pagination, Ordering, and Filtering**


Unless otherwise noted, MobiControl API resources have support for bulk fetches, to “list” all devices found in the environment for example.

These “list” API methods use cursor-based pagination, a common structure to define ordering, and property-based filtering which is defined as follows:- &nbsp;&nbsp;&nbsp;*skip* (optional): where in the list you would like to begin. The value will tell the server to remove the first X records retrieved from the result.- &nbsp;&nbsp;&nbsp;*take* (optional): the size of the list you would like returned.- &nbsp;&nbsp;&nbsp;*order* (optional): the ordering criteria in the format *{direction (+/-)}{property name}*, where “+” is ascending and “-” is descending.- &nbsp;&nbsp;&nbsp;*filter* (optional): filter expression, the syntax is different for GET /api/devices/search endpoint (advanced search expressions) and GET /api/devices (name-value pairs)Example of /api/device/search query parameters:





filter=Manufacturer%3D%27Apple%27&order=+osversion,-model&skip=20&take=10```




In the example above we're looking for devices manufactured by "Apple". The devices are first ordered ascending by OS version, then ordered descending by model. Then, the first 20 records are skipped and the next 10 records are returned.


**Resources and API Calls**


The documentation that follows defines all endpoints, parameters and error messages available in the MobiControl REST API.

If you have a valid client ID, client secret, and MobiControl administrator credentials, you can test each API call by clicking the **Authorize** button on the lower right of this page.

<b id="Warning2" >WARNING: API calls sent from this page are executed against your MobiControl environment. Exercise extreme caution when executing each API call against a production environment and/or device.**




## Authentication
MobiControl API calls are protected by OAuth2 (RFC 6749), and support both Resource Owner and Authorization Code grant types.

## API Usage Guide

### Base URL
The base URL for all API requests is: `https://[your-mobicontrol-server]/MobiControl/api`

### Authentication
Before making API calls, you need to obtain an OAuth2 access token:

1. **Request an access token**:
````

POST /token
Authorization: Basic {base64 encoded client_id:client_secret}
Content-Type: application/x-www-form-urlencoded

grant_type=password&username={admin_username}&password={admin_password}

```

2. **Use the access token**:
```

GET /devices
Authorization: Bearer {access_token}

````

### Making Requests
- All requests should include the `Authorization` header with your access token
- For POST and PUT requests, include `Content-Type: application/json` header
- Request and response bodies use JSON format

### Pagination
Many endpoints that return lists support pagination using the following parameters:
- `skip`: Number of items to skip
- `take`: Number of items to retrieve

### Filtering and Sorting
- Use the `filter` parameter to filter results (format: `Property1:Value1,Property2:Value2`)
- Use the `order` parameter to sort results (prefix with + for ascending, - for descending)

## Error Handling

MobiControl uses standard HTTP response codes:
- `2xx`: Success
- `4xx`: Client error (invalid input, authentication issues)
- `5xx`: Server error

Common error codes:
- `400`: Contract validation error (invalid input)
- `401/403`: Authentication/authorization error
- `422`: Business logic error
- `500`: Server error

Error responses include additional information in the response body to help identify the issue.


## API Endpoints

## Agents And Plugins

### GET /agentsAndPlugins/android/agents

**Summary:** Returns a list of Android agents.

**Description:** Returns a list of all Android agents for a manufacturer, either from SOTI Agent Delivery Service or local cache based on the configuration of the parameter 'forceRefresh'.

Requires the caller be granted the "Web Console Access" permission.

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `manufacturer` (Required): Type: string. Description: Manufacturer name.
- `status` (Required): Type: string. Description: Agent Status.
- `forceRefresh`: Type: boolean. Description: When set to True, always pulls agent information from SOTI Agent Delivery Service, instead of locally cached information.
         <br />When set to False, make use of cached data until it's marked stale in 30mins.

**Responses:**
- **200**: return the list of Agent Info objects.
- **401**: Unauthorized access.
- **400**: Contract validation failed.
- **403**: Forbidden.

---
### GET /agentsAndPlugins/android/agents/manufacturers

**Summary:** Returns a list of manufacturers for Android agents.

**Description:** Returns a list of manufacturers for Android agents from SOTI Agent Delivery Service.

Requires the caller be granted the "Web Console Access" permission.

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `status` (Required): Type: string. Description: Agent status.
- `forceRefresh`: Type: boolean. Description: When set to True, always pulls agent information from SOTI Agent Delivery Service, instead of locally cached information.
         <br />When set to False, make use of cached data until it's marked stale in 30mins.

**Responses:**
- **200**: return the list of Manufacture Info objects.
- **401**: Unauthorized access.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>6700 - Android Delivery Service sync is currently in progress. Please wait until it is finished.</li><li>6701 - Android Delivery Service sync could not be completed. Available agents might not be up-to-date.</li></ol>

---
### POST /agentsAndPlugins/android/agents/actions/cancelDownload

**Summary:** Cancel Android agent(s) download to MobiControl.

**Description:** Cancel Android agent(s) download from SOTI Agent Delivery Service to MobiControl.

Requires the caller to be granted "Manage Android Agents and Plugins" permission.

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `referenceId`: Type: string. Description: Job reference Id. Leave empty to cancel all active download jobs.

**Responses:**
- **204**: Successfully Canceled Agent Install.
- **401**: Unauthorized access.
- **403**: Forbidden.

---
### POST /agentsAndPlugins/android/agents/actions/download

**Summary:** Download Android agent(s) to MobiControl.

**Description:** Initiate Android agent(s) download from SOTI's Agent Delivery Service to MobiControl.

Requires the caller to be granted "Manage Android Agents and Plugins" permission.

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `agentInfo` (Required): Type: object. Description: Agent Information.

**Responses:**
- **200**: return the object of download agents status.
- **401**: Unauthorized access.
- **400**: Contract validation failed.
- **403**: Forbidden.

---
### GET /agentsAndPlugins/android/agents/agentCompatibility

**Summary:** Returns compatibility information of an Android agent.

**Description:** Returns compatibility information of an Android agent for given application Id and certificate hash from MobiControl database.
         The details of  application Id and certificate hash to be fetched from "GET /agentsAndPlugins/android/agents".

Requires the caller be granted the "Web Console Access" permission.

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `applicationId` (Required): Type: string. Description: The identifier of the agent.
- `certificateHash` (Required): Type: string. Description: The certificate hash of the agent.

**Responses:**
- **200**: Return the agent compatibility info.
- **401**: Unauthorized access.
- **400**: Contract validation failed.
- **403**: Forbidden.

---

### PUT /agentsAndPlugins/android/agents/agentCompatibility

**Summary:** Updates the specified entry for android agent compatibility.

**Description:** Updates the existing entry for android agent compatibility in MC database. This is the second
         step after install operation on Agent.

Requires the caller to be granted "Manage Android Agents and Plugins" permission.

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `applicationId` (Required): Type: string. Description: The identifier of the agent.
- `certificateHash` (Required): Type: string. Description: The certificate hash of the agent.
- `agentInfo` (Required): Type: object. Description: Agent Information.

**Responses:**
- **200**: Successfully updated agent compatibility and returning the agent info.
- **401**: Unauthorized access.
- **400**: Contract validation failed.
- **403**: Forbidden.

---

### POST /agentsAndPlugins/android/agents/agentCompatibility

**Summary:** Creates an entry for compatible MC server versions with Android agent.

**Description:** Creates the entry for the min and maximum versions of MC server that will be compatible with Android agent downloaded from SOTI Agent Delivery Service.

Requires the caller to be granted "Manage Android Agents and Plugins" permission.

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `agentInfo` (Required): Type: object. Description: Agent Information.

**Responses:**
- **200**: Successfully added agent compatibility and returning the agent info.
- **401**: Unauthorized access.
- **400**: Contract validation failed.
- **403**: Forbidden.

---
### GET /agentsAndPlugins/android/plugins

**Summary:** Returns a list of Android plugins.

**Description:** Returns a list of all Android plugins for a manufacturer, either from SOTI Agent Delivery Service or local cache based on the configuration of the parameter 'forceRefresh'.

Requires the caller be granted the "Web Console Access" permission.

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `status` (Required): Type: string. Description: PlugIn Status.
- `forceRefresh`: Type: boolean. Description: When set to True, always pulls agent information from SOTI Agent Delivery Service, instead of locally cached information.
         <br />When set to False, make use of cached data until it's marked stale in 30mins.

**Responses:**
- **200**: return the list of PlugInInfo objects.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.

---
### POST /agentsAndPlugins/android/plugins/actions/download

**Summary:** Download Android plugin(s) to MobiControl.

**Description:** Initiate Android plugin(s) download from SOTI's Agent Delivery Service to MobiControl.

Requires the caller to be granted "Manage Android Agents and Plugins" permission.

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `pluginInfo` (Required): Type: object. Description: Plugin Information.

**Responses:**
- **200**: return the list of PlugInJob objects.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.

---
### POST /agentsAndPlugins/android/plugins/actions/cancelDownload

**Summary:** Cancel Android plugin(s) download to MobiControl.

**Description:** Cancel Android plugin(s) download from SOTI Agent Delivery Service to MobiControl.

Requires the caller to be granted "Manage Android Agents and Plugins" permission.

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `referenceId`: Type: string. Description: Job reference Id. Leave empty to cancel all active download jobs.

**Responses:**
- **204**: Successfully Canceled Plugins Install.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.

---
## Android Applications Package

### GET /android/enterprise/apps/{referenceId}/{appPackageId}.apk

**Summary:** GetS Android Application Content Apk.

**Parameters:**
- `referenceId` (Required): Type: string. Description: referenceId of an application.
- `appPackageId` (Required): Type: string. Description: appPackageId of an application.

**Responses:**
- **200**:

---
## Android Configuration

### GET /configurations/android/DeploymentType

**Summary:** Returns the deployment type for the Android devices

**Description:** Returns the deployment type setting for the Android devices you want to manage

Requires the caller be granted the "Web Console Access" permission

**(Available Since MobiControl v15.4.0)**

**Responses:**
- **200**: Returns the Allowed Android Type
- **401**: Unauthorized access
- **403**: Forbidden

---

### PUT /configurations/android/DeploymentType

**Summary:** Updates the deployment type for the Android devices

**Description:** Updates the deployment type that fits best the Android devices you want to manage

Requires the caller be granted the "Manage Servers and Global Settings" or "Manage Enrollment Policies" permission

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `request` (Required): Type: object. Description: Define the values in key value format for the deployment type to be used for the android device management. Check Model for details.

**Responses:**
- **200**: Successfully update the deployment type for Android devices
- **400**: Contract validation failed
- **401**: Unauthorized access
- **403**: Forbidden

---
### GET /configurations/android/samsungElmConfiguration

**Summary:** Retrieve the samsung ELM configuration

**Description:** This gets the samsung ELM configuration.

Requires the caller be granted the "Web Console Access" permission

**(Available Since MobiControl v15.4.0)**

**Responses:**
- **200**: Returns the samsung elm configuration
- **401**: Unauthorized access
- **403**: Forbidden

---

### PUT /configurations/android/samsungElmConfiguration

**Summary:** Update the samsung ELM configuration

**Description:** This updates the samsung ELM configuration.

Requires the caller be granted the "Manage Servers and Global Settings" permission

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `request` (Required): Type: object. Description: The samsung elm configuration

**Responses:**
- **204**: Successfully update the samsung elm configuration
- **400**: Contract validation failed
- **401**: Unauthorized access
- **403**: Forbidden

---
### GET /configurations/android/samsungKpeConfiguration

**Summary:** Retrieve the Samsung KPE configuration

**Description:** This gets the Samsung KPE configuration.

Requires the caller be granted the "Web Console Access" permission

ConfigurationType value standard will be On-Cloud. ConfigurationType value Custom will be On-Premise.

**(Available Since MobiControl v15.6.0)**

**Responses:**
- **200**: Returns the Samsung KPE configuration
- **401**: Unauthorized access
- **403**: Forbidden

---

### PUT /configurations/android/samsungKpeConfiguration

**Summary:** Update the Samsung KPE configuration

**Description:** This updates the Samsung KPE configuration.

Requires the caller be granted the "Manage Servers and Global Settings" permission

ConfigurationType value standard will be On-Cloud. ConfigurationType value Custom will be On-Premise.

**(Available Since MobiControl v15.6.0)**

**Parameters:**
- `request` (Required): Type: object. Description: The Samsung KPE configuration

**Responses:**
- **204**: Successfully update the Samsung KPE configuration
- **400**: Contract validation failed
- **401**: Unauthorized access
- **403**: Forbidden

---
### GET /configurations/android/reEnrollment/deviceMatchCriteria

**Summary:** Returns the mechanism to identify an Android device

**Description:** Returns the mechanism to be used by MobiControl to identify an Android device during re-enrollment

Requires the caller be granted the "Web Console Access" permission

**(Available Since MobiControl v15.3.0)**

**Responses:**
- **401**: Unauthorized access
- **403**: Forbidden

---

### PUT /configurations/android/reEnrollment/deviceMatchCriteria

**Summary:** Updates the mechanism to identify an Android device

**Description:** Updates the mechanism to be used by MobiControl to identify an Android device during re-enrollment.
         This API will Accept "DeviceId"="0" or "HardwareId"="1" any of the key or value and perform the respective operation

Requires the caller be granted the "Manage Servers and Global Settings" permission

**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `request` (Required): Type: object. Description: contract to define the mechanism for device identification

**Responses:**
- **204**: Successfully updated device match criteria
- **400**: Contract validation failed
- **401**: Unauthorized access
- **403**: Forbidden

---
## Android Enrollment Configuration Qr Code

### GET /enrollmentConfiguration/android/qRCodes

**Summary:** GetQrCodeConfigurationsSummarySimple method to do the same.

**Parameters:**
- `searchString`: Type: string. Description: Qr code name filter string.
- `order`: Type: string. Description: data Retrieval options.
- `skip`: Type: integer. Description: How many records to skip. Same as index.
- `take`: Type: integer. Description: Record count to take.

**Responses:**
- **200**: Returns {System.Collections.Generic.List`1}where T is {Soti.MobiControl.Android.QrCode.Web.Contracts.AndroidEnrollmentQrCodeConfigurationSummary}
         on success.
- **400**: Contract validation failed.
- **403**: Forbidden.

---

### POST /enrollmentConfiguration/android/qRCodes

**Summary:** API to create new Android Enrollment Qr code configuration.

**Parameters:**
- `request` (Required): Type: object. Description: qr code generator request.

**Responses:**
- **200**: {Soti.MobiControl.Android.QrCode.Web.Contracts.AndroidEnrollmentQrCodeConfiguration} Success.
- **400**: Contract validation failed.
- **403**: Forbidden.

---
### GET /enrollmentConfiguration/android/qRCodes/{referenceId}

**Summary:** GetQrCodeConfigurationSummaryUsingReferenceId method to do the same.

**Parameters:**
- `referenceId` (Required): Type: string. Description: Qr code reference id.

**Responses:**
- **200**: {Soti.MobiControl.Android.QrCode.Web.Contracts.AndroidEnrollmentQrCodeConfiguration} Success.
- **400**: Contract validation failed.
- **403**: Forbidden.

---

### PUT /enrollmentConfiguration/android/qRCodes/{referenceId}

**Summary:** API to update existing QR code configuration.

**Parameters:**
- `referenceId` (Required): Type: string. Description: unique reference id.
- `request` (Required): Type: object. Description: request parameter.

**Responses:**
- **200**: {Soti.MobiControl.Android.QrCode.Web.Contracts.AndroidEnrollmentQrCodeConfiguration}
         Success.
- **400**: Contract validation failed.
- **403**: Forbidden.

---

### DELETE /enrollmentConfiguration/android/qRCodes/{referenceId}

**Summary:** API to delete existing QR code configuration.

**Parameters:**
- `referenceId` (Required): Type: string. Description: unique reference id.

**Responses:**
- **204**: Success.
- **202**: Success but in pipeline.
- **400**: Contract validation failed.
- **403**: Forbidden.

---
### GET /enrollmentConfiguration/android/qRCodes/{referenceId}/svg

**Summary:** API to get svg data for Qr code configuration.

**Parameters:**
- `referenceId` (Required): Type: string. Description: unique reference id.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.

---
### GET /enrollmentConfiguration/android/qRCodes/{referenceId}/logs/summary

**Summary:** API to get the count of information, warning and error logs.

**Parameters:**
- `referenceId` (Required): Type: string. Description: Unique identifier for a QRCode configuration.
- `logSeverities`: Type: array. Description: If specified, returns logs count only for the given log Severities.
- `startDate`: Type: string. Description: If specified, then returns logs count from specified startDate.
- `endDate`: Type: string. Description: If specified, then returns logs count till specified endDate.

**Responses:**
- **200**: {Soti.MobiControl.Android.QrCode.Web.Contracts.AndroidEnrollmentQrCodeConfigLogsCountSummary}
         Success.
- **400**: Contract validation failed.
- **403**: Forbidden.

---
### GET /enrollmentConfiguration/android/qRCodes/{referenceId}/logs

**Summary:** Api to get the list of AndroidEnrollmentConfigurationQrCode logs.

**Parameters:**
- `referenceId` (Required): Type: string. Description: Unique identifier for a QRCode configuration.
- `logSeverities`: Type: array. Description: Log severity.
- `startDate`: Type: string. Description: Start date.
- `endDate`: Type: string. Description: End date.
- `orderByDesc`: Type: boolean. Description: Determines the order. If set to true order is descending.
- `skip`: Type: integer. Description: Determines how many entities to skip.
- `take`: Type: integer. Description: Determines how many entities to take.

**Responses:**
- **200**: Returns {System.Collections.Generic.List`1}where T is {Soti.MobiControl.Android.QrCode.Web.Contracts.AndroidEnrollmentQrCodeConfigLogSummary}
         on success.
- **400**: Contract validation failed.
- **403**: Forbidden.

---
## Android Enrollment Policies

### POST /enrollmentPolicies/android

**Summary:** Creates new Android Enrollment Policy

**Description:** Creates new Android Enrollment Policy



         Requires the caller be granted the "Manage Enrollment Policies" permission.

**(Available Since MobiControl v16.0.0)**


**Parameters:**
- `androidEnrollmentPolicy` (Required): Type: object. Description: Android Enrollment Policy

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.

---
### PUT /enrollmentPolicies/android/{referenceId}

**Summary:** Updates an existing Android Enrollment Policy

**Description:** Updates an existing Android Enrollment Policy



         Requires the caller be granted the "Manage Enrollment Policies" permission.

**(Available Since MobiControl v16.0.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Android Enrollment Policy Reference Id
- `request` (Required): Type: object. Description: Android Enrollment Policy

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.

---

### DELETE /enrollmentPolicies/android/{referenceId}

**Summary:** Deletes an existing Android Enrollment Policy

**Description:** Deletes Android Enrollment Policy



         Requires the caller be granted the "Manage Enrollment Policies" permission.

**(Available Since MobiControl v16.0.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Android Enrollment Policy Reference Id

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.

---

### GET /enrollmentPolicies/android/{referenceId}

**Summary:** Returns the android enrollment policy details.

**Description:** This API returns the details of specified android enrollment policy.



         Requires the caller be granted the 'View Enrollment Policy' permission.

**(Available Since MobiControl v16.0.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Unique identifier for an android enrollment policy.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.

---
### POST /enrollmentPolicies/android/{referenceId}/actions/email

**Summary:** Email Enrollment Policy details

**Description:** This API emails Enrollment Policy Details to the targetted recipient



         Requires the caller be granted the 'Manage Enrollment Policies' permission.

**(Available since MobiControl v15.5.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Unique Identifier for an Enrollment Policy
- `parameter` (Required): Type: object. Description: Parameters required for dispatching email

**Responses:**
- **204**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:<br /><ol><li>6021 - Failed to send email.</li><li>7501 - Unable to send email as enrollment policy is not published.</li></ol>

---
### GET /enrollmentPolicies/android/{referenceId}/actions/downloadConfig

**Summary:** Returns the policy enrollment INI config file.

**Description:** This API returns the INI config file of specified android enrollment policy.



         Requires the caller be granted the 'View Enrollment Policy' permission.

**(Available Since MobiControl v16.0.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Unique identifier for an android enrollment policy.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.

---
### GET /enrollmentPolicies/android/actions/downloadAgent/{manufacturerReferenceId}

**Summary:** Returns Android agent Apk file.

**Description:** This API returns the Android agent Apk file by reference Id.



         Requires the caller be granted the 'View Enrollment Policy' permission.

**(Available Since MobiControl v16.0.0)**


**Parameters:**
- `manufacturerReferenceId` (Required): Type: string. Description: Unique identifier for Android agent apk.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.

---
### PUT /enrollmentPolicies/android/{referenceId}/actions/sync

**Summary:** Publishes or updates Android enrollment policy

**Description:** This API will publishes or update Android enrollment policy profile in Soti Services



         Requires the caller be granted the 'Manage Enrollment Policy' permission.

**(Available Since MobiControl v16.0.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Unique identifier for an android enrollment policy.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.

---
## Android Enterprise Certificates

### GET /androidEnterpriseCertificates/{oem}

**Summary:** Gets Android Enterprise Migration certificate information for an OEM

**Description:** Returns Android Enterprise Migration certificate information for an OEM. A single OEM can have multiple manufacturers e.g. Honeywell OEM can have 'Honeywell, Inc' or intermec or Honeywell. Zebra can have 'Zebra Technologies'. Requires the caller be granted the "Access Web Console" permission.
**(Available Since MobiControl v14.4.2)**

**Parameters:**
- `oem` (Required): Type: string. Description: The Android OEM

**Responses:**
- **200**: Returns a single certificate information of the OEM
- **403**: Unauthorized access

---

### PUT /androidEnterpriseCertificates/{oem}

**Summary:** Uploads Android Enterprise Migration Certificate for an OEM

**Description:** Uploads Android Enterprise Migration Certificate for an OEM. A single OEM can have multiple manufacturers e.g. Honeywell OEM can have 'Honeywell, Inc' or intermec or Honeywell. Zebra can have 'Zebra Technologies'. Requires the caller be granted the "Global Setting" permission.
**(Available Since MobiControl v14.4.2)**

**Parameters:**
- `oem` (Required): Type: string. Description: The Android OEM

**Responses:**
- **204**: File was uploaded successfully
- **400**: Bad request, i.e. invalid file or file content
- **403**: Unauthorized access
- **415**: Unsupported content media type

---
## Android Firmware Upgrade Client

### GET /androidFirmwareUpgrade/clients/{clientType}/actions/sync

**Summary:** Synchronize Android firmware upgrade client.

**Description:** Synchronize Enrollment &amp; FOTA Ready status and target firmware version for target devices.

Requires the caller to be granted Web Console Access permission.

**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `clientType` (Required): Type: string. Description: Android Firmware Upgrade Client Type.

**Responses:**
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>3716 - Android Firmware Upgrade Zebra Synchronization is In-Progress State.</li></ol>

---
### GET /androidFirmwareUpgrade/clients/zebra/actions/syncStatus

**Summary:** Retrieve Android firmware upgrade zebra synchronization status.

**Description:** Returns the status of Android firmware upgrade synchronization process.

Requires the caller to be granted Web Console Access permission.

**(Available Since MobiControl v15.3.0)**

**Responses:**
- **200**: Returns zebra android firmware upgrade synchronization status.
- **401**: Unauthorized access.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>3717 - Android Firmware Upgrade Zebra Synchronization Process is not initiated.</li></ol>

---
### GET /androidFirmwareUpgrade/clients/zebra/authorizationGrant

**Summary:** Retrieve Android firmware upgrade Zebra authorization grant.

**Description:** Retrieve authorization grant from Zebra to generate access token required for firmware upgrade.

Requires the caller to be granted Web Console Access permission.

**(Available Since MobiControl v15.3.0)**

**Responses:**
- **200**: Returns Zebra Android firmware upgrade authorization grant.
- **401**: Unauthorized access.

---
### GET /androidFirmwareUpgrade/clients/{clientType}/status

**Summary:** Retrieve Android firmware upgrade client status.

**Description:** Retrieve OEM's Android firmware upgrade client registration status.

Requires the caller to be granted Web Console Access permission.

**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `clientType` (Required): Type: string. Description: Android Firmware Upgrade Client Type.

**Responses:**
- **200**: Returns android firmware upgrade client response.
- **401**: Unauthorized access.

---
### GET /androidFirmwareUpgrade/zebra/availableFirmwareVersions

**Summary:** Retrieve Android firmware versions zebra.

**Description:** Retrieve available target firmware versions for a Zebra device.

Requires the caller to be granted Web Console Access permission.

**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `model` (Required): Type: string. Description:
- `currentFirmwareVersion` (Required): Type: string. Description:

**Responses:**
- **200**: Android Firmware Versions.

---
### PUT /androidFirmwareUpgrade/clients/{clientType}/reset

**Summary:** Reset Account.

**Description:** Reset account for our OEM partner.

Requires the caller to be granted Web Console Access permission.

**(Available Since MobiControl v2024.0.0)**

**Parameters:**
- `clientType` (Required): Type: string. Description: Android Firmware Upgrade Client Type.

**Responses:**
- **200**: Successful.
- **401**: Unauthorized access.
- **403**: Security Exception.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>3721 - Android Firmware Upgrade Zebra Reset Account is In-Progress.</li></ol>

---
## Apns Configuration

### GET /apple/apns/configurations

**Summary:** Returns a list of all available APNS configurations

**Description:**
Requires the caller to be granted the "MobiControl Access" permission.

**(Available Since MobiControl v15.3.0)**

**Responses:**
- **200**: All APNS configurations
- **401**: Unauthorized attempt to execute the method

---

### POST /apple/apns/configurations

**Summary:** Creates a new Apple Push Notification Service configuration

**Description:**
Requires the caller to be granted the "Manage APNS Certificates" permission.

**(Available Since MobiControl v15.3.0)**

The request's headers must have: <code>Content-Type: multipart/related;boundary=mobicontrol_boundary</code>

         Boundary length must be set to less than or equal to 11 to prevent internal server errors.



The request's body:
         - Should be multipart request comprising of metadata and certificate content encoded in base64.- Supported values of Content-Type for certificate part of request's body: application/x-pem-file, application/x-pkcs12.- The appropriate content-type value should be chosen in accordance with the certificate type being uploaded.- Metadata part of request's body contains a JSON object with optional AppleId and CertificatePassword fields and should be identified by <code>Content-Type: application/x-pkcs12.metadata+json (or application/x-pem-file.metadata+json)</code>

Sample request's body:


         --mobicontrol_boundary
         Content-Type: application/x-pkcs12.metadata+json


         {"CertificatePassword":"password", "AppleId":"some@id.com"}


         --mobicontrol_boundary
            Content-Type: application/x-pkcs12
            Content-Transfer-Encoding: base64
            Content-Disposition: attachment; filename="cert.pfx"


         BASE64_ENCODED_CERTIFICATE_CONTENT_HERE
         --mobicontrol_boundary--
         ```



**Responses:**
- **400**: Bad request.<br /><ol><li>If the request's header's content type is incorrect or malformed</li><li>If the request's body is missing a certificate</li><li>If the request's body is missing a certificate password (for the case of pfx files)</li><li>If the request's body contains a certificate password that exceeds 512 characters</li><li>If the request's body contains a an Apple ID that exceeds 256 characters</li></ol>
- **401**: Unauthorized attempt to execute the method
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:<br /><ol><li>5800 - If the request's body contains an invalid certificate file type.</li><li>5801 - If the request's body contains a certificate with an invalid topic string</li><li>5802 - If the request's body contains a certificate that was not generated using a downloaded CSR</li><li>5803 - If the request's body contains an invalid password for the provided certificate</li><li>5805 - If MobiControl cannot establish a connection with APNS to determine whether the certificate is valid</li><li>5806 - If Apple rejects the connection to an invalid certificate</li><li>5807 - If there already exists an APNS configuration</li><li>5808 - If APNS certificate is expired.</li></ol>
- **200**: Created configuration object.

---
### GET /apple/apns/configurations/{referenceId}

**Summary:** Returns the specified APNS configuration as referenced by {referenceId}

**Description:**
Requires the caller to be granted the "MobiControl Access" permission.

**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Configuration reference ID in Microsoft GUID format.

**Responses:**
- **400**: Bad request
- **401**: Unauthorized attempt to execute the method
- **403**: Failed operation due to non-existing configuration record
- **200**: Configuration object.

---

### PUT /apple/apns/configurations/{referenceId}

**Summary:** Updates the specified APNS configuration

**Description:**
Requires the caller to be granted the "Manage APNS Certificates" permission.

**(Available Since MobiControl v15.3.0)**

The request's headers must have: <code>Content-Type: multipart/related;boundary=mobicontrol_boundary</code>

         Boundary length must be set to less than or equal to 11 to prevent internal server errors.



The request's body:
         - Should be multipart request comprising of metadata and certificate content encoded in base64.- Supported values of Content-Type for certificate part of request's body: application/x-pem-file, application/x-pkcs12.- The appropriate content-type value should be chosen in accordance with the certificate type being uploaded.- Metadata part of request's body contains a JSON object with optional AppleId and CertificatePassword fields and should be identified by <code>Content-Type: application/x-pkcs12.metadata+json (or application/x-pem-file.metadata+json)</code>- To update AppleId only (without certificate content) the request's body should have <code>Content-Transfer-Encoding: binary</code>

Sample request's body:


         --mobicontrol_boundary
         Content-Type: application/x-pkcs12.metadata+json


         {"AppleId":"sample123"}


         --mobicontrol_boundary
            Content-Type: application/x-pkcs12
            Content-Transfer-Encoding: binary
            Content-Disposition: attachment; filename="empty.pfx"



         --mobicontrol_boundary--
         ```



**Parameters:**
- `referenceId` (Required): Type: string. Description: Configuration reference ID in Microsoft GUID format.
- `allowTopicChange` (Required): Type: boolean. Description: If it is 'true', the new APNS certificate's topic string can be different than that of the existing APNS certificate <br />
         If it is 'false', the new APNS certificate's topic string must match that of the existing APNS certificate <br />

**Responses:**
- **400**: Bad request.<br /><ol><li>If the request is missing the reference ID</li><li>If the request's header's content type is incorrect or malformed</li><li>If the request's body is missing a certificate</li><li>If the request's body is missing a certificate password (for the case of pfx files)</li><li>If the request's body contains a certificate password that exceeds 512 characters</li><li>If the request's body contains a an Apple ID that exceeds 256 characters</li></ol>
- **401**: Unauthorized attempt to execute the method
- **403**: Failed operation due to non-existing configuration record
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:<br /><ol><li>5800 - If the request's body contains an invalid certificate file type.</li><li>5801 - If the request's body contains a certificate with an invalid topic string</li><li>5802 - If the request's body contains a certificate that was not generated using a downloaded CSR</li><li>5803 - If the request's body contains an invalid password for the provided certificate</li><li>5804 - If topic string of the new APNS certificate does not match that of the existing APNS certificate</li><li>5805 - If MobiControl cannot establish a connection with APNS to determine whether the certificate is valid</li><li>5806 - If Apple rejects the connection to an invalid certificate</li><li>5808 - If APNS certificate is expired.</li></ol>
- **200**: Updated configuration object.

---
### PUT /apple/apns/configurations/{referenceId}/appleId

**Summary:** Updates the specified Apple ID for the specified APNS configuration

**Description:**
Requires the caller to be granted the "Manage APNS Certificates" permission.

**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Configuration reference ID in Microsoft GUID format.
- `updateRequest` (Required): Type: object. Description: Update APNS configuration in MobiControl.

**Responses:**
- **204**:
- **400**: Bad request.<br /><ol><li>If the request is missing the reference ID</li><li>If the request's body is missing an Apple ID</li><li>If the request's body contains a an Apple ID that exceeds 256 characters</li></ol>
- **401**: Unauthorized attempt to execute the method
- **403**: Failed operation due to non-existing configuration record

---
### GET /apple/apns/certificateSigningRequests

**Summary:** Returns a Certificate Signing Request (CSR).

**Description:**
Requires the caller to be granted the "Manage APNS Certificates" permission.

**(Available Since MobiControl v15.3.0)**

**Responses:**
- **200**: Base64 encoded CSR content
- **401**: Unauthorized attempt to execute the method

---
### POST /apple/apns/configurations/{referenceId}/actions/testConnection

**Summary:** Executes a test connection with APNS

**Description:**
Requires the caller to be granted the "Manage APNS Certificates" permission.

**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Configuration reference ID in Microsoft GUID format.

**Responses:**
- **401**: Unauthorized attempt to execute the method
- **204**: Operation Successful
- **422**: Violated logical condition.The following ErrorCode values can be returned:<br /><ol><li>5805 - If MobiControl cannot establish a connection with APNS to determine whether the certificate is valid</li><li>5806 - If Apple rejects the connection to an invalid certificate</li><li>5808 - If APNS certificate is expired.</li></ol>
- **403**: Failed operation due to non-existing configuration record

---
## App Management Android Apps

### GET /appManagement/android/apps/enterprise/{referenceId}

**Summary:** Returns Android application details.

**Description:** Returns Android Enterprise application details.



          Requires the caller be granted the "View App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Application Reference Id.

**Responses:**
- **200**: OK.
- **400**: Contract validation failed.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>1 - Reference Id is either null, empty or consists only of white space.</li><li>2 - The given reference Id is not in valid format.</li><li>5501 - Application with the given reference Id is not found in the inventory.</li></ol>

---

### DELETE /appManagement/android/apps/enterprise/{referenceId}

**Summary:** Deletes Enterprise Android application.

**Description:** Deletes Enterprise Android application.



          Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Application Reference ID.

**Responses:**
- **200**: OK.
- **400**: Contract validation failed.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>1 - Reference Id is either null, empty or consists only of white space.</li><li>2 - The given reference Id is not in valid format.</li><li>4 - Inventory customer application Id is out of range.</li><li>5501 - Application with the given reference Id is not found in the inventory.</li><li>5509 - The application is associated with these app policy(s): {0}. Delete the app policies before deleting the application.</li></ol>

---

### PUT /appManagement/android/apps/enterprise/{referenceId}

**Summary:** Updates Enterprise Android application.

**Description:** Updates Enterprise Android application details.



          Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**

Content-Type of the Request body must be <code>application/json</code>



**Parameters:**
- `referenceId` (Required): Type: string. Description: Application reference Id.
- `updateCustomerApplicationRequest` (Required): Type: object. Description: Enterprise Application details.

**Responses:**
- **200**: OK.
- **400**: Contract validation failed.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>1 - Reference Id is either null, empty or consists only of white space.</li><li>1 - Customer application request is null.</li><li>1 - Inventory customer application is null.</li><li>1 - Inventory customer application's name is null.</li><li>1 - Android customer application inventory data is null.</li><li>2 - The given reference Id is not in valid format.</li><li>4 - Inventory customer application Id is out of range.</li><li>5501 - Application with the given reference Id is not found in the inventory.</li></ol>

---
### POST /appManagement/android/apps/enterprise/internal

**Summary:** Creates an internal Android application.

**Description:** Creates new enterprise Android application hosted internally by MobiControl.



          Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**

Content-Type of the Request body must be <code>multipart/related; boundary={boundary identifier}</code>

          Boundary length must be set to less than or equal to 11 to prevent internal server errors.


          Multipart request body must contain the following parts:
- application file - Contains application file with Content-Type:
application/vnd.android.application OR```

application/vnd.android.package-archive```


          Mandatory headers

          Content-Disposition: attachment; filename="{application-filename}"


          Optional headers

          Content-Type-Encoding: binary

          The maximum size of the Android enterprise application file to be uploaded when using this endpoint is <u>2 GB</u>.


          The example below shows an application upload request.



          Content-Type: multipart/related; boundary=foo_bar_baz
          Content-Length: number_of_bytes_in_entire_request_body


          --foo_bar_baz
          Content-Type: application/vnd.android.application


          Content-Disposition: attachment; filename="application_name.apk"


          application data
          --foo_bar_baz--
          ```


**Parameters:**
- `failIfApplicationAlreadyExists`: Type: boolean. Description:
- `extractConfigurationSchema`: Type: boolean. Description:

**Responses:**
- **200**: OK.
- **400**: Contract validation failed.
- **401**: Unauthorized.
- **403**: Forbidden.
- **415**: Unsupported media type.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>1 - Reference Id is either null, empty or consists only of white space.</li><li>1 - Cannot create temporary file of the apk because the stream is null.</li><li>1 - The path of temporary created file is either null, empty or consists of only white space.</li><li>1 - The application package Id is either null, empty or consists of only white space.</li><li>1 - Android customer application inventory data is null.</li><li>1 - Application icon path is either null, empty or consists of white space.</li><li>1 - ApkMetaData is null.</li><li>1 - Android customer application inventory data is null.</li><li>2 - The given reference Id is not in valid format.</li><li>2 - Application Url must have a value for external applications.</li><li>2 - File path must be empty for external applications.</li><li>2 - File path must have a value for internal applications.</li><li>2 - Application url must be empty for internal applications.</li><li>4 - Inventory customer application Id is out of range.</li><li>5501 - Application with the given reference Id is not found in the inventory.</li><li>5500 - The given android apk is invalid.</li><li>5506 - A customer application with the given application name and application package Id already exists in the inventory.</li><li>5508 - Unsupported customer application icon format.</li></ol>

---
### POST /appManagement/android/apps/enterprise/external

**Summary:** Creates an external Android application.

**Description:** Creates new enterprise Android application hosted externally.



          Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**

Content-Type of the Request body must be <code>application/json</code>



**Parameters:**
- `addExternalCustomerApplicationRequest` (Required): Type: object. Description: External Application URL.
- `failIfApplicationAlreadyExists`: Type: boolean. Description: Check for existing application.
- `extractConfigurationSchema`: Type: boolean. Description: Extract configuration schema.

**Responses:**
- **200**: OK.
- **400**: Contract validation failed.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>1 - Reference Id is either null, empty or consists only of white space.</li><li>1 - External customer application request is either null, empty or consists only of white space.</li><li>1 - Applicaiton url in external customer application request is either null, empty or consists only of white space.</li><li>1 - The file path of downloaded apk file is either null, empty or consists of only white space.</li><li>1 - The application package Id is either null, empty or consists of only white space.</li><li>1 - Android customer application inventory data is null.</li><li>1 - Application icon path is either null, empty or consists of white space.</li><li>2 - The given reference Id is not in valid format.</li><li>2 - Application Url must have a value for external applications.</li><li>2 - File path must be empty for external applications.</li><li>2 - File path must have a value for internal applications.</li><li>2 - Application url must be empty for internal applications.</li><li>4 - Inventory customer application Id is out of range.</li><li>5501 - Application with the given reference Id is not found in the inventory.</li><li>5505 - Application url mentioned in the external customer application request is not accessible.</li><li>5506 - A customer application with the given application name and application package Id already exists in the inventory.</li><li>5508 - Unspported customer application icon format.</li><li>5500 - The given android apk is invalid.</li></ol>

---
### GET /appManagement/android/apps/googlePlayStore/{appPackageId}

**Summary:** Returns Google Play Store application details.

**Description:** Returns Android application details for a Google Play Store app.



          Requires the caller be granted the "View App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `appPackageId` (Required): Type: string. Description: Application package ID.

**Responses:**
- **200**: OK.
- **400**: Contract validation failed.
- **401**: Unauthorized.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>1 - Application package Id is either null, empty or consists only of white space.</li><li>5501 - Application with the given application package Id is not found in the inventory.</li></ol>

---

### PUT /appManagement/android/apps/googlePlayStore/{appPackageId}

**Summary:** Updates Google Play Store application details.

**Description:** Updates Android application details for a Google Play Store app.



          Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `appPackageId` (Required): Type: string. Description: Application package ID.

**Responses:**
- **200**: OK.
- **400**: Contract validation failed.
- **401**: Unauthorized.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>1 - Application package Id is either null, empty or consists only of white space.</li><li>1 - Google play store application is null.</li><li>1 - Language is null.</li><li>5501 - Application with the given application package Id is not found in the inventory.</li><li>5503 - Application with the given application package Id is not found on google play store.</li></ol>

---
### GET /appManagement/android/apps/googlePlayStore/{appPackageId}/appFeedback/summary

**Summary:** Returns summary of application feedback.

**Description:** Returns summary for application feedback by severity



         Requires the caller be granted the "View App Policies" permission.

**(Available Since MobiControl v15.3.0)
Deprecated use GET googlePlayStore/{appPackageId}/appFeedbackGroups/summary instead.**


**Parameters:**
- `appPackageId` (Required): Type: string. Description: Application package ID.
- `ruleReferenceId` (Required): Type: string. Description: Rule reference ID.
- `startDate`: Type: string. Description: The start date.
- `endDate`: Type: string. Description: The end dat.

**Responses:**
- **200**: OK.
         {System.Collections.Generic.IEnumerable`1} where T is {Soti.MobiControl.AppPolicy.Android.Web.ApplicationFeedback.ApplicationFeedbackSeverityCount}.
- **400**: Contract validation failed.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br />

---
### GET /appManagement/android/apps/offlineOEMConfig/{appPackageId}/appFeedback/summary

**Summary:** Returns summary of Offline OEM Config application feedback.

**Description:**

**(Available Since MobiControl v15.5.0)
Deprecated use GET offlineOEMConfig/{appPackageId}/appFeedbackGroups/summary instead.**


         Returns summary for Offline OEM Config application feedback by severity


         Requires the caller be granted the "View App Policies" permission.



**Parameters:**
- `appPackageId` (Required): Type: string. Description:
- `ruleReferenceId` (Required): Type: string. Description:
- `startDate`: Type: string. Description:
- `endDate`: Type: string. Description:

**Responses:**
- **200**: OK.
         {System.Collections.Generic.IEnumerable`1} where T is {Soti.MobiControl.AppPolicy.Android.Web.ApplicationFeedback.ApplicationFeedbackSeverityCount}.
- **400**: Contract validation failed.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br />

---
### GET /appManagement/android/apps/enterprise/{referenceId}/icon

**Summary:** Gets customer's application icon.

**Description:** Returns the application icon for an enterprise application with the given ReferenceId.



          Requires the caller be granted the "View App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Application Reference ID.

**Responses:**
- **200**: OK.
- **400**: Contract validation failed.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>1 - Reference Id is either null, empty or consists only of white space.</li><li>2 - The given reference Id is not in valid format.</li><li>4 - Inventory customer application Id is out of range.</li><li>5501 - Application with the given reference Id is not found in the inventory.</li><li>5507 - Application icon for the given customer application reference Id does not exists in the inventory.</li></ol>

---
### GET /appManagement/android/apps/googlePlayStore/{appPackageId}/appFeedback

**Summary:** Returns application feedback reported by AE devices.

**Description:** Returns application feedback reported by AE devices to Google Cloud.



         Requires the caller be granted the "View App Policies" permission.

**(Available Since MobiControl v15.3.0)
Deprecated use GET googlePlayStore/{appPackageId}/appFeedbackGroups instead.**


**Parameters:**
- `appPackageId` (Required): Type: string. Description: Application Package ID.
- `ruleReferenceId` (Required): Type: string. Description: Rule Reference ID.
- `startDate`: Type: string. Description: The start date.
- `endDate`: Type: string. Description: The end date.
- `severity`: Type: string. Description: Severity of applicaiton feedback event.
- `Skip`: Type: integer.
- `Take`: Type: integer.

**Responses:**
- **200**: OK.
         {System.Collections.Generic.IEnumerable`1} where T is {Soti.MobiControl.AppPolicy.Android.Web.ApplicationFeedback.ApplicationFeedback}.
- **400**: Contract validation failed.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br />

---
### GET /appManagement/android/apps/offlineOEMConfig/{appPackageId}/appFeedback

**Summary:** Returns Offline OEM Config application feedback reported by AE devices.

**Description:**

**(Available Since MobiControl v15.5.0)
Deprecated use GET offlineOEMConfig/{appPackageId}/appFeedbackGroups instead.**


         Returns Offline OEM Config application feedback reported by AE devices.


         Requires the caller be granted the "View App Policies" permission.



**Parameters:**
- `appPackageId` (Required): Type: string. Description:
- `ruleReferenceId` (Required): Type: string. Description:
- `startDate`: Type: string. Description:
- `endDate`: Type: string. Description:
- `severity`: Type: string. Description:
- `Skip`: Type: integer.
- `Take`: Type: integer.

**Responses:**
- **200**: OK
         {System.Collections.Generic.IEnumerable`1} where T is {Soti.MobiControl.AppPolicy.Android.Web.ApplicationFeedback.ApplicationFeedback}.
- **400**: Contract validation failed.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br />

---
### GET /appManagement/android/apps/googlePlayStore/{appPackageId}/appFeedbackGroups

**Summary:** Returns application feedback groups reported by AE devices.

**Description:** Returns application feedback groups reported by AE devices to Google Cloud.



         Requires the caller be granted the "View App Policies" permission.

**(Available Since MobiControl v15.6.1)**


**Parameters:**
- `appPackageId` (Required): Type: string. Description: Application Package ID.
- `ruleReferenceId` (Required): Type: string. Description: Rule Reference ID.
- `timeRange` (Required): Type: string. Description: Time Range.
- `startDate`: Type: string. Description: The start date.
- `endDate`: Type: string. Description: The end date.
- `severity`: Type: string. Description: Severity of applicaiton feedback event.
- `Skip`: Type: integer.
- `Take`: Type: integer.

**Responses:**
- **200**: OK.
         {System.Collections.Generic.IEnumerable`1} where T is {Soti.MobiControl.AppPolicy.Android.Web.ApplicationFeedback.ApplicationFeedbackGroup}.
- **400**: Contract validation failed.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br />

---
### GET /appManagement/android/apps/googlePlayStore/{appPackageId}/appFeedbackGroups/summary

**Summary:** Returns summary of application feedback groups.

**Description:** Returns summary for application feedback groups by severity



         Requires the caller be granted the "View App Policies" permission.

**(Available Since MobiControl v15.6.1)**


**Parameters:**
- `appPackageId` (Required): Type: string. Description: Application package ID.
- `ruleReferenceId` (Required): Type: string. Description: Rule reference ID.
- `timeRange` (Required): Type: string. Description: Time Range.
- `startDate`: Type: string. Description: The start date.
- `endDate`: Type: string. Description: The end dat.

**Responses:**
- **200**: OK.
         {System.Collections.Generic.IEnumerable`1} where T is {Soti.MobiControl.AppPolicy.Android.Web.ApplicationFeedback.ApplicationFeedbackSeverityCount}.
- **400**: Contract validation failed.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br />

---
### GET /appManagement/android/apps/googlePlayStore/{appPackageId}/appFeedbackDetails

**Summary:** Returns application feedback groups reported by AE devices.

**Description:** Returns application feedback groups reported by AE devices to Google Cloud.



         Requires the caller be granted the "View App Policies" permission.

**(Available Since MobiControl v15.6.1)**


**Parameters:**
- `appPackageId` (Required): Type: string. Description: Application Package ID.
- `ruleReferenceId` (Required): Type: string. Description: Rule Reference ID.
- `timeRange` (Required): Type: string. Description: Time Range.
- `timestampStart` (Required): Type: string. Description: The Time Range start date.
- `timestampEnd` (Required): Type: string. Description: The Time Range end date.
- `key` (Required): Type: string. Description: key.
- `message` (Required): Type: string. Description: message.
- `severity` (Required): Type: string. Description: Severity of applicaiton feedback event.
- `startDate`: Type: string. Description: The start date.
- `endDate`: Type: string. Description: The end date.
- `Skip`: Type: integer.
- `Take`: Type: integer.

**Responses:**
- **200**: OK.
         {System.Collections.Generic.IEnumerable`1} where T is {Soti.MobiControl.AppPolicy.Android.Web.ApplicationFeedback.ApplicationFeedback}.
- **400**: Contract validation failed.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br />

---
### GET /appManagement/android/apps/offlineOEMConfig/{appPackageId}/appFeedbackGroups

**Summary:** Returns Offline OEM Config application feedback groups reported by AE devices.

**Description:**

**(Available Since MobiControl v15.6.1)**


         Returns Offline OEM Config application feedback groups reported by AE devices.


         Requires the caller be granted the "View App Policies" permission.



**Parameters:**
- `appPackageId` (Required): Type: string. Description:
- `ruleReferenceId` (Required): Type: string. Description:
- `timeRange` (Required): Type: string. Description:
- `startDate`: Type: string. Description:
- `endDate`: Type: string. Description:
- `severity`: Type: string. Description:
- `Skip`: Type: integer.
- `Take`: Type: integer.

**Responses:**
- **200**: OK.
         {System.Collections.Generic.IEnumerable`1} where T is {Soti.MobiControl.AppPolicy.Android.Web.ApplicationFeedback.ApplicationFeedbackGroup}.
- **400**: Contract validation failed.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br />

---
### GET /appManagement/android/apps/offlineOEMConfig/{appPackageId}/appFeedbackGroups/summary

**Summary:** Returns summary of Offline OEM Config application feedback by severity.

**Description:**

**(Available Since MobiControl v15.6.1)**


         Returns summary for Offline OEM Config application feedback by severity


         Requires the caller be granted the "View App Policies" permission.



**Parameters:**
- `appPackageId` (Required): Type: string. Description:
- `ruleReferenceId` (Required): Type: string. Description:
- `timeRange` (Required): Type: string. Description:
- `startDate`: Type: string. Description:
- `endDate`: Type: string. Description:

**Responses:**
- **200**: OK.
         {System.Collections.Generic.IEnumerable`1} where T is {Soti.MobiControl.AppPolicy.Android.Web.ApplicationFeedback.ApplicationFeedbackSeverityCount}.
- **400**: Contract validation failed.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br />

---
### GET /appManagement/android/apps/offlineOEMConfig/{appPackageId}/appFeedbackDetails

**Summary:** Returns Offline OEM Config application feedback reported by AE devices.

**Description:**

**(Available Since MobiControl v15.6.1)**


         Returns Offline OEM Config application feedback reported by AE devices.


         Requires the caller be granted the "View App Policies" permission.



**Parameters:**
- `appPackageId` (Required): Type: string. Description: Application Package ID.
- `ruleReferenceId` (Required): Type: string. Description: Rule Reference ID.
- `timeRange` (Required): Type: string. Description: Time Range.
- `timestampStart` (Required): Type: string. Description: The Time Range start date.
- `timestampEnd` (Required): Type: string. Description: The Time Range end date.
- `key` (Required): Type: string. Description: key.
- `message` (Required): Type: string. Description: message.
- `severity` (Required): Type: string. Description: Severity of application feedback event.
- `startDate`: Type: string. Description: The start date.
- `endDate`: Type: string. Description: The end date.
- `Skip`: Type: integer.
- `Take`: Type: integer.

**Responses:**
- **200**: OK
         {System.Collections.Generic.IEnumerable`1} where T is {Soti.MobiControl.AppPolicy.Android.Web.ApplicationFeedback.ApplicationFeedback}.
- **400**: Contract validation failed.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br />

---
## App Management Android Policies

### GET /appManagement/android/policies/{referenceId}

**Summary:** Returns Android app management policy details.

**Description:** Returns Android app management policy details.



          Requires the caller be granted the "View App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Policy reference ID.

**Responses:**
- **200**: OK.
- **400**: Contract validation failed.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>1 - Reference Id is either null, empty or consists only of white space.</li><li>2 - The given reference Id is not in valid format</li><li>4 - The app policy Id for the given reference Id is out of range.</li></ol>

---

### DELETE /appManagement/android/policies/{referenceId}

**Summary:** Deletes an Android app management policy.

**Description:** Deletes an Android app management policy.



          Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Policy reference ID.

**Responses:**
- **200**: OK.
- **400**: Contract validation failed.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>1 - Reference Id is either null, empty or consists only of white space.</li><li>2 - The given reference Id is not in valid format</li></ol>

---

### PUT /appManagement/android/policies/{referenceId}

**Summary:** Updates an Android app management policy.

**Description:** Updates an Android app management policy.



          Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Policy reference ID.
- `rule` (Required): Type: object. Description: Update Android App Policy request.

**Responses:**
- **200**: OK.
- **400**: Contract validation failed.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>1 - App policy for given reference Id does not exists or is null.</li><li>1 - Reference Id is either null, empty or consists only of white space.</li><li>1 - App policy name param of the given app policy is null, empty or consists of white space.</li><li>2 - The given reference Id is not in valid format</li><li>4 - The app policy Id for the given reference Id is out of range.</li><li>5000 - Application catalog app policy name already exists.</li></ol>

---
### POST /appManagement/android/policies

**Summary:** Creates new Android app management policy.

**Description:** Creates a new Android app management policy.



          Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `rule` (Required): Type: object. Description: Android App Policy details.

**Responses:**
- **200**: OK.
- **400**: Contract validation failed.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>1 - App policy is null.</li><li>1 - App policy Id is null.</li><li>1 - App policy name param of the given app policy is null, empty or consists of white space.</li><li>1 - Missing enterprise reference Id in the given android application catalog app policy request.</li><li>2 - The given app policy kind does not exists.</li><li>2 - The app policy family does not exists.</li><li>5000 - Application catalog app policy name already exists.</li></ol>

---
### PUT /appManagement/android/policies/{referenceId}/enterpriseReferenceId

**Summary:** Updates an Android app management policy.

**Description:** Updates an Android app management policy.



          Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Policy reference ID.
- `rule` (Required): Type: object. Description: Update Android Enterprise App Policy request.

**Responses:**
- **200**: OK.
- **400**: Contract validation failed.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>1 - App policy for given reference Id does not exists or is null.</li><li>1 - App policy Id does not exists or is null.</li><li>1 - Reference Id is either null, empty or consists only of white space.</li><li>1 - App policy name param of the given app policy is null, empty or consists of white space.</li><li>2 - The given reference Id is not in valid format</li><li>4 - The app policy Id for the given reference Id is out of range.</li></ol>

---
### GET /appManagement/android/policies/{referenceId}/apps/enterprise

**Summary:** Returns Android apps for the selected policy.

**Description:** Returns a list of applications for the selected Android app management policy.



          Requires the caller be granted the "View App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Policy Reference ID.

**Responses:**
- **200**: OK
          {System.Collections.Generic.IEnumerable`1} where T is {Soti.MobiControl.AppPolicy.Android.Web.Rules.CustomerAppCatalogRuleItemAppInventory}
          Collection of CustomerAppCatalogRuleItemAppInventory that holds information about the customer applications that are associated to a certain Android application catalog rule.
          <seealso cref="T:Soti.MobiControl.AppPolicy.Android.Web.Rules.CustomerAppCatalogRuleItemAppInventory" />
- **400**: Contract validation failed.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>1 - Reference Id is either null, empty or consists only of white space.</li><li>2 - The given reference Id is not in valid format</li><li>4 - The app policy Id for the given reference Id is out of range.</li></ol>

---

### PUT /appManagement/android/policies/{referenceId}/apps/enterprise

**Summary:** Updates Android applications for the selected policy.

**Description:** Updates Android applications for the selected app management policy.



          Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Policy Reference ID.
- `applications` (Required): Type: object. Description: {System.Collections.Generic.IEnumerable`1} where T is {Soti.MobiControl.AppPolicy.Android.Web.Rules.CustomerAppCatalogRuleItem}Collection of Android Enterprise Applications.

**Responses:**
- **200**: OK.
- **400**: Contract validation failed.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>1 - Reference Id is either null, empty or consists only of white space.</li><li>1 - The customer app management policy item list is null.</li><li>1 - App policy for given referenceId is null.</li><li>2 - The given reference Id is not in valid format</li><li>4 - The app policy Id for the given reference Id is out of range.</li><li>5502 - The application list is empty or null. It should contain at least one application.</li></ol>

---
### GET /appManagement/android/policies/apps/{appPackageId}/Configuration

**Summary:** Returns available App Configuration for given App Package Id.

**Description:** Returns available App Configuration for given App Package Id.


         Requires the caller be granted the "View App Policies" permission.


**(Available Since MobiControl v15.5.0)**


**Parameters:**
- `appPackageId` (Required): Type: string. Description: Application Package Id.

**Responses:**
- **200**: OK.
- **400**: App Package Id is either null, empty or consists only of white space.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>1 -5510 - Application with the given application package Id is not found in the inventory.</li></ol>

---
### POST /appManagement/android/policies/apps/{referenceId}/actions/ExtractCustomerAppConfiguration

**Summary:** Updates App Configuration Schema for a given Application.

**Description:** Updates App Configuration Schema for a given Application.


          Requires the caller be granted the "Manage App Policies" permission.


**(Available Since MobiControl v15.5.1)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Application reference Id.

**Responses:**
- **200**: OK.
- **400**: Contract validation failed.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>1 - Reference Id is either null, empty or consists only of white space.</li><li>1 - Cannot create temporary file of the apk because the stream is null.</li><li>1 - The path of temporary created file is either null, empty or consists of only white space.</li><li>1 - The application package Id is either null, empty or consists of only white space.</li><li>1 - Android customer application inventory data is null.</li><li>1 - Application icon path is either null, empty or consists of white space.</li><li>1 - ApkMetaData is null.</li><li>1 - Android customer application inventory data is null.</li><li>2 - File path must have a value for internal applications.</li><li>2 - Application url must be empty for internal applications.</li><li>4 - Inventory customer application Id is out of range.</li><li>5501 - Application with the given reference Id is not found in the inventory.</li><li>5506 - A customer application with the given application name and application package Id already exists in the inventory.</li><li>5508 - Unsupported customer application icon format.</li></ol>

---
### GET /appManagement/android/policies/{referenceId}/apps/googlePlayStore

**Summary:** Returns Google Play store apps for the selected policy.

**Description:** Returns Google Play store applications for the selected Android  app management policy.



          Requires the caller be granted the "View App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Policy reference ID.

**Responses:**
- **200**: OK.
          {System.Collections.Generic.IEnumerable`1} where T is {Soti.MobiControl.AppPolicy.Android.Web.Rules.GooglePlayStoreAppCatalogRuleItemAppInventory}.
- **400**: Contract validation failed.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>1 - Reference Id is either null, empty or consists only of white space.</li><li>2 - The given reference Id is not in valid format</li><li>4 - The app policy Id for the given reference Id is out of range.</li></ol>

---

### PUT /appManagement/android/policies/{referenceId}/apps/googlePlayStore

**Summary:** Updates Google Play store applications for the selected policy.

**Description:** Updates Google Play store applications for the selected Android app management policy.



          Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Policy reference ID.
- `applications` (Required): Type: object. Description: Collection of Google PlayStore Applications.

**Responses:**
- **200**: OK.
- **400**: Contract validation failed.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>1 - Reference Id is either null, empty or consists only of white space.</li><li>1 - The google play store app management policy item list is null.</li><li>2 - The given reference Id is not in valid format</li><li>4 - The app policy Id for the given reference Id is out of range.</li><li>5502 - The application list is empty or null. It should contain at least one application.</li><li>5504 - One of the given application is not approved for enterprise.</li></ol>

---
## App Management Apple Policies

### GET /appManagement/apple/common/policies/{referenceId}

**Summary:** Returns Apple app management policy details.

**Description:** Returns Apple app management policy details



         Requires the caller be granted the "View App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Policy reference ID.

**Responses:**
- **200**: OK.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.

---

### PUT /appManagement/apple/common/policies/{referenceId}

**Summary:** Updates Apple app management policy.

**Description:** Updates Apple app management policy



         Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Policy reference ID.
- `rule` (Required): Type: object. Description: Update Apple App Policy request.

**Responses:**
- **200**: OK.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.

---
### POST /appManagement/apple/common/policies

**Summary:** Creates Apple app management policy.

**Description:** Creates Apple app management policy



         Requires the call be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `rule` (Required): Type: object. Description: Apple App Policy details.

**Responses:**
- **200**: OK.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.

---
### DELETE /appManagement/apple/{referenceId}

**Summary:** Deletes an Apple app management policy.

**Description:** Deletes an Apple app management policy.


          Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The public identifier of App Store Records in MobiControl.

**Responses:**
- **200**: OK.
- **401**: Unauthorized.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>1 - Reference Id is either null, empty or consists only of white space.</li><li>2 - The given reference Id is not in valid format</li></ol>

---
### PUT /appManagement/apple/macOS/policies/{referenceId}/apps

**Summary:** Updates the specified macOS App Policy.

**Description:** Updates MacOS applications for selected Apple app management policy.



         Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference ID of the app policy.
- `request` (Required): Type: object. Description: AssociateMacAppsWithAppCatalogRuleRequest.

**Responses:**
- **200**: OK.
- **400**: Invalid request.
- **401**: Unauthorized.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>5131 - one or more MacOS app store apps has invalid App Store License Account configuration</li><li>5135 - one or more MacOS app store apps has invalid AppConfiguration configuration</li><li>5136 - one or more MacOS app store apps has invalid ConfigurationURI configuration</li><li>5137 - one or more MacOS app store apps has invalid ManagedAssociatedDomains configuration</li><li>5138 - one or more MacOS app store apps has invalid VppApplicationID configuration</li><li>5139 - one or more MacOS app store apps has invalid TimesPromptToInstall or PromptToInstall configuration</li></ol>

---

### GET /appManagement/apple/macOS/policies/{referenceId}/apps

**Summary:** Returns a list of macOS applications for an App Policy.

**Description:** Returns MacOS applications for selected Apple app management policy.



         Requires the caller be granted the "View App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference ID of the app policy.

**Responses:**
- **200**: OK.
- **400**: Invalid request.
- **401**: Unauthorized.

---
### PUT /appManagement/apple/iOS/policies/{referenceId}/apps

**Summary:** Updates the specified iOS App Policy.

**Description:** Updates iOS apps for specified Apple app management policy.



         Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference ID of the app policy.
- `request` (Required): Type: object. Description: AssociateIosAppsWithAppCatalogRuleRequest.

**Responses:**
- **200**: OK.
- **400**: Invalid request.
- **401**: Unauthorized.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>5131 - one or more iOS app store apps has invalid App Store License Account configuration</li><li>5132 - one or more iOS app store apps has invalid TimesPromptToInstall configuration</li><li>5133 - one or more mandatory iOS app store apps has invalid TimesPromptToInstall or PromptToInstall configuration</li><li>5134 - one or more iOS app store apps has invalid VppAccountGuid or VppApplicationId configuration</li></ol>

---

### GET /appManagement/apple/iOS/policies/{referenceId}/apps

**Summary:** Returns a list of iOS apps for an App Policy.

**Description:** Returns iOS apps for selected Apple app management policy.



         Requires the caller be granted the "View App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference ID of the app policy.

**Responses:**
- **200**: OK.
- **400**: Invalid request.
- **401**: Unauthorized.

---
### PUT /appManagement/apple/{referenceId}/banner

**Summary:** Updates App Policy Banner.

**Description:** Updates the App Policy banner of the provided policy reference ID.



         Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**

Content-Type of the Request body must be <code>multipart/related; boundary={boundary identifier}</code>

         Boundary length must be set to less than or equal to 11 to prevent internal server errors.


         Multipart request body must contain the following parts:
- image file - Contains image file with one of the following Content-Type:

image/gif```

image/png```

image/jpeg```

image/bmp```

image/x-icon```


         Mandatory headers

         Content-Disposition: attachment; filename="{image-filename}"


         Optional headers

         Content-Type-Encoding: binary

         The maximum size of the image file to be uploaded when using this endpoint is <u>1 MB</u>.


         The example below shows an banner image upload request.



         Content-Type: multipart/related; boundary=foo_bar_baz
         Content-Length: number_of_bytes_in_entire_request_body


         --foo_bar_baz
         Content-Type: image/jpeg


         Content-Disposition: attachment; filename="image_name.jpg"


         image data
         --foo_bar_baz--
         ```


**Parameters:**
- `referenceId` (Required): Type: string. Description: App Policy reference id.

**Responses:**
- **200**: Banner image uploaded successfully.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.
- **415**: Unsupported media type.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>5120 - file has invalid format, not one of .ico, .gif, .png, .bmp, .jpeg or .jpg</li><li>5121 - file exceeds 1MB limit.</li></ol>

---

### DELETE /appManagement/apple/{referenceId}/banner

**Summary:** Deletes App Policy Banner.

**Description:** Deletes an App Policy banner of the provided reference ID.



         Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: App Policy reference id.

**Responses:**
- **200**: App Policy banner deleted successfully.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.

---

### GET /appManagement/apple/{referenceId}/banner

**Summary:** Returns App Policy Banner.

**Description:** Returns an App Policy banner of the provided policy reference ID.



         Requires the caller be granted the "View App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: App Policy reference id.

**Responses:**
- **200**: App Policy banner retrieved successfully.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.

---
## App Management Policies

### GET /appManagement/policies

**Summary:** Returns app management policy summaries.

**Description:** Returns app management policy summaries



         Requires the caller be granted the "View App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `nameContains`: Type: string. Description: App management policy name filter.
- `families`: Type: array. Description: If specified, returns only app management policies for the selected families.
- `statuses`: Type: array. Description: If specified, returns only app management policies having the selected status(es).
- `isScheduled`: Type: boolean. Description: When true, return app management policies that currently have a schedule. When false, only return app management policies that do not have a schedule. If undefined, then do not take schedule status into account.
- `order`: Type: string. Description: Defines the sorting order by property. Pass the value as -property for descending, and +property for ascending.
- `skip`: Type: integer. Description: Input the first X (count) entries that should not be returned.
- `take`: Type: integer. Description: Input the number of entries to be returned, after skipping over the 'skip' count.

**Responses:**
- **200**: Return app management policy summaries successfully.
- **400**: Invalid request.
- **401**: Unauthorized.

---
### POST /appManagement/policies/{referenceId}/actions

**Summary:** Executes an action on selected app management policy.

**Description:** Executes an action on selected app management policy


         Supported Actions:
         - Enable - Enables the App management policy- Disable - Disables the App management policy

         Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: App management policy reference id.
- `action` (Required): Type: object. Description: The action to be performed on the app management policy.

**Responses:**
- **200**: Action executed successfully.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.

---
### PUT /appManagement/policies/{referenceId}/assignment

**Summary:** Updates app management policy assignment.

**Description:** Updates app management policy assignment



          Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: App management policy reference id.
- `assignment` (Required): Type: object. Description: App management policy assignment.

**Responses:**
- **200**: Return app management policy assignment successfully.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>5001 - Bad filter expression provided: {0}.</li><li>5003 - Cannot Disable the policy in the past, update the scheduled date.</li></ol>

---

### GET /appManagement/policies/{referenceId}/assignment

**Summary:** Returns app management policy assignment.

**Description:** Returns app management policy assignment



         Requires the caller be granted the "View App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: App management policy reference id.

**Responses:**
- **200**: Return app management policy assignment successfully.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.

---
### GET /appManagement/policies/{referenceId}/logs

**Summary:** Returns logs for selected app management policy.

**Description:** Returns logs for selected app management policy. Ordering is restricted to Timestamp.



         Requires the caller be granted the "View App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: App management policy reference id.
- `logSeverities`: Type: array. Description: Log severities.
- `startDate`: Type: string. Description: Start date.
- `endDate`: Type: string. Description: End date.
- `orderByDesc`: Type: boolean. Description: Determines the order. If set to true order is descending.
- `skip`: Type: integer. Description: Determines how many entities to skip.
- `take`: Type: integer. Description: Determines how many entities to take.

**Responses:**
- **200**: Return app management policy logs successfully.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.

---
### GET /appManagement/policies/{referenceId}/logs/summary

**Summary:** Returns logs summary for selected app management policy.

**Description:** Returns logs summary for selected app management policy



         Requires the caller be granted the "View App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: App management policy reference id.
- `startDate`: Type: string. Description: Start date.
- `endDate`: Type: string. Description: End date.

**Responses:**
- **200**: Return app management policy log summaries successfully.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.

---
## App Management Windows Apps

### POST /appManagement/windows/apps/enterprise/internal

**Summary:** Creates new enterprise Windows application hosted internally by MobiControl

**Description:** Uploads a Windows application(.xap, .appx and .msi) to be hosted internally by MobiControl.



         Requires the caller be granted the **"Manage App Policies"** permission.

**(Available Since MobiControl v15.3.0)**


Content-Type of the Request body must be multipart/related;<code>multipart/related; boundary={boundary identifier}</code>

         Boundary length must be set to less than or equal to 11 to prevent internal server errors.


         Multipart request body must contain the following parts:

- Application Kind info - Contains Content-Type and application kind, which should be one of <code>ModernEnterprise, Enterprise or ClassicDesktop</code>

         Content-Type: application/vnd.ms.application.metadata+json


         {"AppKind":"ModernEnterprise"}
         ```
- Application file - Contains application file content and headers:


         Content-Type: application/vnd.ms.application
         Content-Transfer-Encoding: base64
         Content-Disposition: attachment; filename="{application-filename}"


         Application file content encoded in base64
         ```

         The maximum size of the Windows application file to be uploaded when using this endpoint is <u>2 GB</u>.


         An example below shows an application upload request:



         Content-Type: multipart/related; boundary=mobicontrol_boundary
         Content-Length: number_of_bytes_in_entire_request_body


         --mobicontrol_boundary
         Content-Type: application/vnd.ms.application.metadata+json


         {"AppKind":"ModernEnterprise"}


         --mobicontrol_boundary
         Content-Type: application/vnd.ms.application
         Content-Transfer-Encoding: base64
         Content-Disposition: attachment; filename="[self_signed]W10UWP_1.0.2.0_x86.appx"


         application data encoded in base64
         --mobicontrol_boundary--
         ```


**Responses:**
- **200**: Internal application file uploaded successfully
- **400**: Invalid request, i.e., Invalid application file contents or metadata
- **403**: Forbidden
- **415**: Unsupported content media type
- **422**: Business Error<br />The following ErrorCode values can be returned:<br /><response code="500">Internal Error</response><ol><li>5300 - The application cannot be validated without a valid token.</li><li>5301 - The token is invalid.</li><li>5302 - Error reading the application file.</li><li>5303 - The file is signed with an incorrect token or expired certificate.</li><li>5304 - The certificate is expired.</li><li>5305 - Invalid application signer.</li><li>5306 - The file is not signed.</li><li>5307 - Invalid reference id.</li><li>5308 - The file is not a valid dependency.</li><li>5309 - The file type not supported.</li><li>5310 - Error parsing the classic application installer descriptor.</li><li>5311 - The application with reference Id: {0} is not found!</li><li>5312 - Transaction to save application {0} to database failed.</li><li>5313 - Save application {0} to database timed out.</li><li>5402 - Error parsing the parameter</li><li>5404 - The uploading application kind is not supported</li><li>5405 - Contract validation exception</li></ol>

---
### POST /appManagement/windows/apps/enterprise/external

**Summary:** Creates new enterprise Windows application hosted externally

**Description:** Creates a Windows application(.xap and .appx) to be hosted externally by MobiControl.



         Requires the caller be granted the **"Manage App Policies"** permission.

**(Available Since MobiControl v15.3.0)**


         The maximum size of the Windows application file to be uploaded when using this endpoint is <u>2 GB</u>.



**Parameters:**
- `request` (Required): Type: object. Description: Application External URL

**Responses:**
- **200**: External application file uploaded successfully
- **400**: Invalid request, i.e., Invalid application file contents or metadata
- **403**: Forbidden
- **415**: Unsupported content media type
- **422**: Business Error<br />The following ErrorCode values can be returned:<br /><response code="500">Internal Error</response><ol><li>5300 - The application cannot be validated without a valid token.</li><li>5301 - The token is invalid.</li><li>5302 - Error reading the application file.</li><li>5303 - The file is signed with an incorrect token or expired certificate.</li><li>5304 - The certificate is expired.</li><li>5305 - Invalid application signer.</li><li>5306 - The file is not signed.</li><li>5307 - Invalid reference id.</li><li>5308 - The file is not a valid dependency.</li><li>5309 - The file type not supported.</li><li>5310 - Error parsing the classic application installer descriptor.</li><li>5311 - The application with reference Id: {0} is not found!</li><li>5312 - Save application {0} to database failed.</li><li>5313 - Save application {0} to database timed out.</li><li>5400 - External URI does not appear to be a valid link.</li><li>5401 - The Company Hub App (XAP/APPX file) URI is invalid.</li><li>5402 - Error parsing the parameter</li><li>5404 - The uploading application kind is not supported</li><li>5405 - Contract validation exception</li></ol>

---
### GET /appManagement/windows/apps/{referenceId}

**Summary:** Returns details for the selected Windows application

**Description:** Returns details for the Windows application referred by &lt;ReferenceID&gt;.



         Requires the caller be granted the **"View App Policies"** permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Application reference id
- `appKind` (Required): Type: string. Description: Application kind

**Responses:**
- **200**: Returns Windows application details successfully
- **400**: Invalid request, i.e., Invalid application file contents or metadata
- **403**: Forbidden
- **422**: Business Error
- **500**: Internal Error

---
### GET /appManagement/windows/apps/{referenceId}/icon

**Summary:** Returns Windows application icon

**Description:** Returns Windows application icon data.



         Requires the caller be granted the **"View App Policies"** permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Application reference id
- `appKind` (Required): Type: string. Description: Application kind

**Responses:**
- **200**: Return application icon data stream successfully
- **400**: Invalid request, i.e., Invalid application file contents or metadata
- **403**: Forbidden
- **422**: Business Error<br />The following ErrorCode values can be returned:<br /><ol><li>5404 - The application kind is not supported</li></ol>

---
### GET /appManagement/windows/apps

**Summary:** Returns Windows applications' summaries

**Description:** Returns meta data of Windows applications matching search criteria.



         Requires the caller be granted the **"View App Policies"** permission.

**(Available Since MobiControl v15.3.0)**

The search criteria should be in the URI as array and contains the following parts:


**Name**: Application identity name
         **PublisherId**: Application publisher identity name
         **Version**: Application version
         **Architectures**: Application target processor architecture
         **MatchHigherVersion**: Flag to specify if accept application of higher version
         ```


         An example below shows the URI arguments of querying 2 applications' summary:



         ?[0].Name=Microsoft.VCLibs.140.00
         &amp;[0].PublisherIdName=Microsoft.VCLibs.140.00
         &amp;[0].Version=14.0.22929.0
         &amp;[0].Architectures=X86
         &amp;[0].MatchHigherVersion=true
         &amp;[1].Name=Microsoft.NET.Native.Framework.1.3
         &amp;[1].PublisherIdName=Microsoft.NET.Native.Framework.1.3
         &amp;[1].Version=1.3.24201.0
         &amp;[1].Architectures=X86
         &amp;[1].MatchHigherVersion=true
         ```


**Parameters:**
- `appQueryInfos`: Type: array. Description: Criteria to search applications

**Responses:**
- **200**: Return application meta data successfully
- **400**: Invalid request, i.e., Invalid application file contents or metadata
- **403**: Forbidden
- **422**: Business Error
- **500**: Internal Error

---
## App Management Windows Policies

### POST /appManagement/windows/policies

**Summary:** Creates Windows app management policy

**Description:** Creates Windows app management policy.



         Requires the caller be granted the **"Manage App Policies"** permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `appPolicy` (Required): Type: object. Description: Windows app management policy info

**Responses:**
- **200**: Create Windows app management policy successfully
- **400**: Invalid request, i.e., Invalid app policy info
- **403**: Forbidden
- **422**: Business Error
- **500**: Internal Error

---
### GET /appManagement/windows/policies/{referenceId}

**Summary:** Returns Windows app management policy details

**Description:** Returns Windows app management policy details.



         Requires the caller be granted the **"View App Policies"** permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Windows app management policy reference id

**Responses:**
- **200**: Return app management policy successfully
- **400**: Invalid request, i.e., Invalid reference id
- **403**: Forbidden
- **422**: Business Error
- **500**: Internal Error

---

### DELETE /appManagement/windows/policies/{referenceId}

**Summary:** Deletes Windows app management policy

**Description:** Deletes Windows app management policy.



         Requires the caller be granted the **"Manage App Policies"** permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Windows app management policy reference id

**Responses:**
- **200**: Delete Windows app management policy successfully
- **400**: Invalid request, i.e., Invalid reference id
- **403**: Forbidden
- **422**: Business Error
- **500**: Internal Error

---

### PUT /appManagement/windows/policies/{referenceId}

**Summary:** Updates Windows app management policy

**Description:** Updates Windows app management policy.



         Requires the caller be granted the **"Manage App Policies"** permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Windows app management policy reference id
- `appPolicy` (Required): Type: object. Description: Windows app management policy info

**Responses:**
- **200**: Update Windows app management policy successfully
- **400**: Invalid request, i.e., Invalid reference id or app policy
- **403**: Forbidden
- **422**: Business Error
- **500**: Internal Error

---
### PUT /appManagement/windows/policies/{referenceId}/apps

**Summary:** Updates Windows app for the selected policy

**Description:** Updates apps for selected Windows app management policy.



         Requires the caller be granted the **"Manage App Policies"** permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Windows app management policy reference id
- `request` (Required): Type: object. Description: Request to configure app policy applications

**Responses:**
- **200**: Update apps for selected Windows app management policy successfully
- **400**: Invalid request, i.e., Invalid reference id or request
- **403**: Forbidden
- **422**: Business Error<br />The following ErrorCode values can be returned:<br /><response code="500">Internal Error</response><ol><li>5407 - The app policy has no application associated.</li><li>5408 - The product setting for Windows Modern application is invalid.</li><li>5409 - The product setting error, the key must not be empty.</li><li>5410 - The product setting error, the key must be no more than 255 characters.</li><li>5411 - The product setting error, the char is not allowed as key.</li><li>5411 - The product setting error, the value is more than 8192 characters.</li><li>5412 - Unable to Force Provisioned Synchronization without Provisioning for all users.</li></ol>

---

### GET /appManagement/windows/policies/{referenceId}/apps

**Summary:** Returns Windows apps for the selected policy

**Description:** Returns apps for selected Windows app management policy.



         Requires the caller be granted the **"View App Policies"** permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Windows app management policy reference id

**Responses:**
- **200**: Return apps for selected Windows app management policy successfully
- **400**: Invalid request, i.e., Invalid reference id
- **403**: Forbidden
- **422**: Business Error
- **500**: Internal Error

---
## Apple Applications

### POST /appManagement/apple/iOS/apps/enterprise/internal

**Summary:** Creates an internal iOS enterprise application.

**Description:** Creates new iOS enterprise application hosted internally by MobiControl



         Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**

Content-Type of the Request body must be <code>multipart/related; boundary={boundary identifier}</code>

         Boundary length must be set to less than or equal to 11 to prevent internal server errors.


         Multipart request body must contain the following parts:
- application file - Contains application file with Content-Type:
application/vnd.ios.application```


         Mandatory headers

         Content-Disposition: attachment; filename="{application-filename}"


         Optional headers

         Content-Type-Encoding: binary

         The maximum size of the iOS enterprise application file to be uploaded when using this endpoint is <u>2 GB</u>.


         The example below shows an application upload request.



         Content-Type: multipart/related; boundary=foo_bar_baz
         Content-Length: number_of_bytes_in_entire_request_body


         --foo_bar_baz
         Content-Type: application/vnd.ios.application


         Content-Disposition: attachment; filename="application_name.ipa"


         application data
         --foo_bar_baz--
         ```


**Responses:**
- **200**: Application uploaded successfully.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.
- **415**: Unsupported media type.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>5100 - file has invalid format</li><li>5101 - file is not ipa</li><li>5106 - file exceeds maximum allowed limit</li><li>5109 - device management address not configured</li><li>5141 - The enterprise app contains files with a path longer than 260 characters and long paths are not supported.</li></ol>

---
### POST /appManagement/apple/iOS/apps/enterprise/{referenceId}/provisioningProfile

**Summary:** Updates provisioning profile for iOS enterprise application.

**Description:** Updates provisioning profile for iOS enterprise application



          Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**

Content-Type of the Request body must be <code>multipart/related; boundary={boundary identifier}</code>

          Boundary length must be set to less than or equal to 11 to prevent internal server errors.


          Multipart request body must contain the following parts:
- file - Contains iOS provisioning profile with Content-Type:
application/vnd.ios.provisioningprofile```


          Mandatory headers

          Content-Disposition: attachment; filename="{filename}"


          Content-Type-Encoding: binary

          The maximum size of the file to be uploaded when using this endpoint is <u>2 GB</u>.


          The example below shows an upload request.



          Content-Type: multipart/related; boundary=foo_bar_baz
          Content-Length: number_of_bytes_in_entire_request_body


          --foo_bar_baz
          Content-Type: application/vnd.ios.provisioningprofile


          Content-Disposition: attachment; filename="filename.mobileprovision"


          Content-Type-Encoding: binary


          application data
          --foo_bar_baz--
          ```


**Parameters:**
- `referenceId` (Required): Type: string. Description: Application reference ID.

**Responses:**
- **200**: File uploaded successfully.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.
- **415**: Unsupported media type.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>5104 - file has invalid format</li><li>5106 - file exceeds maximum allowed limit</li><li>5113 - application doesn't exist</li><li>5114 - application bundle id doesnt match</li></ol>

---
### POST /appManagement/apple/iOS/apps/enterprise

**Summary:** Deletes Apple iOS enterprise application.

**Description:** Update Apple iOS enterprise application.



         Requires the caller be granted the "Manage App Policies" permission.

**Parameters:**
- `request` (Required): Type: object. Description: IosEnterpriseApplicationMetadataUpdateRequest.

**Responses:**
- **200**: Application updated successfully.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.

---
### DELETE /appManagement/apple/iOS/apps/enterprise/{referenceId}

**Summary:** Deletes Apple iOS enterprise application.

**Description:** Deletes Apple iOS enterprise application.



         Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Application reference ID.

**Responses:**
- **200**: Application deleted successfully.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.

---
### DELETE /appManagement/apple/macOS/apps/enterprise/{referenceId}

**Summary:** Deletes Apple MacOS enterprise application.

**Description:** Deletes Apple MacOS enterprise application



         Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Application reference ID.

**Responses:**
- **200**: Application deleted successfully.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.

---
### POST /appManagement/apple/iOS/apps/enterprise/external

**Summary:** Creates an external iOS enterprise application.

**Description:** Creates new iOS enterprise application hosted externally



         Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**

         Returns retrieved application metadata.

Content-Type of the Request body must be <code>application/json</code>




**Parameters:**
- `request` (Required): Type: object. Description: AddExternalFileRequest.

**Responses:**
- **200**: Application added successfully.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>5101 - file is not ipa</li><li>5102 - URI has incorrect format</li><li>5103 - manifest file not found</li><li>5110 - The enterprise app contains files with a path longer than 260 characters and long paths are not supported.</li><li>5111 - manifest file is not correct</li><li>5112 - ipa file not found</li></ol>

---
### POST /appManagement/apple/common/apps/appStore

**Summary:** Creates Apple App Store applications.

**Description:** Creates Apple App Store applications.



         Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**

         Returns collection of applications with assigned reference ID.

Content-Type of the Request body must be <code>application/json</code>



**Parameters:**
- `applications` (Required): Type: object. Description: Collection of applications to add.

**Responses:**
- **200**: Applications added successfully.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.

---
### POST /appManagement/apple/macOS/apps/enterprise/internal

**Summary:** Creates an internal MacOS enterprise application.

**Description:** Creates new MacOS enterprise application hosted internally by MobiControl.



         Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Responses:**
- **200**: Application uploaded successfully.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.
- **415**: Unsupported media type.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>5105 - Invalid Mac app file</li><li>5106 - Max file size</li><li>5107 - Metadata not provided</li><li>5129 - Invalid app file</li></ol>

---
### POST /appManagement/apple/macOS/apps/enterprise/external

**Summary:** Creates an external MacOS enterprise application.

**Description:** Creates new MacOS enterprise application hosted externally



         Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `request` (Required): Type: object. Description: AddExternalMacAppRequest.

**Responses:**
- **200**: Application added successfully.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Business Error<br />The following ErrorCode values can be returned:.<br /><ol><li>5103 - No manifest found</li><li>5107 - Metadata not provided</li><li>5108 - Mac URI incorrect format</li><li>5116 - Mac manifest not correct</li><li>5117 - Referenced Mac file not found</li><li>5130 - Invalid app URL</li></ol>

---
### POST /appManagement/apple/iOS/apps/actions/forceUpdate

**Summary:** Forces application update.

**Description:** Forces Application update on devices



         Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**

Content-Type of the Request body must be <code>application/json</code>



**Parameters:**
- `request` (Required): Type: object. Description: ForceApplicationUpdateRequest.

**Responses:**
- **200**: Success.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.

---
### POST /appManagement/apple/common/apps/actions/forceUpdate

**Summary:** Forces application update.

**Description:** Forces Application update on devices



         Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**

Content-Type of the Request body must be <code>application/json</code>



**Parameters:**
- `request` (Required): Type: object. Description: ForceApplicationUpdateRequest.

**Responses:**
- **200**: Success.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.

---
### GET /appManagement/apple/common/apps/{referenceId}/icon

**Summary:** Returns application icon.

**Description:** Returns application icon for the application reference ID



         Requires the caller be granted the "View App Policies" permission.

**(Available Since MobiControl v15.3.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Application reference ID.
- `applicationKind` (Required): Type: string. Description: Application kind.

**Responses:**
- **200**: Success.
- **204**: No Content.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.

---
## Apple Automated Device Enrollment

### POST /apple/appleBusinessManager/deviceAccounts/publicKey

**Summary:** Generates a Public Key certificate for an MDM Server in Apple Business Manager

**Description:**
Requires the caller to be granted the "Manage Automated Device Enrollment - Accounts" permission.

**(Available Since MobiControl v15.3.0)**

Returns the certificate information of the generated Public Key certificate.

ReferenceId is used to download the certificate using GET /apple/appleBusinessManager/deviceAccounts/publicKey/{certificateReferenceId}.


**Responses:**
- **200**: Operation Successful
- **401**: Unauthorized attempt to execute the method

---
### GET /apple/appleBusinessManager/deviceAccounts/publicKey/{certificateReferenceId}

**Summary:** Downloads the specified Public Key certificate for an MDM Server in Apple Business Manager

**Description:**
Requires the caller to be granted the "Manage Automated Device Enrollment - Accounts" permission.

**(Available Since MobiControl v15.3.0)**

This API is used after calling POST /apple/appleBusinessManager/deviceAccounts/publicKey to generate the Public Key certificate.

Returns HttpResponseMessage with http code and application/octet-stream as certificate file content.


**Parameters:**
- `certificateReferenceId` (Required): Type: string. Description: The reference ID of the Public Key certificate as returned by the API.

**Responses:**
- **200**: Operation Successful
- **400**: Bad Request, i.e. invalid Certificate Reference Id
- **401**: Unauthorized attempt to execute the method
- **403**: Failed operation due to non-existing certificate record

---
### GET /apple/appleBusinessManager/deviceAccounts

**Summary:** Returns a list of all Apple Automated Device Enrollment accounts

**Description:**
Requires the caller to be granted the "MobiControl Access" permission.

**(Available Since MobiControl v15.3.0)**

Returns a list of AccountInfo properties


**Responses:**
- **200**: Operation Successful
- **401**: Unauthorized attempt to execute the method

---

### POST /apple/appleBusinessManager/deviceAccounts

**Summary:** Creates a new Apple Automated Device Enrollment account

**Description:**
Requires the caller to be granted the "Manage Automated Device Enrollment - Accounts" permission.

**(Available Since MobiControl v15.3.0)**

The request's headers must have: <code>Content-Type: multipart/related;boundary=mobicontrol_boundary</code>

         Boundary length must be set to less than or equal to 11 to prevent internal server errors.



The request's body:
         - Should be multipart request comprising of metadata and token file downloaded from Apple Business Manager.- Token file part of the request's body is mandatory and should be identified by <code>Content-Type: application/octet-stream</code>- Metadata part of request's body is mandatory and should be identified by <code>Content-Type: application/octet-stream.metadata+json</code>- Metadata is a JSON object with:
                 <ul style="list-style-type:circle">- AccountName: Friendly name of the account being created- CertificateReferenceId: The reference ID of the public key certificate (as returned by POST /apple/appleBusinessManager/deviceAccounts/publickey) used to generate the provided token file.

Sample request's body:


         --mobicontrol_boundary
         Content-Type: application/octet-stream.metadata+json


         {"AccountName":"string", "CertificateReferenceId":"The reference of the public key certificate (string)"}


         --mobicontrol_boundary
         Content-Type: application/octet-stream
         Content-Transfer-Encoding: base64
         Content-Disposition: attachment; filename="somecert.p7m"


         BASE64_ENCODED_TOKEN_FILE_CONTENT_HERE
         --mobicontrol_boundary--
         ```



**Responses:**
- **200**: Operation Successful
- **400**: Bad request.<br /><ol><li>If the request is missing TokenData</li><li>If the request is missing CertificateReferenceId</li><li>If the request is missing AccountName</li></ol>
- **401**: Unauthorized attempt to execute the method
- **403**: Failed operation due to non-existing certificate record
- **422**: Violated logical condition.
         <br />The following ErrorCode values can be returned:<br /><ol><li>1202 - If there was a failure to decrypt the server token.</li><li>1210 - If the Apple Device Management services could not be reached.</li><li>1211 - If the server token is successfully decrypted but found to be expired.</li><li>1214 - If the account name is used by another Automated Device Enrollment account.</li><li>1216 - If the test connection (retrieving a session token) with Apple Device Management services failed due to invalid authentication token.</li><li>1218 - If failed to retrieve account information (GET /account).</li><li>1219 - If MDM Server associated with the supplied MDM Server Token is the same as that of an existing account.</li></ol>

---
### GET /apple/appleBusinessManager/deviceAccounts/{accountReferenceId}

**Summary:** Returns the specified Apple Automated Device Enrollment account

**Description:**
Requires the caller to be granted the "MobiControl Access" permission.

**(Available Since MobiControl v15.3.0)**

Returns the specified Apple Automated Device Enrollment account by reference ID.


**Parameters:**
- `accountReferenceId` (Required): Type: string. Description: Account Reference ID

**Responses:**
- **200**: Operation Successful
- **400**: Bad Request, i.e. invalid Account Reference Id
- **401**: Unauthorized
- **403**: Forbidden

---

### PUT /apple/appleBusinessManager/deviceAccounts/{accountReferenceId}

**Summary:** Updates the specified Apple Automated Device Enrollment account

**Description:**
Requires the caller to be granted the "Manage Automated Device Enrollment - Accounts" permission.

**(Available Since MobiControl v15.3.0)**

Updates the specified Apple Automated Device Enrollment account corresponding to the account reference ID.


The request's headers must have: <code>Content-Type: multipart/related;boundary=mobicontrol_boundary</code>

         Boundary length must be set to less than or equal to 11 to prevent internal server errors.



The request's body:
         - Should be multipart request comprising of metadata and token file downloaded from Apple Business Manager.- Token file part of the request's body is mandatory should be identified by <code>Content-Type: application/octet-stream</code>- Metadata part of request's body is optional and should be identified by <code>Content-Type: application/octet-stream.metadata+json</code>- Metadata is a JSON object with:
                 <ul style="list-style-type:circle">- AccountName: Friendly name of the account being updated. If it is not specified, the account name will be unchanged- CertificateReferenceId: The reference ID of the public key certificate (as returned by POST /apple/appleBusinessManager/deviceAccounts/publickey) used to generate the provided token file.  If it is not specified, the public key certificate used to generate the current token file will be used to decrypt the provided token file

Sample request's body:


         --mobicontrol_boundary
         Content-Type: application/octet-stream.metadata+json


         {"AccountName":"string", "CertificateReferenceId":"The reference of the public key certificate (string)"}


         --mobicontrol_boundary
         Content-Type: application/octet-stream
         Content-Transfer-Encoding: base64
         Content-Disposition: attachment; filename="somecert.p7m"


         BASE64_ENCODED_TOKEN_FILE_CONTENT_HERE
         --mobicontrol_boundary--
         ```



**Parameters:**
- `accountReferenceId` (Required): Type: string. Description: Account Reference ID

**Responses:**
- **200**: Operation Successful
- **400**: Bad request.<br /><ol><li>If the request is missing TokenData</li><li>If the request is missing CertificateReferenceId</li><li>If the request is missing AccountName</li></ol>
- **401**: Unauthorized attempt to execute the method
- **403**: Failed operation due to non-existing certificate record
- **422**: Violated logical condition.
         <br />The following ErrorCode values can be returned:<br /><ol><li>1202 - If there was a failure to decrypt the server token.</li><li>1210 - If the Apple Device Management services could not be reached.</li><li>1211 - If the server token is successfully decrypted but found to be expired.</li><li>1214 - If the account name is used by another Automated Device Enrollment account.</li><li>1216 - If the test connection (retrieving a session token) with Apple Device Management services failed due to invalid authentication token.</li><li>1218 - If failed to retrieve account information (GET /account).</li><li>1220 - If MDM Server associated with the supplied MDM Server Token is different than that of the current account.</li></ol>

---

### DELETE /apple/appleBusinessManager/deviceAccounts/{accountReferenceId}

**Summary:** Deletes the specified Apple Automated Device Enrollment account

**Description:**
Requires the caller to be granted the "Manage Automated Device Enrollment - Accounts" permission.

**(Available Since MobiControl v15.3.0)**

Deletes the specified Apple Automated Device Enrollment account corresponding to the account reference ID.


**Parameters:**
- `accountReferenceId` (Required): Type: string. Description: Account Reference ID

**Responses:**
- **200**: Operation Successful
- **400**: Bad Request, i.e. invalid Account Reference Id
- **401**: Unauthorized attempt to execute the method
- **403**: Forbidden
- **422**: Violated logical condition.
         <br />The following ErrorCode values can be returned:<br /><ol><li>1217 - If the account is used by an Add Device Rule.</li></ol>

---
### PUT /apple/appleBusinessManager/deviceAccounts/{accountReferenceId}/name

**Summary:** Updates the specified Apple Automated Device Enrollment account's name

**Description:**
Requires the caller to be granted the "Manage Automated Device Enrollment - Accounts" permission.

**(Available Since MobiControl v15.3.0)**

Call shall contains following parameters:

AccountName - This is AccountName shall be updated



**Parameters:**
- `accountReferenceId` (Required): Type: string. Description: Account Reference ID
- `accountName` (Required): Type: object. Description:

**Responses:**
- **200**: Operation Successful
- **400**: Bad Request, i.e. invalid Account Reference Id or Account Name
- **401**: Unauthorized attempt to execute the method
- **403**: Forbidden
- **422**: Violated logical condition.
         <br />The following ErrorCode values can be returned:<br /><ol><li>1214 - If the account name is used by another Automated Device Enrollment account.</li></ol>

---
### POST /apple/appleBusinessManager/deviceAccounts/{accountReferenceId}/actions/test

**Summary:** Test connection with Apple's Automated Device Enrollment server using specified account

**Description:**
Requires the caller to be granted the "Manage Automated Device Enrollment - Accounts" permission.

**(Available Since MobiControl v15.3.0)**

Returns HttpResponseMessage OK (200)


**Parameters:**
- `accountReferenceId` (Required): Type: string. Description: Account Reference ID

**Responses:**
- **200**: Operation Successful
- **400**: Bad Request, i.e. invalid Account Reference Id
- **401**: Unauthorized attempt to execute the method
- **403**: Forbidden
- **422**: Violated logical condition.
         <br />The following ErrorCode values can be returned:<br /><ol><li>1210 - If MobiControl cannot establish a connection with Apple Automated Device Enrollment service to retrieve a session token using the MDM Server Token.</li><li>1211 - If the server token is successfully decrypted but found to be expired.</li><li>1216 - If Apple rejects the connection due to an invalid authentication token.</li></ol>

---
### POST /apple/appleBusinessManager/deviceAccounts/{accountReferenceId}/actions/sync

**Summary:** Synchronize Apple Automated Device Enrollment account corresponding to the account reference ID

**Description:**
Requires the caller to be granted the "Manage Automated Device Enrollment - Accounts" permission.

**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `accountReferenceId` (Required): Type: string. Description: Account Reference ID

**Responses:**
- **200**: Operation Successful
- **400**: Bad Request, i.e. invalid Account Reference Id
- **401**: Unauthorized attempt to execute the method
- **403**: Forbidden
- **422**: Violated logical condition.
         <br />The following ErrorCode values can be returned:<br /><ol><li>1210 - If MobiControl cannot establish a connection with Apple Automated Device Enrollment service to retrieve a session token using the MDM Server Token.</li><li>1211 - If the server token is successfully decrypted but found to be expired.</li><li>1216 - If Apple rejects the connection due to an invalid authentication token.</li><li>1222 - If MobiControl already synchronizing an account.</li></ol>

---
### GET /apple/appleBusinessManager/deviceAccounts/{accountReferenceId}/rules

**Summary:** Retrieve all Add Device Rules associated with an Automated Device Enrollment account

**Description:**
Requires the caller to be granted the "Manage Automated Device Enrollment - Accounts" permission.

**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `accountReferenceId` (Required): Type: string. Description: Account Reference ID

**Responses:**
- **200**: Operation Successful
- **400**: Bad Request, i.e invalid Account Reference Id
- **401**: Unauthorized attempt to execute the method
- **403**: Forbidden

---
### POST /apple/appleBusinessManager/deviceAccounts/{accountReferenceId}/devices/actions/assignProfile

**Summary:** Assign Automated Device Enrollment devices to the specified Enrollment Policy.

**Description:**

**(Available Since MobiControl v15.6.0)**

Requires the caller be granted the "Manage Automated Device Enrollment - Devices" permission.

Request body: Model with list of devices SerialNumbers.

Responses Body: EnrollmentDevices

content-type: application/json.

**Parameters:**
- `accountReferenceId` (Required): Type: string. Description: Account Reference ID.
- `adeDevices` (Required): Type: object. Description: Request body with the enrollment Policy Reference ID and list of SerialNumber of devices to be assigned to EnrollmentPolicy.

**Responses:**
- **200**: Operation Successful.
- **400**: Failed operation due to bad request.
- **401**: Unauthorized attempt to execute the method.
- **403**: Failed operation due to non-existing Automated Device Enrollment account.
- **422**: Failed operation due to business logic error.

---
### POST /apple/appleBusinessManager/deviceAccounts/{accountReferenceId}/actions/setDefaultRule

**Summary:** Set a Default Add Device Rule for an Automated Device Enrollment account

**Description:**
Requires the caller to be granted the "Manage Automated Device Enrollment - Accounts" permission.

**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `accountReferenceId` (Required): Type: string. Description: Account Reference ID
- `defaultRuleModel` (Required): Type: object. Description:

**Responses:**
- **200**: Operation Successful
- **400**: Bad Request, i.e invalid Account Reference Id
- **401**: Unauthorized attempt to execute the method
- **403**: Forbidden
- **422**: Violated logical condition.
         <br />The following ErrorCode values can be returned:<br /><ol><li>1221 - If Add Device Rule cannot be set as the Default Add Device Rule because it is not associated with the specified Automated Device Enrollment account.</li></ol>

---
### GET /apple/appleBusinessManager/deviceAccounts/{accountReferenceId}/enrollmentPolicies

**Summary:** Retrieve all Enrollment Policies associated with the specified Automated Device Enrollment account

**Description:**
Requires the caller to be granted the "Manage Automated Device Enrollment - Accounts" permission.

**(Available Since MobiControl v15.6.0)**

**Parameters:**
- `accountReferenceId` (Required): Type: string. Description: Account Reference ID

**Responses:**
- **200**: Operation Successful
- **400**: Bad Request, i.e invalid Account Reference Id
- **401**: Unauthorized attempt to execute the method
- **403**: Forbidden

---
### GET /apple/appleBusinessManager/deviceAccounts/{accountReferenceId}/devices

**Summary:** Retrieve all Automated Device Enrollment devices assigned to the specified Enrollment Policy.

**Description:**
Requires the caller be granted the "Manage Automated Device Enrollment - Devices" permission.

Request body: nothing.

Responses Body: EnrollmentDevices

content-type: application/json.

**(Available Since MobiControl v15.6.0)**

**Parameters:**
- `accountReferenceId` (Required): Type: string. Description: Account Reference ID.
- `enrollmentPolicyReferenceId`: Type: string. Description: Enrollment Policy Reference ID.
- `filterValue`: Type: integer. Description: Filter value.
         When FilterType = 1 (ByEnrollmentStatus), valid value [Not enrolled =0 , Enrolled = 1, UnEnrolled =2].
         When FilterType = 2 (ByProfileStatus), valid value [Unknown = 0, Empty = 1, Assigned = 2, Pushed = 3, Removed = 4].
- `filterType`: Type: string. Description: FilterType.
- `search`: Type: string. Description:
- `order`: Type: string. Description: Defines the sorting order by property. Pass the value as -property for descending, and +property for ascending.
- `skip`: Type: integer. Description: Input the first X (count) entries that should not be returned.
- `take`: Type: integer. Description: Input the number of entries to be returned, after skipping over the 'skip' count.

**Responses:**
- **200**: Operation Successful.
- **400**: Failed operation due to bad request.
- **401**: Unauthorized attempt to execute the method.
- **403**: Failed operation due to non-existing Automated Device Enrollment account.
- **422**: Failed operation due to business logic error.

---
### POST /apple/appleBusinessManager/deviceAccounts/{accountReferenceId}/actions/mac/setDefaultPolicy

**Summary:** Sets/Removes default mac enrollment policy for an Automated Device Enrollment account.

**Description:**
This API Sets/Removes default macOS enrollment policy for an Automated Device Enrollment account.
          User need to send "EnrollmentPolicyReferenceId" property as empty in order to remove associated default enrollment policy for an Automated Device Enrollment account.

Requires the caller be granted the "Manage Automated Device Enrollment - Accounts" permission.

**(Available since MobiControl v15.6.0)**

**Parameters:**
- `accountReferenceId` (Required): Type: string. Description: Account Reference ID.
- `defaultEnrollmentPolicy` (Required): Type: object. Description: Default Mac Enrollment Policy.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Business Logic Exception.
          <br />The following ErrorCode values can be returned:.<br /><ol><li>1225 - Enrollment Policy cannot be set as the Default Policy because it is not associated with the specified Automated Device Enrollment account.</li></ol>

---
### POST /apple/appleBusinessManager/deviceAccounts/{accountReferenceId}/actions/ios/setDefaultPolicy

**Summary:** Sets/Removes default Ios enrollment policy for an Automated Device Enrollment account.

**Description:**
This API Sets/Removes default Ios enrollment policy for an Automated Device Enrollment account.
         User need to send "EnrollmentPolicyReferenceId" property as empty in order to remove associated default enrollment policy for an Automated Device Enrollment account.

Requires the caller be granted the "Manage Automated Device Enrollment - Accounts" permission.

**(Available since MobiControl v15.6.0)**

**Parameters:**
- `accountReferenceId` (Required): Type: string. Description: Account Reference ID.
- `defaultEnrollmentPolicy` (Required): Type: object. Description: Default Ios Enrollment Policy.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Business Logic Exception.
         <br />The following ErrorCode values can be returned:.<br /><ol><li>1225 - Enrollment Policy cannot be set as the Default Policy because it is not associated with the specified Automated Device Enrollment account.</li></ol>

---
## Apple Ios Wallpaper

### PUT /enrollmentPolicies/apple/iOS/{referenceId}/wallpaper

**Summary:** Update the iOS wallpaper for specified Enrollment Policy.

**Description:** This API updates the iOS wallpaper for the specified Enrollment Policy.



         Requires the caller be granted the "Manage Enrollment Policies" permission.

**(Available since MobiControl v15.6.0)**

Content-Type of the Request body must be <code>multipart/related; boundary={any boundary identifier}</code>

         Multipart request body must contain the following parts:
- image file - Contains image file with one of the following Content-Type:

image/png```

image/jpeg```

image/jpg```


         Mandatory headers

         Content-Disposition: attachment; filename="{image-filename}"


         Optional headers

         Content-Type-Encoding: binary

         The example below shows an wallpaper upload request.



         Content-Type: multipart/related; boundary=foo_bar_baz
         Content-Length: number_of_bytes_in_entire_request_body


         --foo_bar_baz
         Content-Type: image/jpeg


         Content-Disposition: attachment; filename="image_name.jpg"


         image data
         --foo_bar_baz--
         ```


**Parameters:**
- `referenceId` (Required): Type: string. Description: Unique identifier for an enrollment policy.
- `modelType` (Required): Type: string. Description: Model type will be either Iphone or Ipad.
- `screenType` (Required): Type: string. Description: Screen type will be Home Screen or Lock Screen.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **415**: Unsupported media type.
- **422**: Business Logic Exception<br />The following ErrorCode values can be returned:.<br /><ol><li>7804 - You have selected a file with the incorrect format. Please select another .png, .jpeg or .jpg file.</li></ol>

---
### GET /enrollmentPolicies/apple/iOS/{referenceId}/wallpaper/{screenType}/{modelType}

**Summary:** Returns the wallpaper for specified iOS Enrollment Policy.

**Description:** This API returns the wallpaper for specified iOS Enrollment Policy



         Requires the caller be granted the "View Enrollment Policies" permission.

**(Available since MobiControl v15.6.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Unique identifier for an enrollment policy.
- `screenType` (Required): Type: string. Description: Screen type will be Home Screen or Lock Screen.
- `modelType` (Required): Type: string. Description: Model type will be either Iphone or Ipad.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **204**: No Content.

---
### DELETE /enrollmentPolicies/apple/iOS/{referenceId}/wallpaper/{screenType}/{modelType}/delete

**Summary:** Deletes the specified iOS enrollment policy wallpaper.

**Description:** This API deletes the specified iOS enrollment policy wallpaper


         For iPhone set Model Type as 1 and for iPad set Model Type as 2


         For Home screen set Screen Type as 1 and for Lock screen set Screen Type as 2



         Requires the caller be granted the "Manage Enrollment Policies" permission.

**(Available since MobiControl v15.6.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Unique identifier for an enrollment policy.
- `screenType` (Required): Type: string. Description: Screen type will be Home Screen or Lock Screen.
- `modelType` (Required): Type: string. Description: Model type will be either Iphone or Ipad.

**Responses:**
- **400**: Contract validation failed.
- **403**: Forbidden.
- **204**: No Content.

---
## Apple Redemption Codes

### POST /appManagement/apple/iOS/redemptionCodes/{applicationId}/actions/cleanup

**Summary:** Cleans up unused redemption codes.

**Description:** Cleans up unused redemption codes



         Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0)**

Content-Type of the Request body must be <code>application/json</code>



**Parameters:**
- `applicationId` (Required): Type: string. Description: Application ID.
- `request` (Required): Type: object. Description: request.

**Responses:**
- **204**: Success.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.

---
### GET /appManagement/apple/iOS/redemptionCodes/{applicationId}

**Summary:** Returns application information.

**Description:** Returns application information



         Requires the caller be granted the "View App Policies" permission.

**(Available Since MobiControl v15.3.0)**

Content-Type of the Request body must be <code>application/json</code>



**Parameters:**
- `applicationId` (Required): Type: string. Description: Application ID.
- `appPolicyReferenceId`: Type: string. Description: Application Policy Reference ID.
- `useCodes`: Type: boolean. Description: Use codes flag.
- `useCodesExclusive`: Type: boolean. Description: Use codes exclusive flag.

**Responses:**
- **200**: Success.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.
- **415**: Unsupported media type.
- **422**: Business Error.

---

### POST /appManagement/apple/iOS/redemptionCodes/{applicationId}

**Summary:** Uploads redemption codes.

**Description:** Uploads redemption codes from Microsoft Excel file.

</br>
         Requires the caller be granted the "Manage App Policies" permission.

**(Available Since MobiControl v15.3.0).**</br>
Content-Type of the Request body must be.<code>multipart/related; boundary={boundary identifier}</code>

         Boundary length must be set to less than or equal to 11 to prevent internal server errors.


          Multipart request body must contain the following parts:.
- MS Excel file - Contains MS Excel file with Content-Type:
application/vnd.ms-excel```


          or
application/vnd.openxmlformats-officedocument.spreadsheetml.sheet```

- metadata - Contains json-formatted information with Content-Type:
application/vnd.ms-excel.metadata+json```

          or
application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.metadata+json```


          Mandatory headers

          Content-Disposition: attachment; filename="{filename}"


          Content-Type-Encoding: binary

         The maximum size of the MS Excel file to be uploaded when using this endpoint is <u>2 GB.</u>.
</br>
         The example below shows an upload request.



          Content-Type: multipart/related; boundary=foo_bar_baz
          Content-Length: number_of_bytes_in_entire_request_body


          --foo_bar_baz
          Content-Type: application/vnd.ms-excel.metadata+json

         {"ExpectedName":"Tetris",

         "SuppressUpdateIssues":[3],

         "AppPolicyReferenceId":"b2467f93-7042-4792-be20-e3103acbf547"}

          --foo_bar_baz
          Content-Type: application/vnd.ms-excel


          Content-Disposition: attachment; filename="filename.xls"


          Content-Type-Encoding: binary


          application data
          --foo_bar_baz--.
          ```


**Parameters:**
- `applicationId` (Required): Type: string. Description: Application ID.

**Responses:**
- **200**: File uploaded successfully.
- **400**: Invalid request.
- **401**: Unauthorized.
- **415**: Unsupported media type.

---
### GET /appManagement/apple/iOS/redemptionCodes/{applicationId}/summary

**Summary:** Returns the redemption codes collection.

**Description:** Returns the redemption codes collection



         Requires the caller be granted the "View App Policies" permission.

**(Available Since MobiControl v15.3.0)**

Content-Type of the Request body must be <code>application/json</code>



**Parameters:**
- `applicationId` (Required): Type: string. Description: Application ID.
- `appPolicyReferenceId`: Type: string. Description: Application Policy Reference ID.
- `skip`: Type: integer. Description: Number of entries to skip.
- `take`: Type: integer. Description: Number of entries to take.

**Responses:**
- **200**: Success.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.

---
## Apple Volume Purchase Program Account

### POST /apple/appleBusinessManager/licenseAccounts/{accountId}/actions/refresh

**Summary:** Refresh the specified App Store License account.

**Description:**
Requires the caller to be granted the "Manage Servers and Global Settings" permission.

**(Available Since MobiControl v15.3.0)**</br>

**Parameters:**
- `accountId` (Required): Type: string. Description: The public identifier of App Store Records in MobiControl.

**Responses:**
- **201**:
- **400**: Bad request.<br /><ol><li>If the request missing AccountId</li></ol>
- **401**: Unauthorized attempt to execute the method.
- **403**: Failed operation due to non-existing account.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>1302 - Refresh account licensing information failed.</li><li>1340 - The license account is owned by a different MobiControl instance</li><li>1304 - Apple's App Store License Management service is unavailable.  Retry after {0} (UTC).</li><li>1328 - The Apple App Store License Management account token is invalid.</li><li>1346 - The Apple App Store License Management account token is revoked.</li><li>1343 - The Apple service cannot be reached.</li><li>1303 - The Apple's App Store License Management token you are attempting to upload has expired.</li><li>1333 - The App Store License Management services returned an unexpected error.</li><li>1347 - A connection with Apple iTunes service cannot be established to retrieve information about apps in this account.</li><li>1348 - Failed to retrieve information about an app (ID: {0}) in this account using the Apple iTunes service.</li><li>1349 - An unexpected error occurred while communicating with the App Store License Management service (Error: {0}).</li><li>1352 - Failed to refresh the Apple App Store License Management account '{0}', because another refresh or reconciliation is already in progress.</li></ol>

---
### POST /apple/appleBusinessManager/licenseAccounts/actions/reconcile

**Summary:** Reconcile all App Store License accounts.

**Description:**
Requires the caller to be granted the "Manage Servers and Global Settings" permission.

**(Available Since MobiControl v15.3.0)**</br>

Reconcile all App Store License accounts by revoking all licenses and users assigned or created by this instance of MobiControl

Call type : Async call</br>

**Parameters:**
- `reconcileAccount` (Required): Type: object. Description: Reconcile App Store License account.

**Responses:**
- **201**:
- **400**: Bad request.
- **422**: <br>Violated logical condition. </br>
<ol>
<li>1340 - The license account is owned by a different MobiControl instance </li>
<li>1343 - The Apple service cannot be reached</li>
<li>1304 - Apple's App Store License Management service is unavailable.  Retry after {0} (UTC).</li>
<li>1303 - The Apple's App Store License Management token you are attempting to upload has expired.</li>
<li>1328 - The Apple App Store License Management account token is invalid.</li>
<li>1346 - The Apple App Store License Management account token is revoked.</li>
<li>1333 - The App Store License Management services returned an unexpected error.</li>
<li>1349 - An unexpected error occurred while communicating with the App Store License Management service (Error: {0}).</li>
<li>1353 - Failed to reconcile the Apple App Store License Management accounts, because another refresh or reconciliation is already in progress.</li>
</ol>
- **401**: Unauthorized attempt to execute the method.

---
### PUT /apple/appleBusinessManager/licenseAccounts/{accountId}

**Summary:** Updates the specified App Store License account's name or server token.

**Description:**
Requires the caller to be granted the "Manage Servers and Global Settings" permission.

**(Available Since MobiControl v15.3.0)**

The request's headers must have: <code>Content-Type: multipart/related;boundary=mobicontrol_boundary</code>

         Boundary length must be set to less than or equal to 11 to prevent internal server errors.



The request's body:
         - Should be multipart request comprising of metadata and certificate content encoded in base64.-  Token file part of the request's body is mandatory and should be identified by Content-Type: application/octet-stream.-  Metadata part of request's body is mandatory and should be identified by Content-Type: application/octet-stream.metadata.-  Metadata is a JSON object with:

         -- AccountName: Friendly name of the account being created.

         -- ClaimOwnership: (Optional) If it is true, MobiControl will claim ownership of the account if it is owned by another host.If it is not specified, it defaults to false.

         -- RetireExistingUsers: (Optional) If it is true, MobiControl will retire all existing users associated with this account.If it is not specified, it defaults to false.


Sample request's body:


--mobicontrol_boundary                                               </br>
Content-Disposition: form-data; name="fieldNameHere"; filename="test.vpptoken"            </br>
Content-Type: application/octet-stream                                                    </br>
 eyJleHBEYXRlIjoiMjAyMS0wMi0yNlQxMToyOTo0OC0wODAwIiwidG9rZW4iOiIvMmY2ZUNMTTM2d01ERUpJ  </br>
--mobicontrol_boundary                                                 </br>
 Content-Type: application/octet-stream.metadata                                       </br>
{AccountName:"Test34", ClaimOwnership : true}                                                                   </br>
--mobicontrol_boundary--</br>```


**Parameters:**
- `accountId` (Required): Type: string. Description: The public identifier of App Store Records in MobiControl.

**Responses:**
- **201**:
- **400**: Bad request.
- **401**: Unauthorized attempt to execute the method.
- **403**: Failed operation due to non-existing account.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>1336 - Failed to claim ownership of Apple App Store License Account ID</li><li>1302 - Refresh account licensing information failed.</li><li>1308 - The Apple App Store License account name '{0}' is already added to the system, please use another name.</li><li>1345 - Error updating account '{0}', because the provided token belongs to a different location '{1}({2})' than the existing account's location '{3}({4})'</li><li>1331 - Error updating account '{0}', because it is owned by a different MobiControl instance ({1})</li><li>1303 - The Apple's App Store License Management token you are attempting to upload has expired.</li><li>1304 - Apple's App Store License Management service is unavailable.  Retry after {0} (UTC).</li><li>1343 - The Apple service cannot be reached.</li><li>1327 - The Apple App Store License Management account token is invalid or expired.</li><li>1328 - The Apple App Store License Management account token is invalid.</li><li>1346 - The Apple App Store License Management account token is revoked.</li><li>1333 - The App Store License Management services returned an unexpected error.</li><li>1347 - A connection with Apple iTunes service cannot be established to retrieve information about apps in this account.</li><li>1348 - Failed to retrieve information about an app (ID: {0}) in this account using the Apple iTunes service.</li><li>1349 - An unexpected error occurred while communicating with the App Store License Management service (Error: {0}).</li><li>1351 - Failed to update the Apple App Store License Management account '{0}', because another update is already in progress.</li></ol>

---

### DELETE /apple/appleBusinessManager/licenseAccounts/{accountId}

**Summary:** Deletes the specified App Store License account.

**Description:**
Requires the caller to be granted the "Manage Servers and Global Settings" permission.

**(Available Since MobiControl v15.3.0)**</br>
          Call Type : Async call.

**Parameters:**
- `accountId` (Required): Type: string. Description: The public identifier of App Store Records in MobiControl.

**Responses:**
- **201**:
- **400**: Bad request.
- **401**: Unauthorized attempt to execute the method.
- **403**: Failed operation due to non-existing account.
- **422**: <ol>
<li>1342 - Error deleting account '{0}', because the account is used by at least one app in your App Policies</li>
<li>1343 - The Apple service cannot be reached</li>
<li>1304 - Apple's App Store License Management service is unavailable.  Retry after {0} (UTC).</li>
<li>1349 - An unexpected error occurred while communicating with the App Store License Management service (Error: {0}).</li>
</ol>

---

### GET /apple/appleBusinessManager/licenseAccounts/{accountId}

**Summary:** Returns the specified App Store License account's summary.

**Description:**
Requires the caller to be granted the "MobiControl Access" permission.

**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `accountId` (Required): Type: string. Description: The public identifier of App Store Records in MobiControl.

**Responses:**
- **200**:
- **400**: Bad request.
- **401**: Unauthorized attempt to execute the method.
- **403**: Failed operation due to non-existing account.

---
### POST /apple/appleBusinessManager/licenseAccounts

**Summary:** Creates a new App Store License account.

**Description:**
Requires the caller to be granted the "Manage Servers and Global Settings" permission.

**(Available Since MobiControl v15.3.0)**

The request's headers must have: <code>Content-Type: multipart/related;boundary=mobicontrol_boundary</code>

         Boundary length must be set to less than or equal to 11 to prevent internal server errors.



The request's body:
         - Should be multipart request comprising of metadata and certificate content encoded in base64.-   Token file part of the request's body is mandatory and should be identified by Content-Type: application/octet-stream.-  Metadata part of request's body is mandatory and should be identified by Content-Type: application/octet-stream.metadata.-  Metadata is a JSON object with:

         -- AccountName: Friendly name of the account being created.

         -- ClaimOwnership: (Optional) If it is true, MobiControl will claim ownership of the account if it is owned by another host.If it is not specified, it defaults to false.

         -- RetireExistingUsers: (Optional) If it is true, MobiControl will retire all existing users associated with this account.If it is not specified, it defaults to false.


Sample request's body:


--mobicontrol_boundary                                               </br>
Content-Disposition: form-data; name="fieldNameHere"; filename="test.vpptoken"            </br>
Content-Type: application/octet-stream                                                    </br>
 eyJleHBEYXRlIjoiMjAyMS0wMi0yNlQxMToyOTo0OC0wODAwIiwidG9rZW4iOiIvMmY2ZUNMTTM2d01ERUpJ  </br>
--mobicontrol_boundary                                                 </br>
 Content-Type: application/octet-stream.metadata                                       </br>
{AccountName:"Test34", ClaimOwnership : true, RetireExistingUsers: false }                                                               </br>
--mobicontrol_boundary--</br>```


**Responses:**
- **400**: Bad request.
- **200**:
- **401**: Unauthorized attempt to execute the method.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>1316 - The Apple App Store License token you are attempting to upload already exists under different account. </li><li>1343 - The Apple service cannot be reached</li><li>1308 - The Apple's App Store License Management account name '{0}' is already added to the system, please use another name.</li><li>1303 - The Apple's App Store License Management token you are attempting to upload has expired.</li><li>1327 - The Apple App Store License Management account token is invalid or expired.</li><li>1328 - The Apple App Store License Management account token is invalid.</li><li>1346 - The Apple App Store License Management account token is revoked.</li><li>1336 - Failed to claim ownership of Apple's App Store License Management Account ID '{0}'</li><li>1311 - Add Apple's Apple's App Store License Management License Management account '{0}' failed because fail to retire existing users.</li><li>1335 - Apple's App Store License Management Account '{0}' no longer managed by this instance of MobiControl but by '{1}'</li><li>1304 - Apple's App Store License Management service is unavailable.  Retry after {0} (UTC).</li><li>1333 - The App Store License Management services returned an unexpected error.</li><li>1347 - A connection with Apple iTunes service cannot be established to retrieve information about apps in this account.</li><li>1348 - Failed to retrieve information about an app (ID: {0}) in this account using the Apple iTunes service.</li><li>1349 - An unexpected error occurred while communicating with the App Store License Management service (Error: {0}).</li><li>1350 - Failed to add the Apple App Store License Management account '{0}', because another account is being added.</li></ol>

---

### GET /apple/appleBusinessManager/licenseAccounts

**Summary:** Returns a list of App Store License accounts.

**Description:**
Requires the caller to be granted the "MobiControl Access" permission.

**(Available Since MobiControl v15.3.0)**

**Responses:**
- **200**:
- **400**: Bad request.
- **401**: Unauthorized.

---
### PUT /apple/appleBusinessManager/licenseAccounts/{accountId}/name

**Summary:** Updates the specified App Store License account's name.

**Description:**
Requires the caller to be granted the "Manage Servers and Global Settings" permission.

**(Available Since MobiControl v15.3.0)**</br>

**Parameters:**
- `accountId` (Required): Type: string. Description: The public identifier of App Store Records in MobiControl.
- `updateAccount` (Required): Type: object. Description: VppUpdateAccountName.

**Responses:**
- **400**: Bad request.<br /><ol><li>If the request missing AccountId</li><li>If the request body is missing</li></ol>
- **201**:
- **401**: Unauthorized attempt to execute the method.
- **403**: Failed operation due to non-existing account.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>1308 - The Apple App Store License account name '{0}' is already added to the system, please use another name.</li></ol>

---
### POST /apple/appleBusinessManager/licenseAccounts/{accountId}/actions/cleanUp

**Summary:** Clean up the specified App Store License account.

**Description:**
Requires the caller to be granted the "Manage Servers and Global Settings" permission.

**(Available Since MobiControl v15.3.0)**</br>

Clean up the specified App Store License account by revoking all licenses and users NOT assigned or created by this instance of MobiControl.

         Call Type : Async Call.

**Parameters:**
- `accountId` (Required): Type: string. Description: The public identifier of App Store Records in MobiControl.

**Responses:**
- **201**:
- **400**: Bad request.
- **401**: Unauthorized attempt to execute the method.
- **403**: Failed operation due to non-existing account.
- **422**: <ol>
<li>1340 - The license account is owned by a different MobiControl instance</li>
<li>1304 - Apple's App Store License Management service is unavailable.  Retry after {0} (UTC).</li>
<li>1343 - The Apple service cannot be reached.</li>
<li>1303 - The Apple's App Store License Management token you are attempting to upload has expired.</li>
<li>1328 - The Apple App Store License Management account token is invalid.</li>
<li>1346 - The Apple App Store License Management account token is revoked.</li>
<li>1333 - The App Store License Management services returned an unexpected error.</li>
<li>1349 - An unexpected error occurred while communicating with the App Store License Management service (Error: {0}).</li>
</ol>

---
### POST /apple/appleBusinessManager/licenseAccounts/{accountId}/actions/reclaimOwnership

**Summary:** Reclaim ownership of the specified App Store License account.

**Description:**
Requires the caller to be granted the "Manage Servers and Global Settings" permission.

**(Available Since MobiControl v15.3.0)**</br>

**Parameters:**
- `accountId` (Required): Type: string. Description: Identifier of the target account.

**Responses:**
- **201**:
- **401**: Unauthorized attempt to execute the method.
- **400**: Bad request.
- **403**: Failed operation due to non-existing account.
- **422**: <ol>
<li>1343 - The Apple service cannot be reached</li>
<li>1336 - Failed to claim ownership of Apple App Store License Account ID</li>
<li>1304 - Apple's App Store License Management service is unavailable.  Retry after {0} (UTC).</li>
<li>1328 - The Apple App Store License Management account token is invalid.</li>
<li>1346 - The Apple App Store License Management account token is revoked.</li>
<li>1303 - The Apple's App Store License Management token you are attempting to upload has expired.</li>
<li>1333 - The App Store License Management services returned an unexpected error.</li>
<li>1349 - An unexpected error occurred while communicating with the App Store License Management service (Error: {0}).</li>
</ol>

---
### POST /apple/appleBusinessManager/licenseAccounts/{accountId}/actions/test

**Summary:** Tests the validity of the Automated Device Enrollment account.

**Description:**
Requires the caller to be granted the "Manage Servers and Global Settings" permission.

**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `accountId` (Required): Type: string. Description: The public identifier of App Store Records in MobiControl.

**Responses:**
- **201**:
- **400**: Bad request.
- **401**: Unauthorized.
- **403**: Failed operation due to non-existing account.
- **422**: <ol>
<li> 1340 - The license account is owned by a different MobiControl instance </li>
<li>1304 - Apple's App Store License Management service is unavailable.  Retry after {0} (UTC).</li>
<li>1328 - The Apple App Store License Management account token is invalid.</li>
<li>1346 - The Apple App Store License Management account token is revoked.</li>
<li>1343 - The Apple service cannot be reached.</li>
<li>1303 - The Apple's App Store License Management token you are attempting to upload has expired.</li>
<li>1333 - The App Store License Management services returned an unexpected error.</li>
<li>1349 - An unexpected error occurred while communicating with the App Store License Management service (Error: {0}).</li>
</ol>

---
### GET /apple/appleBusinessManager/licenseAccounts/settings

**Summary:** Returns the settings for App Store License Management.

**Description:**
Requires the caller to be granted the "MobiControl Access" permission.

**(Available Since MobiControl v15.3.0)**

**Responses:**
- **400**: Bad request.
- **401**: Unauthorized.

---

### POST /apple/appleBusinessManager/licenseAccounts/settings

**Summary:** Set settings for App Store License Management.

**Description:**
Requires the caller to be granted the "Manage Servers and Global Settings" permission.

**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `vppSettings` (Required): Type: object. Description: VppSettings.

**Responses:**
- **204**:

---
## Branding

### GET /branding/images/{type}

**Summary:** Returns the Branding image

**Description:** Returns the Branding image
Note: Returns HttpResponseMessage with https code and image-content as content
Requires the caller be granted the "Web Console Access" permission
**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `type` (Required): Type: string. Description: Type of BrandingImage

**Responses:**
- **200**: Success
- **400**: Contract validation failed
- **404**: Resource not found (No image content)

---

### DELETE /branding/images/{type}

**Summary:** Deletes the Branding image

**Description:** Deletes the specified Branding image
Requires the caller be granted the "Manage Servers and Global Settings" permission.
**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `type` (Required): Type: string. Description: Type of BrandingImage.

**Responses:**
- **204**: Operation Successful
- **400**: Contract validation failed
- **401**: Unauthorized access
- **403**: Forbidden
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:<br /><ol><li>7100 - Custom logo deletion not allowed</li></ol>

---

### PUT /branding/images/{type}

**Summary:** Updates the Branding image

**Description:**
Uploads an image that can be used in different Portals for branding. This also supports replacing the existing image.
Requires the caller be granted the "Manage Servers and Global Settings" permission.
**(Available Since MobiControl v15.4.0)**

Uploads an image that can be used in different Portals for branding. It will Upload an image or Update in case an image alrady exists.

Content-Type of the Request body must be <code>multipart/related; boundary={any boundary identifier}</code>
Boundary length must be set to less than or equal to 11 to prevent internal server errors.
Multipart request body must contain the following parts:
- image metadata - Contains json-formatted image information with Content-Type:
image/jpeg.metadata+json```
- image file - Contains Base64 or encoded binary image file with Content-Type:
image/jpeg```

Allowed Content type for images (image/png, image/gif, image/jpg, image/jpeg)  Optional headers
Content-Type-Encoding: base64 or binary
Content-Disposition: attachment; filename="{image-filename}"

Currently, the maximum size of image file to be uploaded when using this endpoint is <u>1 MB</u>.

The example below shows image upload request.

Content-Type: multipart/related; boundary=foo_bar_baz Content-Length: number_of_bytes_in_entire_request_body
--foo_bar_baz Content-Type: image/jpeg.metadata+json
              --foo_bar_baz Content-Type: image/jpeg Content-Transfer-Encoding: Binary Content-Disposition: attachment; filename="image_file_name.jpeg"
Binary-encoded image data --foo_bar_baz--```



**Parameters:**
- `type` (Required): Type: string. Description: Type of BrandingImage

**Responses:**
- **201**: Image uploaded successfully
- **400**: Contract validation failed ie. Invalid image or file contents or metadata
- **401**: Unauthorized access
- **403**: Forbidden
- **415**: Unsupported content media type

---
## Catalogue Item Management

### GET /security/principal/catalogueItems/{referenceId}/rights

**Summary:** Returns the permissions for the specified catalogue item.

**Description:** Returns the permissions allocated to the catalogue item referred to by referenceId. These catalogue items can be users, user groups or roles.

Requires the caller be granted the 'Manage Console Security' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference identifier.

**Responses:**
- **200**: Successfully returns permissions for the specified catalogue item.
- **400**: Contract validation failed.
- **403**: Forbidden.

---

### PUT /security/principal/catalogueItems/{referenceId}/rights

**Summary:** Updates the permissions for the specified catalogue item.

**Description:** Updates the permissions allocated to the catalogue item referred to by referenceId. These catalogue items can be users, user groups or roles.

Requires the caller be granted the 'Manage Console Security' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference id of the catalogue item.
- `userRights` (Required): Type: object. Description: The user rights.

**Responses:**
- **200**: Successfully returns permissions.
- **400**: Contract validation failed.
- **403**: Forbidden.

---
### GET /security/principal/catalogueItems/{referenceId}/currentUserRights

**Summary:** Get permissions from the permission catalogue item for the current user.

**Description:** This API retrieves all permissions from the permission catalogue item for the current user specified by its Reference Id.

Requires the caller be granted the "Web Console Access" permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id of catalogue item, which could be that of a user, directory or role.

**Responses:**
- **200**: Successfully returns right associated with a Catalogue Item for current user.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><li>6512: Insufficient view permission</li>

---
## Certificate Management

### POST /certificateManagement/certificationAuthorities/adcsDcom

**Summary:** Creates a new ADCS PKI DCOM Certification Authority.

**Description:** Creates a new ADCS PKI DCOM Certification Authority.

**(Available Since MobiControl v15.3.0)**
Requires the caller be granted the "Manage Certificate Authorities" permission.

**Parameters:**
- `certificationAuthority` (Required): Type: object. Description: The certification authority object.

**Responses:**
- **200**: Action executed successfully.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.

---
### POST /certificateManagement/certificationAuthorities/adcsHttps

**Summary:** Creates a new ADCS PKI HTTPS Certification Authority.

**Description:** Creates a new ADCS PKI HTTPS Certification Authority

**(Available Since MobiControl v15.3.0)**
Requires the caller be granted the "Manage Certificate Authorities" permission.

**Parameters:**
- `certificationAuthority` (Required): Type: object. Description: The certification authority object.

**Responses:**
- **200**: Action executed successfully.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.

---
### POST /certificateManagement/certificationAuthorities/adcsScep

**Summary:** Creates a new ADCS SCEP Certification Authority.

**Description:** Creates a new ADCS SCEP Certification Authority.

**(Available Since MobiControl v15.3.0)**
Requires the caller be granted the "Manage Certificate Authorities" permission.

**Parameters:**
- `certificationAuthority` (Required): Type: object. Description: The certification authority object.

**Responses:**
- **200**: Action executed successfully.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.

---
### POST /certificateManagement/certificationAuthorities/{referenceId}/certificateTemplates

**Summary:** Creates a new certificate template.

**Description:** Creates a new certificate template to the certification authority specified by "ReferenceID".

**(Available Since MobiControl v15.3.0)**
Requires the caller be granted the "Manage Certificate Authorities" permission.

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference ID of the certification authority.
- `certificateTemplate` (Required): Type: object. Description: The certificate template object.

**Responses:**
- **200**: Action executed successfully.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.

---

### GET /certificateManagement/certificationAuthorities/{referenceId}/certificateTemplates

**Summary:** Returns the certificate templates for the specified certification authority.

**Description:** Returns certificate templates for the certification authority specified by "ReferenceID".

**(Available Since MobiControl v15.3.0)**
Requires the caller be grated the "WebConsole Access" permission.

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference ID of the certification authority.

**Responses:**
- **403**: Unauthorized access.

---
### POST /certificateManagement/certificationAuthorities/entrust

**Summary:** Creates a new Entrust Certification Authority.

**Description:** Creates a new Entrust Certification Authority.

**(Available Since MobiControl v15.3.0)**
Requires the caller be granted the "Manage Certificate Authorities" permission.

**Parameters:**
- `certificationAuthority` (Required): Type: object. Description: The certification authority object.

**Responses:**
- **200**: Action executed successfully.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.

---
### POST /certificateManagement/certificationAuthorities/scep

**Summary:** Creates a new Generic SCEP Certification Authority.

**Description:** Creates a new Generic SCEP Certification Authority.

**(Available Since MobiControl v15.3.0)**
Requires the caller be granted the "Manage Certificate Authorities" permission.

**Parameters:**
- `certificationAuthority` (Required): Type: object. Description: The certification authority object.

**Responses:**
- **200**: Action executed successfully.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.

---
### POST /certificateManagement/certificationAuthorities/symantec

**Summary:** Creates a new Symantec Certification Authority.

**Description:** Creates new Symantec Certification Authority

**(Available Since MobiControl v15.3.0)**
Requires the caller be granted the "Manage Certificate Authorities" permission.

**Parameters:**
- `certificationAuthority` (Required): Type: object. Description: The certification authority object.

**Responses:**
- **200**: Action executed successfully.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.

---
### POST /certificateManagement/certificationAuthorities/ejbcaEst

**Summary:** Creates a new EJBCA EST Certification Authority.

**Description:** Creates new EJBCA EST Certification Authority

**(Available Since MobiControl v2024.0.0)**
Requires the caller be granted the "Manage Certificate Authorities" permission.

**Parameters:**
- `certificationAuthority` (Required): Type: object. Description: The certification authority object.

**Responses:**
- **200**: Action executed successfully.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.

---
### DELETE /certificateManagement/certificationAuthorities/{referenceId}/certificateTemplates/{certificateTemplateReferenceId}

**Summary:** Deletes the specified certificate template.

**Description:** Deletes a certificate template from the certification authority specified by "ReferenceID". The certificate template to be deleted is provided by the "CertificateTemplateReferenceID".

**(Available Since MobiControl v15.3.0)**
Requires the caller be granted the "Manage Certificate Authorities" permission.

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference ID of the certification authority.
- `certificateTemplateReferenceId` (Required): Type: string. Description: The reference ID of the certificate template.

**Responses:**
- **204**: Certification Authority deleted.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>3506 - Certificate template has references in a profile and cannot be deleted</li></ol>

---

### PUT /certificateManagement/certificationAuthorities/{referenceId}/certificateTemplates/{certificateTemplateReferenceId}

**Summary:** Updates the specified certificate template.

**Description:** Updates an existing certificate template for a certification authority specified by the "ReferenceID". The certificate template to be updated is specified by the "CertificateTemplateReferenceID".

**(Available Since MobiControl v15.3.0)**
Requires the caller be granted the "Manage Certificate Authorities" permission.

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference ID of the certification authority.
- `certificateTemplateReferenceId` (Required): Type: string. Description: The reference ID of the certificate template.
- `certificateTemplate` (Required): Type: object. Description: The certificate template object.

**Responses:**
- **400**: Invalid request.
- **403**: Unauthorized access.

---
### DELETE /certificateManagement/certificationAuthorities/{referenceId}

**Summary:** Deletes the specified certification authority.

**Description:** Deletes the certification authority specified by "ReferenceID".

**(Available Since MobiControl v15.3.0)**
Requires the caller be granted the "Manage Certificate Authorities" permission.

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference ID of the certification authority.

**Responses:**
- **204**: Certification Authority deleted.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.

---

### GET /certificateManagement/certificationAuthorities/{referenceId}

**Summary:** Returns the specified certification authority.

**Description:** Returns the certification authority referenced by "ReferenceID"

**(Available Since MobiControl v15.3.0)**
Requires the caller be grated the "WebConsole Access" permission.

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference ID of the certification authority.

**Responses:**
- **403**: Unauthorized access.

---
### DELETE /certificateManagement/extendedKeyUsage

**Summary:** Deletes the specified Extended Key Usage entry.

**Description:** Deletes Extended Key Usage entry specified by "EkuEntry".

**(Available Since MobiControl v15.3.0)**
Requires the caller be granted the "Manage Certificate Authorities" permission.

**Parameters:**
- `ekuEntry` (Required): Type: object. Description: The Extended Key Entry to delete.

**Responses:**
- **204**: Certification Authority deleted.
- **400**: Invalid request.
- **401**: Unauthorized.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>3508 - Extended Key Entry has references in certificate templates and cannot be deleted.</li><li>3509 - Cannot delete system generated Extended Key Usage entry.</li></ol>

---

### GET /certificateManagement/extendedKeyUsage

**Summary:** Returns a list of Extended Key Usage entries.

**Description:** Returns all Extended Key Usage entries.

**(Available Since MobiControl v15.3.0)**
Requires the caller be grated the "WebConsole Access" permission.

**Responses:**
- **200**: Response Contract.

---

### POST /certificateManagement/extendedKeyUsage

**Summary:** Creates a new Extended Key Usage entry.

**Description:** Creates a new Extended Key Usage entry.

**(Available Since MobiControl v15.3.0)**
Requires the caller be granted the "Manage Certificate Authorities" permission.

**Parameters:**
- `ekuEntry` (Required): Type: object. Description: The Extended Key Entry to create.

**Responses:**
- **400**: Bad Request.

---

### PUT /certificateManagement/extendedKeyUsage

**Summary:** Updates the specified Extended Key Usage entry.

**Description:** Updates an existing Extended Key Usage entry.

**(Available Since MobiControl v15.3.0)**
Requires the caller be granted the "Manage Certificate Authorities" permission.

**Parameters:**
- `ekuEntry` (Required): Type: object. Description: The Extended Key Entry to update.

**Responses:**
- **400**: Invalid request.
- **403**: Unauthorized access.

---
### GET /certificateManagement/certificationAuthorities/symantecCertificateRequest

**Summary:** Returns a Symantec Certificate Signing Request.

**Description:** Returns a certificate signing request (CSR) for a Symantec Certification Authority. This CSR can then be used to generate an RA certificate on Symantec's PKI Manager.

**(Available Since MobiControl v15.3.0)**
Requires the caller be granted the "Manage Certificate Authorities" permission.

**Responses:**
- **403**: Unauthorized access.

---
### POST /certificateManagement/certificationAuthorities/{referenceId}/symantecCertificate

**Summary:** Upload Symantec certificate.

**Description:** Creates a new Symantec P7B certificate for a certification authority specified by "ReferenceID".

Content-Type of the request body must be multipart/related; boundary={boundary identifier}.


         Boundary length must be set to less than or equal to 11 to prevent internal server errors.



Multipart body request must contain the following parts:


         --&lt;boundary&gt;
         Content-Type: application/x-pkcs7-certificates.metadata+json
         {"filename": "&lt;filename&gt;"}


         --&lt;boundary&gt;
         Content-Type: application/x-pkcs7-certificates
         Content-Transfer-Encoding: base64
         Content-Disposition: attachment; filename="&lt;filename&gt;"
         &lt;base64 representation of the certificate file&gt;


         --&lt;boundary&gt;
         ```


**(Available Since MobiControl v15.3.0)**
Requires the caller be granted the "Manage Certificate Authorities" permission.

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference ID of the certification authority.

**Responses:**
- **403**: Unauthorized access.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>3507 - The uploaded .p7b file does not match the last created Certificate Signing Request (CSR). Please generate a new CSR and try again.</li></ol>

---
### POST /certificateManagement/certificationAuthorities/{referenceId}/adcsRootCertificate

**Summary:** Upload ADCS Root certificate.

**Description:** Creates a new ADCS Root certificate for a certification authority, specified by "ReferenceID".

Content-Type of the request body must be multipart/related; boundary={boundary identifier}.


         Boundary length must be set to less than or equal to 11 to prevent internal server errors.



Multipart body request must contain the following parts:


         --&lt;boundary&gt;
         Content-Type: application/pkix-cert+json
         {"filename": "&lt;filename&gt;"}


         --&lt;boundary&gt;
         Content-Type: application/pkix-cert
         Content-Transfer-Encoding: base64
         Content-Disposition: attachment; filename="&lt;filename&gt;"
         &lt;base64 representation of the certificate file&gt;


         --&lt;boundary&gt;
         ```


**(Available Since MobiControl v15.3.0)**
Requires the caller be granted the "Manage Certificate Authorities" permission.

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference ID of the certification authority.

**Responses:**
- **403**: Unauthorized access.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>3510 - MobiControl does not support multiple certificate PFX files. Please create a separate PFX file for each certificate if you want all to be installed on the device.</li><li>3511 - Certificate does not have a private key.</li><li>3512 - File is not a valid certificate.</li><li>3513 - Invalid certificate password specified.</li><li>3514 - The provided certificate is invalid because it has expired.</li></ol>

---
### POST /certificateManagement/certificationAuthorities/{referenceId}/adcsEnrollmentCertificate

**Summary:** Upload ADCS Enrolment certificate.

**Description:** Creates a new ADCS Enrollment Certificate for a certification authority, specified by "ReferenceID".

Content-Type of the request body must be multipart/related; boundary={boundary identifier}.


         Boundary length must be set to less than or equal to 11 to prevent internal server errors.



Multipart body request must contain the following parts:


         --&lt;boundary&gt;
         Content-Type: application/x-pkcs12.metadata+json
         {"filename": "&lt;filename&gt;", "password": "&lt;password&gt;"}


         --&lt;boundary&gt;
         Content-Type: application/x-pkcs12
         Content-Transfer-Encoding: base64
         Content-Disposition: attachment; filename="&lt;filename&gt;"
         &lt;base64 representation of the certificate file&gt;


         --&lt;boundary&gt;
         ```


**(Available Since MobiControl v15.3.0)**
Requires the caller be granted the "Manage Certificate Authorities" permission.

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference ID of the certification authority.

**Responses:**
- **403**: Unauthorized access.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>3510 - MobiControl does not support multiple certificate PFX files. Please create a separate PFX file for each certificate if you want all to be installed on the device.</li><li>3511 - Certificate does not have a private key.</li><li>3512 - File is not a valid certificate.</li><li>3513 - Invalid certificate password specified.</li><li>3514 - The provided certificate is invalid because it has expired.</li></ol>

---
### POST /certificateManagement/certificationAuthorities/{referenceId}/adcsAuthenticationCredential

**Summary:** Upload ADCS Authentication Credential certificate.

**Description:** Creates a new ADCS Authentication Credential certificate for a certification authority, specified by "ReferenceID".

Content-Type of the request body must be multipart/related; boundary={boundary identifier}.


         Boundary length must be set to less than or equal to 11 to prevent internal server errors.



Multipart body request must contain the following parts:


         --&lt;boundary&gt;
         Content-Type: application/x-pkcs12.metadata+json
         {"filename": "&lt;filename&gt;", "password": "&lt;password&gt;"}


         --&lt;boundary&gt;
         Content-Type: application/x-pkcs12
         Content-Transfer-Encoding: base64
         Content-Disposition: attachment; filename="&lt;filename&gt;"
         &lt;base64 representation of the certificate file&gt;


         --&lt;boundary&gt;
         ```


**(Available Since MobiControl v15.3.0)**
Requires the caller be granted the "Manage Certificate Authorities" permission.

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference ID of the certification authority.

**Responses:**
- **403**: Unauthorized access.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>3510 - MobiControl does not support multiple certificate PFX files. Please create a separate PFX file for each certificate if you want all to be installed on the device.</li><li>3511 - Certificate does not have a private key.</li><li>3512 - File is not a valid certificate.</li><li>3513 - Invalid certificate password specified.</li><li>3514 - The provided certificate is invalid because it has expired.</li></ol>

---
### POST /certificateManagement/certificationAuthorities/{referenceId}/ejbcaAuthenticationCredential

**Summary:** Upload EJBCA Authentication Credential certificate.

**Description:** Creates a new EJBCA Authentication Credential certificate for a certification authority, specified by "ReferenceID".

Content-Type of the request body must be multipart/related; boundary={boundary identifier}.


         Boundary length must be set to less than or equal to 11 to prevent internal server errors.



Multipart body request must contain the following parts:


         --&lt;boundary&gt;
         Content-Type: application/x-pkcs12.metadata+json
         {"filename": "&lt;filename&gt;", "password": "&lt;password&gt;"}


         --&lt;boundary&gt;
         Content-Type: application/x-pkcs12
         Content-Transfer-Encoding: base64
         Content-Disposition: attachment; filename="&lt;filename&gt;"
         &lt;base64 representation of the certificate file&gt;


         --&lt;boundary&gt;
         ```


**(Available Since MobiControl v2024.0.0)**
Requires the caller be granted the "Manage Certificate Authorities" permission.

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference ID of the certification authority.

**Responses:**
- **403**: Unauthorized access.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>3511 - Certificate does not have a private key.</li><li>3512 - File is not a valid certificate.</li><li>3513 - Invalid certificate password specified.</li><li>3514 - The provided certificate is invalid because it has expired.</li></ol>

---
### GET /certificateManagement/certificateTemplates

**Summary:** Returns a list of certificate templates.

**Description:** Returns the certificate templates by the provided certificate retrieval method, filtering by certificate authority type.

**(Available Since MobiControl v15.3.0)**
Requires the caller be grated the "WebConsole Access" permission.

**Parameters:**
- `certificationAuthorityTypes`: Type: array. Description: Type of the certificate authority.
- `method`: Type: string. Description: Certificate retrieval method.

**Responses:**
- **200**: Response Contract.

---
### GET /certificateManagement/certificationAuthorities

**Summary:** Returns a list of certification authorities.

**Description:** Returns all certification authorities.

**(Available Since MobiControl v15.3.0)**
Requires the caller be grated the "WebConsole Access" permission.

**Responses:**
- **200**: Response Contract.

---
### PUT /certificateManagement/certificationAuthorities/{referenceId}/adcsDcom

**Summary:** Updates the specified ADCS PKI DCOM Certification Authority.

**Description:** Updates ADCS PKI DCOM Certification Authority.

**(Available Since MobiControl v15.3.0)**
Requires the caller be granted the "Manage Certificate Authorities" permission.

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference ID of the certification authority.
- `certificationAuthority` (Required): Type: object. Description: The certification authority object.

**Responses:**
- **400**: Bad Request.
- **403**: Unauthorized access.

---
### PUT /certificateManagement/certificationAuthorities/{referenceId}/adcsHttps

**Summary:** Updates the specified ADCS PKI HTTPS Certification Authority.

**Description:** Updates the ADCS PKI HTTPS Certification Authority specified by "ReferenceID".

**(Available Since MobiControl v15.3.0)**
Requires the caller be granted the "Manage Certificate Authorities" permission.

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference ID of the certification authority.
- `certificationAuthority` (Required): Type: object. Description: The certification authority object.

**Responses:**
- **400**: Bad Request.
- **403**: Unauthorized access.

---
### PUT /certificateManagement/certificationAuthorities/{referenceId}/adcsScep

**Summary:** Updates the specified ADCS SCEP Certification Authority.

**Description:** Updates an existing ADCS SCEP Certification Authority specified by "ReferenceID".

**(Available Since MobiControl v15.3.0)**
Requires the caller be granted the "Manage Certificate Authorities" permission.

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference ID of the certification authority.
- `certificationAuthority` (Required): Type: object. Description: The certification authority object.

**Responses:**
- **400**: Invalid request.
- **403**: Unauthorized access.

---
### PUT /certificateManagement/certificationAuthorities/{referenceId}/entrust

**Summary:** Updates the specified Entrust Certification Authority.

**Description:** Updates an existing Entrust Certification Authority specified by "ReferenceID".

**(Available Since MobiControl v15.3.0)**
Requires the caller be granted the "Manage Certificate Authorities" permission.

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference ID of the certification authority.
- `certificationAuthority` (Required): Type: object. Description: The certification authority object.

**Responses:**
- **400**: Invalid request.
- **403**: Unauthorized access.

---
### PUT /certificateManagement/certificationAuthorities/{referenceId}/scep

**Summary:** Updates the specified Generic SCEP Certification Authority.

**Description:** Updates an existing Generic SCEP Certification Authority specified by "ReferenceID".

**(Available Since MobiControl v15.3.0)**
Requires the caller be granted the "Manage Certificate Authorities" permission.

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference ID of the certification authority.
- `certificationAuthority` (Required): Type: object. Description: The certification authority object.

**Responses:**
- **400**: Invalid request.
- **403**: Unauthorized access.

---
### PUT /certificateManagement/certificationAuthorities/{referenceId}/symantec

**Summary:** Updates the specified Symantec Certification Authority.

**Description:** Updates an existing Symantec Certification Authority specified by "ReferenceID".

**(Available Since MobiControl v15.3.0)**
Requires the caller be granted the "Manage Certificate Authorities" permission.

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference ID of the certification authority.
- `certificationAuthority` (Required): Type: object. Description: The certification authority object.

**Responses:**
- **400**: Invalid request.
- **403**: Forbidden.

---
### PUT /certificateManagement/certificationAuthorities/{referenceId}/ejbcaEst

**Summary:** Updates the specified EJBCA EST Certification Authority.

**Description:** Updates an existing EJBCA EST Certification Authority specified by "ReferenceID".

**(Available Since MobiControl v2024.0.0)**
Requires the caller be granted the "Manage Certificate Authorities" permission.

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference ID of the certification authority.
- `certificationAuthority` (Required): Type: object. Description: The certification authority object.

**Responses:**
- **400**: Invalid request.
- **403**: Forbidden.

---
## Compliance Policies

### POST /compliancepolicies

**Summary:** Create a new compliance policy

**Description:** Creates a compliance policy as specified. Requires the caller be granted "View Compliance Policies" and "Manage Compliance Policies" permissions.
When the DeviceFamily is iOS, both iOS and macOS devices are included.
**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `policy` (Required): Type: object. Description: Details of compliance policy to be created

**Responses:**
- **200**: New compliance policy created
- **403**: Unauthorized access

---

### GET /compliancepolicies

**Summary:** Retrieve all compliance policies from the server

**Description:** Retrieves all compliance policies from the server. Requires the caller be granted "View Compliance Policies" permission.
**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `families`: Type: array. Description: If specified, return only policies for the selected families.<br />When iOS is selected, both iOS and macOS devices will be targeted.
- `nameContains`: Type: string. Description: If specified, return only policies where the name contains the specified string
- `statuses`: Type: array. Description: If specified, return only policies having the selected status(es)
- `isAssigned`: Type: boolean. Description:
- `order`: Type: string. Description: Defines the sorting order by property. Pass the value as -property for descending, and +property for ascending.
- `skip`: Type: integer. Description: Input the first X (count) entries that should not be returned.
- `take`: Type: integer. Description: Input the number of entries to be returned, after skipping over the 'skip' count.

**Responses:**
- **200**: Returns a list of compliance policies
- **403**: Unauthorized access

---
### DELETE /compliancepolicies/{referenceId}

**Summary:** Delete a compliance policy by reference Id.

**Description:** Delete a compliance policy. Requires the caller be granted "View Compliance Policies" and "Manage Compliance Policies" permissions.
**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference ID of the policy

**Responses:**
- **204**: Policy has been deleted
- **403**: Unauthorized access

---

### GET /compliancepolicies/{referenceId}

**Summary:** Get a single compliance policy by referenceId

**Description:** Retrieves details about a compliance policy. Requires the caller be granted "View Compliance Policies" permission.
When the DeviceFamily is iOS, both iOS and macOS devices are included.
**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference ID of the policy

**Responses:**
- **200**: Policy returned
- **403**: Unauthorized access

---

### PUT /compliancepolicies/{referenceId}

**Summary:** Update an existing compliance policy

**Description:** Updates a compliance policy. Requires the caller be granted "View Compliance Policies" and "Manage Compliance Policies" permissions.
When the DeviceFamily is iOS, both iOS and macOS devices are included.
**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference ID of the policy
- `policy` (Required): Type: object. Description: Details of the updated compliance policy

**Responses:**
- **200**: Policy has been updated
- **403**: Unauthorized access

---
### GET /compliancepolicies/{referenceId}/assignment

**Summary:** Get the assignment information about a compliance policy

**Description:** Get assignment information of a policy. Requires the caller be granted "View Compliance Policies" permission.
**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference ID of the policy

**Responses:**
- **200**: Assignment information has been retrieved
- **403**: Unauthorized access

---

### PUT /compliancepolicies/{referenceId}/assignment

**Summary:** Update the assignment of a compliance policy

**Description:** Updates policy assignment. Requires the caller be granted "View Compliance Policies" and "Manage Compliance Policies" permissions.
**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference ID of the policy
- `assignment` (Required): Type: object. Description: Assignment information

**Responses:**
- **200**: Assignment information has been updated
- **403**: Unauthorized access

---

### DELETE /compliancepolicies/{referenceId}/assignment

**Summary:** Delete the assignment of a compliance policy

**Description:** Deletes policy assignment. Requires the caller be granted "View Compliance Policies" and "Manage Compliance Policies" permissions.
**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference ID of the policy

**Responses:**
- **204**: Assignment information has been deleted
- **403**: Unauthorized access

---
### POST /compliancepolicies/{referenceId}/run

**Summary:** Run specified compliance policy

**Description:** Runs a compliance policy. Requires the caller be granted "View Compliance Policies" and "Manage Compliance Policies" permissions.
**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference ID of the policy

**Responses:**
- **204**:

---
### GET /compliancepolicies/{referenceId}/actions

**Summary:** Get a list of actions associated with this compliance policy

**Description:** Get the list of compliance actions for the policy. Requires the caller be granted "View Compliance Policies"permission.
**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference ID of the policy

**Responses:**
- **200**: Assignment information has been updated
- **403**: Unauthorized access

---

### PUT /compliancepolicies/{referenceId}/actions

**Summary:** Update a list of actions associated with this compliance policy

**Description:** Update the actions to be taken for the compliance policy. Requires the caller be granted "View Compliance Policies" and "Manage Compliance Policies" permissions.
**(Available Since MobiControl v15.1.0)**

Available Action Types:- Set Azure Conditional Access **(Available Since MobiControl v15.5.0)**- Block Email Access- Email Notification

Set Azure Conditional Access action example:

[
{
 "Type": "AzureConditionalAccess",
 "ExecutionDelay": 0,
 "ExecutionDelayUnit": "Hours",
 "ActionInformation": "string",
 "ActionInfoDescriptor": "Na"
}
]```


Block Email Access action example:

[
{
 "Type": "Exchange",
 "ExecutionDelay": 0,
 "ExecutionDelayUnit": "Hours",
 "ActionInformation": "string",
 "ExchangeServerId" : "string"
}
]```


Email Notification action example:

[
{
 "Type": "EmailNotification",
 "RepeatCountInDays": 1,
 "EmailProfileName": "string",
 "Recipients": [
   {
     "Addressee": "To",
     "Email": "user@domain.net"
   }
 ],
 "EmailTemplateReferenceId": "164254a3-b47e-4f68-a82c-af75f551ec27",
 "ExecutionDelay": 0,
 "ExecutionDelayUnit": "Hours",
 "ActionInformation": "user@domain.net"
}
]```


Available recipient addressee types (Addressee):- To- CarbonCopy- BlindCarbonCopy

Available Email template reference Ids (EmailTemplateReferenceId):- 164254A3-B47E-4F68-A82C-AF75F551EC27 : user email template- 6DAD0C7C-DF8B-4378-9F5C-F08E1640404F : administrator email template

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference ID of the policy
- `actions` (Required): Type: object. Description: List of actions to be taken according to the compliance

**Responses:**
- **204**: Assignment information has been updated
- **403**: Unauthorized access

---
### POST /compliancepolicies/{referenceId}/enable

**Summary:** Enable the specified compliance policy

**Description:** Enables the compliance policy. Requires the caller be granted "View Compliance Policies" and "Manage Compliance Policies" permissions.
**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference ID of the policy

**Responses:**
- **204**:

---
### POST /compliancepolicies/{referenceId}/disable

**Summary:** Disable the specified compliance policy

**Description:** Disables the compliance policy. Requires the caller be granted "View Compliance Policies" and "Manage Compliance Policies" permissions.
**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference ID of the policy

**Responses:**
- **204**:

---
### GET /compliancepolicies/{referenceId}/logs

**Summary:** Get compliance policy Logs

**Description:** Returns a list of logs associated with a compliance policy. Requires the caller be granted the "View Compliance Policies" global permission. Ordering is restricted to Timestamp.
**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference Id of the compliance policy
- `logSeverities`: Type: array. Description: Return the logs whose severity matches that from the array
- `startDate`: Type: string. Description: Return the logs whose date is startDate or later
- `endDate`: Type: string. Description: Only return the logs whose date is endDate or before
- `Order`: Type: array.
- `Skip`: Type: integer.
- `Take`: Type: integer.

**Responses:**
- **200**: Returns a list of a logs based on a compliance policy reference id
- **403**: Unauthorized access or compliance policy reference does not exist

---
### GET /compliancepolicies/{referenceId}/logs/summary

**Summary:** Get compliance policy logs summary

**Description:** Returns logs summary associated with a compliance policy. Requires the caller be granted the "View Compliance Policies" global permission.
**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference Id of the compliance policy
- `startDate`: Type: string. Description: Return the logs whose date is startDate or later
- `endDate`: Type: string. Description: Return the logs whose date is endDate or before

**Responses:**
- **200**: Returns a list of a logs based on a compliance policy reference id
- **403**: Unauthorized access or compliance policy reference does not exist

---
## Custom Attributes

### POST /customattributes

**Summary:** Create Custom Attribute

**Description:** Create custom attributes by defining the data type (text, numeric, date, boolean or enumerator), set the value and indicate whether the attribute must be populated on the device.


         Requires the caller be granted the "Manage Servers and Global Setting" permission.

**(Available Since MobiControl v15.0.0)**

**Parameters:**
- `customAttribute` (Required): Type: object. Description: custom attribute

**Responses:**
- **200**:

---

### GET /customattributes

**Summary:** Retrieve List of Custom Attribute Properties

**Description:** Returns a list of Custom Attribute properties and their respective definition. Requires the caller be granted "Web Console Access" permission.

**(Available Since MobiControl v14.0.0)**

**Responses:**
- **200**:

---
### GET /customattributes/{name}

**Summary:** Retrieve an Existing Custom Attribute

**Description:** Retrieve an existing custom attribute by specifying it's name.

**(Available Since MobiControl v15.0.0)**

**Parameters:**
- `name` (Required): Type: string. Description: custom attribute name

**Responses:**
- **200**: Returns existing custom attribute specified by name

---

### PUT /customattributes/{name}

**Summary:** Update an Existing Custom Attribute

**Description:** Update an existing custom attribute by specifying it's name.


         Requires the caller be granted the "Manage Servers and Global Settings" permission.

**(Available Since MobiControl v15.0.0)**

**Parameters:**
- `name` (Required): Type: string. Description:
- `customAttribute` (Required): Type: object. Description: custom attribute

**Responses:**
- **204**:

---

### DELETE /customattributes/{name}

**Summary:** Delete Custom Attribute

**Description:** Delete an existing custom attribute by specifying it's name.


         Requires the caller be granted the "Manage Servers and Global Settings" permission.
**(Available Since MobiControl v15.0.0)**

**Parameters:**
- `name` (Required): Type: string. Description: custom attribute name

**Responses:**
- **204**:

---
### POST /customattributes/{name}/catalogueItemReferenceId

**Summary:** Assign rights to a Custom Attribute.

**Description:** Assign rights associated with a Catalogue Item to a Custom Attribute.


         Requires the caller be granted the "Manage Servers and Global Settings" permission and the right to view the specified Catalogue Item.

**(Available Since MobiControl v15.0.0)**

**Parameters:**
- `name` (Required): Type: string. Description: custom attribute name

**Responses:**
- **204**:

---

### GET /customattributes/{name}/catalogueItemReferenceId

**Summary:** Get the Custom Attribute referenceID.

**Description:** Get the Catalogue Item ReferenceId for a specific Custom Attribute.  Requires the caller to be granted the "WebConsole" global permission and the right to view the specified Catalogue Item.

**(Available Since MobiControl v15.0.0)**

**Parameters:**
- `name` (Required): Type: string. Description: custom attribute name

**Responses:**
- **200**: Returns custom attribute's catalog referenceId

---

### DELETE /customattributes/{name}/catalogueItemReferenceId

**Summary:** Remove rights assigned to a Custom Attribute.

**Description:** Remove rights associated with a Catalogue Item to a Custom Attribute.


         Requires the caller be granted the "Manage Servers and Global Settings" permission and the right to view the specified Catalogue Item.

**(Available Since MobiControl v15.0.0)**

**Parameters:**
- `name` (Required): Type: string. Description: custom attribute name

**Responses:**
- **204**:

---
## Custom Data

### GET /customdata

**Summary:** Retrieve List of Custom Data Properties

**Description:** Returns a list of Custom Data properties and their respective definition. Requires the caller be granted "Web Console Access" permission.


         Note: For "DeviceFamily" in the response, "Blackberry", "Scanner", and "WindowsRuntime" are deprecated. "WindowsPhone" is for all Windows Modern devices.

**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `deviceFamily`: Type: string. Description: Optional. Device Family type.
- `includeBuiltIn`: Type: boolean. Description: Optional. Include build-in custom data

**Responses:**
- **200**:

---

### POST /customdata

**Summary:** Create New Custom Data

**Description:** Creates new Custom Data by specifying the required properties and their respective definition. Requires the caller be granted "Web Console Access" permission.
         A unique name must be given to the Custom Data item being created. There is also limited support for special characters.
         Note: For "DeviceFamily" in the response, "Blackberry", "Scanner", and "WindowsRuntime" are deprecated. "WindowsPhone" is for all Windows Modern devices.

**(Available Since MobiControl v15.0.0)**

**Parameters:**
- `customData` (Required): Type: object. Description: Custom Data

**Responses:**
- **200**:

---
### GET /customdata/{name}

**Summary:** Retrieve Custom Data with Specified Name

**Description:** Retrieves Custom Data by specifying the name. Requires the caller be granted "Web Console Access" permission.
         Note: For "DeviceFamily" in the response, "Blackberry", "Scanner", and "WindowsRuntime" are deprecated. "WindowsPhone" is for all Windows Modern devices.

**(Available Since MobiControl v15.0.0)**

**Parameters:**
- `name` (Required): Type: string. Description: Unique name of custom data

**Responses:**
- **200**:

---

### PUT /customdata/{name}

**Summary:** Update Custom Data Properties

**Description:** Updates Custom Data by specifying the required properties and their respective definition, custom data is located by name. Requires the caller be granted "Web Console Access" permission.
         Note: For "DeviceFamily" in the response, "Blackberry", "Scanner", and "WindowsRuntime" are deprecated. "WindowsPhone" is for all Windows Modern devices.

**(Available Since MobiControl v15.0.0)**

**Parameters:**
- `name` (Required): Type: string. Description: Unique name of custom data
- `customData` (Required): Type: object. Description: Custom Data

**Responses:**
- **200**:

---

### DELETE /customdata/{name}

**Summary:** Delete Custom Data with Specified Name

**Description:** Deletes custom data by specifying the name. Requires the caller be granted "Web Console Access" permission.

**(Available Since MobiControl v15.0.0)**

**Parameters:**
- `name` (Required): Type: string. Description: Unique name of custom data

**Responses:**
- **204**:

---
### GET /customdata/{name}/catalogueItemReferenceId

**Summary:** Get the Custom Data referenceID

**Description:** Get the Catalogue Item ReferenceId for a specific Custom Data item. Requires the caller to be granted the "WebConsole" global permission and the right to view the specified Catalogue Item.

**(Available Since MobiControl v15.0.0)**

**Parameters:**
- `name` (Required): Type: string. Description: Unique name of custom data

**Responses:**
- **200**:

---

### POST /customdata/{name}/catalogueItemReferenceId

**Summary:** Assign Rights to a Custom Data Item

**Description:** Assign rights associated with a Catalogue Item to a Custom Data item. Requires the caller to be granted the "WebConsole" global permission and the right to view the specified Catalogue Item.

**(Available Since MobiControl v15.0.0)**

**Parameters:**
- `name` (Required): Type: string. Description: Unique name of custom data

**Responses:**
- **204**:

---

### DELETE /customdata/{name}/catalogueItemReferenceId

**Summary:** Remove Rights Assigned to a Custom Data Item

**Description:** Remove rights associated with a Catalogue Item to a specific Custom Data item. Requires the caller to be granted the "WebConsole" global permission and the right to view the specified Catalogue Item.

**(Available Since MobiControl v15.0.0)**

**Parameters:**
- `name` (Required): Type: string. Description: Unique name of custom data

**Responses:**
- **204**:

---
## Device Configuration

### GET /devices/{deviceId}/advancedConfigurations

**Summary:** Returns the advanced configurations for the specified device.

**Description:** This API returns the advanced configurations of the specified device.


         Requires the caller to be granted the "Configure Advanced Settings" and "Web Console Access" permission.

**(Available since MobiControl v14.0.0)**


**Parameters:**
- `deviceId` (Required): Type: string. Description: Unique identifier for a device.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **401**: Unauthorized Access.
- **403**: Forbidden.

---
## Device Group App Policy

### GET /devicegroups/{path}/appPolicies

**Summary:** Retrieves details for all application policies assigned to a device group.

**Parameters:**
- `path` (Required): Type: string. Description: The reference ID or the path of the device group. When using reference ID, "referenceId:" must be prepended to the ID value. The path must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company). When using the path, the root of the path must be prepended with "\\". For example: "\\My Company" or "\\My Company\Management Devices".
- `appPolicyFamily`: Type: string. Description: The app policy family.
- `skip`: Type: integer. Description: How many records to skip.
- `take`: Type: integer. Description: How many records to take.

**Responses:**
- **200**: Successfully retrieved app policies for device group &lt;device group name&gt;.
- **400**: Failed to retrieve app policies because of invalid &lt;parameter name&gt;.
- **401**: Unauthorized.
- **403**: Failed to retrieve app policies because you do not have the appropriate permissions. Please speak to your administrator.

---
## Device Groups

### GET /devicegroups

**Summary:** Retrieve a List of Device Groups.

**Description:** Recursively lists all device groups in the system, or the immediate children of a named "parent" device group. Results are limited to where the caller has been granted the "View Groups" permission on a device group. Reference ID was introduced in 14.0.0 as a recommended alternative to using path for identification of a device group.

**(Available Since MobiControl v13.0.0)**

**Parameters:**
- `parentPath`: Type: string. Description: The reference ID or the path of the parent device group. When using reference ID, "referenceId:" must be prepended to the ID value. Path must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).

**Responses:**
- **200**:

---

### POST /devicegroups

**Summary:** Create a Device Group

**Description:** Creates a new device group under a specified path and outputs the created device group information. Reference ID (introduced in 14.0.0) will be generated automatically and should not be included in the request. Virtual groups are supported as of 14.0.0 with an optional a filter using the same syntax as GET /devices/search. Requires the caller be granted "Manage Groups" permission for the specified device group.

**(Available Since MobiControl v13.0.0)**

**Parameters:**
- `deviceGroup` (Required): Type: object. Description: The new device group to create

**Responses:**
- **200**:

---
### GET /devicegroups/{path}

**Summary:** Retrieve a Single Device Group

**Description:** Returns information about a single device group identified by its reference ID or path. Reference ID was introduced in 14.0.0 as a recommended alternative to using path for identification of a device group. Requires the caller be granted the "View Groups" permission for the specified device group.

**(Available Since MobiControl v13.0.0)**

**Parameters:**
- `path` (Required): Type: string. Description: The reference ID or the path of the device group. When using reference ID, "referenceId:" must be prepended to the ID value. Path must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).

**Responses:**
- **200**:

---

### DELETE /devicegroups/{path}

**Summary:** Delete a Device Group

**Description:** Deletes a device group identified by its reference ID or path. Reference ID was introduced in 14.0.0 as a recommended alternative to using path for identification of a device group. Requires the caller be granted "Manage Groups" permission for the specified device group.

**(Available Since MobiControl v13.0.0)**

**Parameters:**
- `path` (Required): Type: string. Description: The reference ID or the path of the device group. When using reference ID, "referenceId:" must be prepended to the ID value. Path must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).

**Responses:**
- **204**:

---
### PUT /devicegroups/{path}/name

**Summary:** Rename a Device Group

**Description:** Renames a device group identified by its reference ID or path. Reference ID was introduced in 14.0.0 as a recommended alternative to using path for identification of a device group. Requires the caller be granted the "View Groups" and "Manage Groups" permissions for the specified path.

**(Available Since MobiControl v13.0.0)**

**Parameters:**
- `path` (Required): Type: string. Description: The reference ID or the path of the device group. When using reference ID, "referenceId:" must be prepended to the ID value. Path must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).
- `newName` (Required): Type: object. Description: The new name for the group. String body parameters must be enclosed in single quotes.

**Responses:**
- **200**:

---
### PUT /devicegroups/{path}/filter

**Summary:** Update a Virtual Group Filter

**Description:** Updates a virtual device group filter identified by its reference ID (recommended) or path. Filter syntax is the same as /devices/search. Requires the caller be granted the "Manage Groups" permission for the specified group.

**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `path` (Required): Type: string. Description: The reference ID or the path of the device group. When using reference ID, "referenceId:" must be prepended to the ID value. Path must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).
- `newFilter` (Required): Type: object. Description: The new filter for the virtual group

**Responses:**
- **200**:

---
### PUT /devicegroups/{path}/path

**Summary:** Move a Device Group

**Description:** Updates the current parent of a device group identified by its reference ID or path. Reference ID was introduced in 14.0.0 as a recommended alternative to using path for identification of a device group. Requires the caller be granted "Manage Groups" permission for the source and destination paths.

**(Available Since MobiControl v13.0.0)**

**Parameters:**
- `path` (Required): Type: string. Description: The reference ID or the path of the device group. When using reference ID, "referenceId:" must be prepended to the ID value. Path must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).
- `newParentPath` (Required): Type: object. Description: The new parent group path. String body parameters must be enclosed in single quotes.

**Responses:**
- **200**:

---
### PUT /devicegroups/{path}/icon

**Summary:** Update a Device Group Icon

**Description:** Updates the icon color of a device group identified by its path and outputs the updated device deviceGroup information.

**(Available Since MobiControl v13.0.0)**

**Parameters:**
- `path` (Required): Type: string. Description: The device group identifier for parent device group taken from Reference ID. Deprecated: Can also be a path of parent device group. Must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).
- `newIcon` (Required): Type: object. Description: The new icon color. Must be enclosed in single quotes.

**Responses:**
- **200**:

---
### PUT /devicegroups/{path}/customAttributes/{customAttributeId}

**Summary:** Update a Single Custom Attribute for a Device Group

**Description:** Updates one custom attribute value for a single device group identified by its reference ID (recommended) or path. Requires the caller be granted the "Edit Custom Attribute Values" permission for the specified device group.

**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `path` (Required): Type: string. Description: The reference ID or the path of the device group. When using reference ID, "referenceId:" must be prepended to the ID value. Path must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).
- `customAttributeId` (Required): Type: string. Description: The name of the custom attribute.
- `customAttributeValue` (Required): Type: object. Description: The new custom attribute value. Use null or empty string to clear the custom attribute. String body parameters must be enclosed in single quotes.

**Responses:**
- **204**:

---

### DELETE /devicegroups/{path}/customAttributes/{customAttributeId}

**Summary:** Clear a Single Custom Attribute for a Device Group

**Description:** Clears a  custom attribute value for a single device group identified by its reference ID (recommended) or path. Requires the caller be granted the "Edit Custom Attribute Values" permission for the specified device group.

**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `path` (Required): Type: string. Description: The reference ID or the path of the device group. When using reference ID, "referenceId:" must be prepended to the ID value. Path must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).
- `customAttributeId` (Required): Type: string. Description: The name of the custom attribute.

**Responses:**
- **204**:

---
### GET /devicegroups/{path}/customAttributes

**Summary:** Retrieve Values of Custom Attributes for a Device Group

**Description:** Returns a list of values for each globally configured custom attribute for a single device group identified by its reference ID (recommended) or path. Requires the caller be granted the "View Groups" permission for the specified device group.

**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `path` (Required): Type: string. Description: The reference ID or the path of the device group. When using reference ID, "referenceId:" must be prepended to the ID value. Path must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).

**Responses:**
- **200**: List of Custom Attribute Info objects

---

### PUT /devicegroups/{path}/customAttributes

**Summary:** Update Multiple Custom Attributes for a Device Group

**Description:** Updates one or more custom attribute values for a single device group identified by its reference ID (recommended) or path. Requires the caller be granted the "Edit Custom Attribute Values" permission for the specified device group.

**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `path` (Required): Type: string. Description: The reference ID or the path of the device group. When using reference ID, "referenceId:" must be prepended to the ID value. Path must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).
- `values` (Required): Type: object. Description: The custom attribute name and value to set a value for.

**Responses:**
- **204**:

---
### POST /devicegroups/{path}/members

**Summary:** Add or Move a Devices to a Device Group

**Description:** Moves one or more devices identified by their device IDs to a device group identified by its reference ID (recommended) or path. In the case the destination is a virtual group, devices will be added to the group rather than moved. Any advanced settings configured for the devices specifically can either be maintained or inherited from the new device group (cleared). Requires the caller be granted the "View Groups" and "Manage Devices" permission for both the source and destination device groups.

**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `path` (Required): Type: string. Description: The reference ID or the path of the device group. When using reference ID, "referenceId:" must be prepended to the ID value. Path must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).
- `deviceIds` (Required): Type: object. Description: Array of device identifiers
- `clearConfigurations`: Type: boolean. Description: Clear any advanced setting/configuration values on the device(s) when moving and inherit these values from the new parent group

**Responses:**
- **204**:

---
### POST /devicegroups/{path}/members/remove

**Summary:** Remove Devices From a Virtual Group

**Description:** Removes one or more devices identified by their device IDs from a virtual group identified by its reference ID (recommended) or path. Not applicable to virtual groups with filter criteria. Requires the caller be granted the "View Groups" and "Manage Devices" permission for both the source and destination device groups.

**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `path` (Required): Type: string. Description: The reference ID or the path of the device group. When using reference ID, "referenceId:" must be prepended to the ID value. Path must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).
- `deviceIds` (Required): Type: object. Description: Array of device identifiers

**Responses:**
- **204**:

---
### GET /devicegroups/{path}/members/lastKnownLocation

**Summary:** Retrieve Last Known Locations of Devices From a Device Group

**Description:** Returns a list of last known location values for each device in device group. Requires the caller be granted the "View Groups" permission for the specified device group.

**(Available Since MobiControl v15.0.0)**

**Parameters:**
- `path` (Required): Type: string. Description: The reference ID or the path of the device group. When using reference ID, "referenceId:" must be prepended to the ID value. Path must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).
- `viewRectLimits`: Type: string. Description: Comma separated string representing Top, Left, Bottom and Right Coordinates of the current view rectangle.
         There must be exactly 4 values, in a correct range:
         Top/Bottom, representing Latitude, should be in [-90, 90] when Bottom is less then Top.
         Left/Right, representing Longitude, should be in [-180, 180].
         For example:
             "86,-140,-32,112"

**Responses:**
- **200**: List of DeviceLocation objects

---
### GET /devicegroups/{path}/members/locationStatuses

**Summary:** Get Status of Location Action for Devices From a Device Group

**Description:** Returns a BulkDeviceLocationActionStatus class with the number of devices which succeeded, failed or pending location in device group. Requires the caller be granted the "View Groups" permission for the specified device group.

**(Available Since MobiControl v15.0.0)**

**Parameters:**
- `path` (Required): Type: string. Description: The reference ID or the path of the device group. When using reference ID, "referenceId:" must be prepended to the ID value. Path must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).
- `includeSubgroups`: Type: boolean. Description: Indicates that action should be executed on devices in all descendant groups (subgroups would be available since MVP2)

**Responses:**
- **200**: BulkDeviceLocationActionStatus objects

---
### POST /devicegroups/{path}/members/actions

**Summary:** Send Actions to Devices Within a Group

**Description:** Sends actions to all devices within a single device group identified by its reference ID (recommended) or path. Requires the caller be granted the permission for the respective action on the specified device group. Refer to  GET /deviceschema for the parameters of each supported action.

**(Available Since MobiControl v14.0.0)**

Supported actions:
         - Checkin - Requests the device to communicate with the server and update its information- Disable - Disconnects a device from the MobiControl deployment server. Disconnected devices will not receive configuration changes or updates from MobiControl until they are re-enabled- DisableAgentUpgrade - Prevent devices from upgrading their agent at the next scheduled or manually requested checkin- EnableAgentUpgrade - Allow devices to upgrade their agent at the next scheduled or manually requested checkin- Locate - Request the device to send its current location- Lock - Request the device return to the lock screen and in some cases display a message- SendMessage - Sends a message to the MobiControl agent that is displayed to the active user- SendScript - Sends a script to the device to be executed immediately upon receiving it- SendScriptViaPns - Sends a script via Platform Notification Service. (Android Plus only)- SendScriptViaSms - Sends a script via SMS, long scripts will be separated and sent in multiple messages- SoftReset - Performs device soft reset- SyncFilesNow - Sync files now- ResetPasscode - Reset the passcode on the target Android or Android+ device.- UpgradeAgentNow - Upgrade agent immediately if the agent has already enabled for upgrade

**Parameters:**
- `path` (Required): Type: string. Description: The reference ID or the path of the device group. When using reference ID, "referenceId:" must be prepended to the ID value. Path must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).
- `actionInfo` (Required): Type: object. Description: The action and its respective parameters.

**Responses:**
- **204**:

---
### POST /devicegroups/{path}/members/actions/v2

**Summary:** Send Actions to Devices Within a Group

**Description:** Sends actions to all devices within a single device group identified by its reference ID (recommended) or path (devices can also be filtered by search criteria). Requires the caller be granted the permission for the respective action on the specified device group. Refer to  GET /deviceschema for the parameters of each supported action.

**(Available Since MobiControl v15.0.0)**

Supported actions:
         - Checkin - Requests the device to communicate with the server and update its information- Disable - Disconnects a device from the MobiControl deployment server. Disconnected devices will not receive configuration changes or updates from MobiControl until they are re-enabled- DisableAgentUpgrade - Prevent devices from upgrading their agent at the next scheduled or manually requested checkin- EnableAgentUpgrade - Allow devices to upgrade their agent at the next scheduled or manually requested checkin- Locate - Request the device to send its current location- Lock - Request the device return to the lock screen and in some cases display a message- SendMessage - Sends a message to the MobiControl agent that is displayed to the active user- SendScript - Sends a script to the device to be executed immediately upon receiving it- SendScriptViaPns - Sends a script via Platform Notification Service. (Android Plus only)- SendScriptViaSms - Sends a script via SMS, long scripts will be separated and sent in multiple messages- SoftReset - Performs device soft reset- SyncFilesNow - Sync files now- ResetPasscode - Reset the passcode on the target Android or Android+ device.- UpgradeAgentNow - Upgrade agent immediately if the agent has already enabled for upgrade

**Parameters:**
- `path` (Required): Type: string. Description: The reference ID or the path of the device group. When using reference ID, "referenceId:" must be prepended to the ID value. Path must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).
- `groupAction` (Required): Type: object. Description: The action and filter for device search.
- `includeSubgroups`: Type: boolean. Description: If action should be executed on devices in all descendant groups

**Responses:**
- **204**:

---
### GET /devicegroups/{path}/advancedSettings

**Summary:** Retrieve Advanced Settings for a Device Group

**Description:** Returns a list of the advanced settings and respective configuration status for a single device group identified by its reference ID (recommended)  or path.
         Requires the caller be granted the "View Groups" permission for the specified device group.

**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `path` (Required): Type: string. Description: The reference ID or the path of the device group.
         <br />When using a reference ID, it must be prepended to the ID value, "referenceId:" (e.g. referenceId%3A7e39724b-6120-4c1f-96a8-c04d4570a974).
         <br />Path must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).

**Responses:**
- **200**:

---

### DELETE /devicegroups/{path}/advancedSettings

**Summary:** Clear All Advanced Configuration Settings from the Target Group

**Description:** This reverts the device group configurations to their default values,
         which is either inherited from a parent group, a system-wide setting, or not configured.

**(Available Since MobiControl v14.1.0)**

**Parameters:**
- `path` (Required): Type: string. Description: The reference ID or the path of the device group.
         <br />When using a reference ID, it must be prepended to the ID value, "referenceId:" (e.g. referenceId%3A7e39724b-6120-4c1f-96a8-c04d4570a974).
         <br />Path must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).

**Responses:**
- **204**:

---
### GET /devicegroups/{path}/notes

**Summary:** Retrieve Notes for a Device Group

**Description:** Returns a list of notes for a single device group identified by its reference ID (recommended) or path.

**(Available Since MobiControl v14.0.1)**

**Parameters:**
- `path` (Required): Type: string. Description: The device group identifier for parent device group taken from Reference ID. Deprecated: Can also be a path of parent device group. Must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).

**Responses:**
- **200**:

---

### POST /devicegroups/{path}/notes

**Summary:** Create a Note

**Description:** Creates a new device group note under a specified group reference ID (recommended) or path and outputs the created note’s information.
         Requires the caller be granted the “Manage Notes” permission for the group.

**(Available Since MobiControl v14.0.3)**

**Parameters:**
- `path` (Required): Type: string. Description: The group path or reference ID.
- `note` (Required): Type: object. Description: The note object

**Responses:**
- **200**:

---
### GET /devicegroups/{path}/members/notes

**Summary:** Retrieves Notes from Member Devices of a Group

**Description:** Returns a list of notes for all devices that are members of the requested group, as well as members of the subgroups of the requested group.

**(Available Since MobiControl v14.0.3)**

**Parameters:**
- `path` (Required): Type: string. Description:

**Responses:**
- **200**:

---
### PUT /devicegroups/{path}/notes/{referenceId}

**Summary:** Update a Note

**Description:** Updates the note for a device group identified by its reference ID (recommended) or path and outputs the updated note’s information.
         Requires the caller be granted the “Manage Notes” permission for the group.

**(Available Since MobiControl v14.0.3)**

**Parameters:**
- `path` (Required): Type: string. Description: The group path or referenceId
- `referenceId` (Required): Type: string. Description: The note reference identifier
- `note` (Required): Type: object. Description: The note object

**Responses:**
- **200**:

---

### DELETE /devicegroups/{path}/notes/{referenceId}

**Summary:** Delete a Note

**Description:** Deletes a note for a device group identified by its reference ID (recommended) or path.
         Requires the caller be granted the “Manage Notes” permission for the group.

**(Available Since MobiControl v14.0.3)**

**Parameters:**
- `path` (Required): Type: string. Description: The group path
- `referenceId` (Required): Type: string. Description: The note identifier

**Responses:**
- **204**:

---
### POST /devicegroups/{referenceId}/actions/setgroupwallpaper

**Summary:** Set Wallpaper for Group

**Description:** Uploads and sets the wallpaper of all devices in a given device group, only executing actions against supported and compatible devices. Requires the caller be granted the "Set Wallpaper" permission on the specified device group.

**(Available Since MobiControl v14.2.2)**


          Content-Type of the Request body must be <code>multipart/related; boundary={boundary identifier}</code>

          Boundary length must be set to less than or equal to 11 to prevent internal server errors.


          Multipart request body must contain the following parts:
- action metadata - Contains json-formatted information with Content-Type:
application/vnd.soti.mobicontrol.setwallpaperaction.metadata+json```
Contains reference id of device group
{"ReferenceId":["string"]}```
- image file for Lock screen wallpaper - Contains Base64 encoded binary image file with Content-Type: <code>image/jpeg</code> or <code>image/png</code>

          Content-Type-Encoding: base64

          Content-Disposition: form-data; name="LockScreenFile"; filename="string"
- image file for Home screen wallpaper - Contains Base64 encoded binary image file with Content-Type: image/jpeg or image/png

          Content-Type-Encoding: base64

          Content-Disposition: form-data; name="HomeScreenFile"; filename="string"

          Currently, the maximum size of image file when using this endpoint is <u>5 MB</u>.



          The example below shows SetWallpaper group level action request.



          Content-Type: multipart/related; boundary=foo_bar_baz
          Content-Length: number_of_bytes_in_entire_request_body


          --foo_bar_baz
          Content-Type: application/vnd.soti.mobicontrol.setwallpaperaction.metadata+json


          {
          "ReferenceId" : "referenceid:123456"
          }


          --foo_bar_baz
          Content-Type: image/jpeg
          Content-Type-Encoding: base64
          Content-Disposition: form-data; name="LockScreenFile"; filename="some_image.jpg"


          Base64-encoded image data
          --foo_bar_baz--
          ```
**Cannot execute this API as file upload not supported from this documentation page.**

**Parameters:**
- `referenceId` (Required): Type: string. Description: the group path
- `includeSubgroups`: Type: boolean. Description:

**Responses:**
- **204**:

---
### DELETE /devicegroups/{path}/advancedConfiguration/{configurationName}/{deviceFamily}

**Summary:** Delete AdvancedConfiguration

**Parameters:**
- `path` (Required): Type: string. Description: The reference ID or the path of the device group.
         <br />When using a reference ID, it must be prepended to the ID value, "referenceId:" (e.g. referenceId%3A7e39724b-6120-4c1f-96a8-c04d4570a974).
         <br />Path must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).
- `configurationName` (Required): Type: string. Description: Only delete Device Groups Advanced Configuration that is targeting to the given configuration name (e.g. AndroidPlusAgentSettings)
- `deviceFamily` (Required): Type: string. Description: Only delete Device Groups Advanced Configuration that is targeting to the given device family (e.g. AndroidPlus)

**Responses:**
- **204**:

---
## Device Kind Schema

### GET /deviceschema

**Summary:** Retrieve Device Action Schema for All Device Kinds

**Description:** Returns a definition of actions including their supported parameters that are applicable to each respective device kind. Requires the caller be granted the "Web Console Access" permission.
**(Available Since MobiControl v14.0.0)**

**Responses:**
- **200**: A collection of "DeviceKindSchema"

---
### GET /deviceschema/{deviceKind}

**Summary:** Retrieve Device Action Schema for a Single Device Kind

**Description:** Returns a definition of actions including their supported parameters that are applicable to a single device kind. Requires the caller be granted the "Web Console Access" permission.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `deviceKind` (Required): Type: string. Description: The device kind

**Responses:**
- **200**: The schema for the specified kind

---
### GET /deviceschema/{deviceKind}/configurations

**Summary:** Retrieve Device Advanced Configuration Schema for a Single Device Kind

**Description:** Returns the advanced configurations that are applicable to a specific device kind. Requires the caller be granted the "Web Console Access" permission.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `deviceKind` (Required): Type: string. Description: The kind to retrieve configuration metadata for
- `advancedOnly`: Type: boolean. Description: Whether to return advanced configurations only

**Responses:**
- **200**: All configurations for the specified kind, filtered as specified

---
## Device Script

### GET /deviceScripts/type

**Summary:** Gets metadata of all device scripts of selected types currently saved on the system. (Defaults to Legacy type if not defined).

**Description:** Requires the caller be granted the 'View Device Scripts' permission.

         If no type is provided, it will default to Legacy.
**(Available Since MobiControl v2024.0.0)**

**Parameters:**
- `scriptTypes`: Type: array. Description: script search type filter.

**Responses:**
- **200**: Success.
- **403**: Forbidden.

---
### GET /deviceScripts/{referenceId}

**Summary:** Gets a specific device script.

**Description:** Requires the caller be granted the 'View Device Scripts' permission.
**(Available Since MobiControl v2024.0.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The device script's reference ID.

**Responses:**
- **200**: Success.
- **400**: Bad Request.
- **403**: Forbidden.

---

### PUT /deviceScripts/{referenceId}

**Summary:** Updates a specified device script.

**Description:** Requires the caller be granted the 'Manage Device Scripts' permission.
**(Available Since MobiControl v2024.0.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The device script's reference ID.
- `content` (Required): Type: object. Description: The new content for the device script (in quotes). Max size 10MB.

**Responses:**
- **204**: No Content.
- **400**: Bad Request.
- **403**: Forbidden.
- **413**: Content Too Large.

---

### DELETE /deviceScripts/{referenceId}

**Summary:** Delete a specified device script.

**Description:** Requires the caller be granted the 'Manage Device Scripts' permission.

         Will only allow deletion if no other features (profiles, policies, etc.) are currently using the script.
**(Available Since MobiControl v2024.0.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The device script's reference ID.

**Responses:**
- **204**: No Content.
- **400**: Bad Request.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>[8000] : Specified script with Id {reference ID} cannot be deleted as there are still features using it.</li></ol>

---
### POST /deviceScripts

**Summary:** Add a new device script to the System.

**Description:** Requires the caller be granted the 'Manage Device Scripts' permission.

         If an existing script has the same name as the new script, by default it will not be added.

         However, if replaceExisting is set to true, it will return the same reference ID as the old script that was replaced.

**(Available Since MobiControl v2024.0.0)**

**Parameters:**
- `newScript` (Required): Type: object. Description: The new device script object. Max size 10MB.
- `replaceExisting`: Type: boolean. Description: If there is a device script saved in the system with the same name, should this device script replace replace it? (Defaults to false).

**Responses:**
- **200**: Success.
- **400**: Bad Request.
- **413**: Content Too Large.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>[8001] : Cannot add device script with name {name} since one with that name already exists.</li><li>[8002] : Cannot add device script with name {0} since special characters like \, /, *, ?, ", :, &lt;, &gt;, and | are not allowed.</li></ol>

---
## Device Script Execution Status

### GET /devices/{deviceId}/scriptStatus/executionStatus

**Parameters:**
- `deviceId` (Required): Type: string.

**Responses:**
- **200**:

---
### GET /devices/{deviceId}/scriptStatus

**Parameters:**
- `deviceId` (Required): Type: string.
- `sourceTypes`: Type: array.
- `startDate`: Type: string.
- `endDate`: Type: string.
- `orderBy`: Type: string.
- `orderByDesc`: Type: boolean.
- `skip`: Type: integer.
- `take`: Type: integer.

**Responses:**
- **200**:

---
### GET /devices/{deviceId}/scriptStatus/scriptOrigins

**Parameters:**
- `deviceId` (Required): Type: string.

**Responses:**
- **200**:

---
### GET /devices/{deviceId}/scriptStatus/{deviceScriptExecutionReferenceId}/scriptContent

**Parameters:**
- `deviceId` (Required): Type: string.
- `deviceScriptExecutionReferenceId` (Required): Type: string.

**Responses:**
- **200**:

---
### GET /devices/{deviceId}/scriptStatus/{deviceScriptExecutionReferenceId}/scriptOutput

**Parameters:**
- `deviceId` (Required): Type: string.
- `deviceScriptExecutionReferenceId` (Required): Type: string.

**Responses:**
- **200**:

---
### POST /devices/{deviceId}/scriptStatus/{deviceScriptExecutionReferenceId}/scriptOutput/actions/request

**Parameters:**
- `deviceId` (Required): Type: string.
- `deviceScriptExecutionReferenceId` (Required): Type: string.

**Responses:**
- **204**:

---
## Devices

### GET /devices/{deviceId}

**Summary:** Retrieve Single Device

**Description:** Returns a single device identified by its device ID, or the device's MAC address when deviceId is prefixed with "mac:". Requires the caller be granted "View Group" permission on the parent device group where the device resides. The device object is polymorphic in that extended properties specific to the device "Kind" will be returned in addition to those listed here. For the complete list properties for each kind, please refer to the online help.
Note: For "DeviceFamily" in the response, "Blackberry", "Scanner", and "WindowsRuntime" are deprecated. "WindowsPhone" is for all Windows Modern devices.
**(Available Since MobiControl v13.0.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier

**Responses:**
- **200**:

---

### DELETE /devices/{deviceId}

**Summary:** Delete Device

**Description:** Delete a device identified by its device ID, or the device's MAC/IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. A request for the device to unenroll is also made. Requires the caller be granted the "Manage Devices" permission.
**(Available Since MobiControl v13.0.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier

**Responses:**
- **204**:

---
### GET /devices

**Summary:** Retrieve List of Devices

**Description:** Returns a list of devices. If devices ids are specified (in a comma separated list), then no other parameters must be supplied. If no device ids are specified, then a list of all devices will be returned, or the devices found in the specified device group. "Skip" allows for you to define from what point you would like devices to be returned (i.e. if you are only interested devices 40 onward, you would list skip as 39). "Take" is equal to the number of results you would like to be returned. Results are limited to devices residing in device groups where the caller has been granted the "View Groups" permission. The device object is polymorphic in that extended properties, specific to the device "Kind", will be returned in addition to those listed here. For the complete list of properties for each kind, please refer to the online help.
Note: For "DeviceFamily" in the response, "Blackberry", "Scanner", and "WindowsRuntime" are deprecated. "WindowsPhone" is for all Windows Modern devices.
**(Available Since MobiControl v13.0.0)**

**Parameters:**
- `path`: Type: string. Description: The reference ID or the path of the device group. When using reference ID, "referenceId:" must be prepended to the ID value. Path of the parent device group. Must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company)
- `filter`: Type: string. Description: Filter string. Format: Property1:Value1,Property2:Value2
- `userFilter`: Type: string. Description: User filter string. Format: UserName:user or UserId:Id
- `ids`: Type: string. Description: Comma separated list of devices ids
- `order`: Type: string. Description: Defines the sorting order by property. Pass the value as -property for descending, and +property for ascending.
- `skip`: Type: integer. Description: Input the first X (count) entries that should not be returned.
- `take`: Type: integer. Description: Input the number of entries to be returned, after skipping over the 'skip' count.

**Responses:**
- **200**:

---
### POST /devices/summary

**Summary:** Retrieve Summary of Devices

**Description:** Returns a summary count of devices with a unique property value within devices that match the given filter criteria. For example, a count of unique model numbers. Use aggregates to obtain a unique count of model numbers of each unique device family. Add a filter to obtain counts of only a subset of devices. Results will be limited to where the caller has been granted the "View Groups" permission. Refer to the online help for details on the filter syntax.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `aggregationRequests` (Required): Type: object. Description: The aggregation requests
- `groupPath`: Type: string. Description: The reference ID or the path of the parent device group. When using reference ID, "referenceId:" must be prepended to the ID value. The path of the parent group. Must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company)
- `filter`: Type: string. Description: The device filter
- `includeSubgroups`: Type: boolean. Description: When group path is specified, determines whether descendant groups should also be included

**Responses:**
- **200**: The aggregated device summary

---
### GET /devices/search

**Summary:** Retrieve List of Devices Matching Filter Criteria

**Description:** Returns a list of devices matching the specified filter criteria, or all devices. Results will be limited to where the caller has been granted the "View Groups" permission. The device object is polymorphic in that properties specific to the device "Kind" will be returned in addition to the base properties applicable to all devices. Refer to the online help for details on the filter syntax.
Note: For "DeviceFamily" in the response, "Blackberry", "Scanner", and "WindowsRuntime" are deprecated. "WindowsPhone" is for all Windows Modern devices.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `groupPath`: Type: string. Description: The group path. The reference ID or the path of the device group. When using reference ID, "referenceId:" must be prepended to the ID value. Must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).
- `filter`: Type: string. Description: Filter string. Must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).<br />The following operators for searching on date and time are deprecated in 14.3.0 and they will be retired in 15.0.0.<ol><li> = equal </li><li> &lt;&gt; not equal </li><li> &gt; greater than </li><li> &lt; less than </li></ol>
- `includeSubgroups`: Type: boolean. Description: When group path is specified, determines whether descendant groups should also be included
- `verifyAndSync`: Type: boolean. Description: When set to true, search results will be compared with up-to-date information and synchronized with Search service if differences are noticed
- `order`: Type: string. Description: Defines the sorting order by property. Pass the value as -property for descending, and +property for ascending.
- `skip`: Type: integer. Description: Input the first X (count) entries that should not be returned.
- `take`: Type: integer. Description: Input the number of entries to be returned, after skipping over the 'skip' count.

**Responses:**
- **200**:

---
### GET /devices/{deviceId}/collectedData

**Summary:** Retrieve Collected Data for a Device

**Description:** Returns collected data of a particular type for a device identified by its device ID, or the device's MAC address when deviceId is prefixed with "mac:". Collected data is a polymorphic object in that different properties are returned depending on the requested type. Where a collected data type is not applicable to a device it will be treated as if there is no data collected.
**(Available Since MobiControl v13.0.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier
- `startDate` (Required): Type: string. Description: The start date. Example: 2015-12-19T16:39:57-02:00
- `endDate` (Required): Type: string. Description: The end date. Example: 2015-12-19T16:39:57-02:00
- `builtInDataType`: Type: string. Description:
- `customDataType`: Type: string. Description:
- `dataRetrievalOptions`: Type: object. Description: Data retrieval options
- `includeTotalCount`: Type: boolean. Description: Flag to include total no of entries in the response header.

**Responses:**
- **200**:

---
### GET /devices/collectedData

**Summary:** Retrieve Collected Data in Bulk

**Description:** Returns collected data of a particular type for all devices. Collected data is a polymorphic object in that different properties are returned depending on the requested type. Where a collected data type is not applicable to a device it will be treated as if there is no data collected.

**(Available Since MobiControl v13.3.0)**

**Parameters:**
- `startDate` (Required): Type: string. Description: The start date. Example: 2015-12-19T16:39:57-02:00
- `endDate` (Required): Type: string. Description: The end date. Example: 2015-12-19T16:39:57-02:00
- `builtInDataType`: Type: string. Description: Built-in device collected data type. Mutually exclusive
         with customDataType.
- `customDataType`: Type: string. Description: Custom data type. Mutually exclusive with builtInDataType.
- `path`: Type: string. Description: The reference ID or the path of the parent device group. When using reference ID, "referenceId:" must be prepended to the ID value. Path of the parent device group. Must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company). If null, applies to ALL devices
- `skip`: Type: integer. Description: The number of entries to skip. 0 by default
- `take`: Type: integer. Description: The number of entries to take. 50 by default

**Responses:**
- **200**:

---
### GET /devices/{deviceId}/installedApplications

**Summary:** Retrieve Installed Applications for a Device

**Description:** Returns a list of applications that are installed on a device identified by its device ID, or the device's MAC address when deviceId is prefixed with "mac:". Pagination, ordering and filtering parameters are available.
**(Available Since MobiControl v13.0.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier
- `filter`: Type: string. Description: filter for the return list
- `order`: Type: string. Description: Defines the sorting order by property. Pass the value as -property for descending, and +property for ascending.
- `skip`: Type: integer. Description: Input the first X (count) entries that should not be returned.
- `take`: Type: integer. Description: Input the number of entries to be returned, after skipping over the 'skip' count.

**Responses:**
- **200**:

---
### GET /devices/{deviceId}/provisioningProfiles

**Summary:** Retrieve Provisioning Profiles for a Device

**Description:** Returns a list of profiles that are provisioned on a device identified by its device ID, or the device's MAC address when deviceId is prefixed with "mac:". Pagination, ordering and filtering parameters are available.
**(Available Since MobiControl v14.1.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier
- `filter`: Type: string. Description: filter for the return list
- `order`: Type: string. Description: Defines the sorting order by property. Pass the value as -property for descending, and +property for ascending.
- `skip`: Type: integer. Description: Input the first X (count) entries that should not be returned.
- `take`: Type: integer. Description: Input the number of entries to be returned, after skipping over the 'skip' count.

**Responses:**
- **200**:

---
### POST /devices/{deviceId}/installedApplications/{applicationId}/actions

**Summary:** Perform a Device Specific Application Action

**Description:** Executes an action against an application installed on a device. Device can be identified by its device ID, or the device's MAC / IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. Requires the caller to be granted the "Manage Devices" Device Group permission on the device's parent device group.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier
- `applicationId` (Required): Type: string. Description: The application identifier
- `installedApplicationAction` (Required): Type: object. Description: The installed application action

**Responses:**
- **204**:

---
### POST /devices/compatibility

**Summary:** Determine Action Compatibility for Devices

**Description:** Returns a list of compatible and incompatible devices for a given action. Compatibility criteria is based on available rights and device support (ie: OS Version, Kind of device, etc.) Devices can be identified by their device IDs, or the device's MAC / IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. Use this method to exclude incompatible.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `actionInfo` (Required): Type: object. Description: The details of the action and devices to check

**Responses:**
- **200**: A report containing list of compatible and accessible device ids, list of the incompatible devices count by device kind, list of the compatible but non-accassible fro current user devices count by device kind

---
### POST /devices/compatibility/actionContext

**Summary:** Determine Action Compatibility for Devices

**Description:** Returns a list of compatible and incompatible devices for a given action. Compatibility criteria is based on available rights and device support (ie: OS Version, Kind of device, etc.) Devices can be identified by their device IDs, or the device's MAC / IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. Use this method to exclude incompatible.
**(Available Since MobiControl v14.1.2)**

**Parameters:**
- `actionInfo` (Required): Type: object. Description: The details of the action and devices to check

**Responses:**
- **200**: A report containing list of compatible and accessible device ids, list of the incompatible devices count by device kind, list of the compatible but non-accassible fro current user devices count by device kind

---
### POST /devices/{deviceId}/actions

**Summary:** Send Actions to a Device

**Description:** Sends an action to a single device identified by its device ID, or the device's MAC / IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. Requires the caller be granted the permission for the respective action on the device's parent device group. Refer to GET /deviceschema and POST /devices/compatibility for the parameters of each action, its applicability to a given device and to verify the device's compatibility prior to execution. Only execute actions against supported and compatible devices.
**(Available Since MobiControl v13.0.0)**

Supported Actions:- AdsInstallPlugIns - Installs or updates plugin for an Android device- AllowExchangeAccess - Allow device to access Exchange server through the Enterprise Resource Gateway- AllowSotiSurf - Allow device to access content delivered through the SOTI Surf application- AppleSoftwareUpdateRefreshStatus - Request the Apple device to refresh OS update status- AppleSoftwareUpdateScan - Request the Apple device to send a list of available OS updates- AppleSoftwareUpdateSchedule - Request the Apple device to update the OS- BlockExchangeAccess - Allow device to access exchange server through the Enterprise Resource Gateway- BlockSotiHub - Block Access to SOTI Hub- BlockSotiSurf - Block Access to SOTI Surf- BypassActivationLock - Bypasses activation lock on the device- CheckIn - Requests the device to communicate with the server and update its information- ClearRestrictions - Clears the restrictions password and restrictions set by the user on the device- ClearSotiSurfCache - Clear SOTI Surf cache- Disable - Disconnects a device from the MobiControl deployment server. Disconnected devices will not receive configuration changes or updates from MobiControl until they are re-enabled- DisableAgentUpgrade - Prevent devices from upgrading their agent at the next scheduled or manually requested checkin - DisableLostMode - Disable Lost Mode on device- DisablePasscodeLock - Disable passcode on the device- EnableAgentUpgrade - Allow devices to upgrade their agent at the next scheduled or manually requested checkin- EnableLostMode - Enable Lost Mode on the device- FactoryReset - Performs device factory reset- Locate - Request the device to send its current location- Lock - Request the device return to the lock screen and in some cases display a message- MigrateToELMAgent - Migrate MobiControl agent on Samsung devices to the ELM agent- ResetPasscode - Reset the passcode on the target Android or Android+ device.- RemoteRing - Ask the phone to ring to locate it- ScanForViruses - Scan for virus on the device- SyncFilesNow - Sync files now- SendMessage - Sends a message to the MobiControl agent that is displayed to the active user- SoftReset - Performs device soft reset- SendScript - Sends a script to the device to be executed immediately upon receiving it- SendScriptViaSms - Sends a script via SMS, long scripts will be separated and sent in multiple messages- SendScriptViaPns - Sends a script via Platform Notification Service. (Android Plus only)- SendTestPage - Print test page on the device- TurnOffSuspend - Requests the device to turnoff or enter suspended state- Unenroll - Request the device remove its management configuration, all organization information, and return to an unmanaged state- UpdateVirusDefinition - Request the device to update its virus definitions- UpgradeAgentNow - Upgrade agent immediately if the agent has already enabled for upgrade- Wipe - Request a complete erase of the device and restore it to factory defaults- UpdateLicense - Update the License- PlaySound - Play sound on the device- SharedDeviceLogout - Logs the current user out of a shared device- SharedDeviceTroubleshoot - Attempts to resolve any issue experienced by a shared device during the login or logout process- AppFeedbackUpdate - Request the Android device to upload a report containing any changes in its app status to Google Play Server- DisableAdminMode - To enter user mode (Android only). Corresponding device action in the MobiControl Web Console: "Enter User Mode"- EnableAdminMode - To enter admin mode (Android only). Corresponding device action in the MobiControl Web Console: "Enter Admin Mode"- DisableKioskMode - To disable kiosk screen (Android, Windows CE, Windows Desktop Classic only). Corresponding device action in the MobiControl Web Console: "Disable Kiosk Screen"- EnableKioskMode - To enable kiosk screen (Android, Windows CE, Windows Desktop Classic only). Corresponding device action in the MobiControl Web Console: "Enable Kiosk Screen"- SharedIpadUserLogout - To force the current user to log out from a shared iPad.(iOS shared iPad only). Corresponding device action in the MobiControl Web Console: "Log Out Shared iPad"

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier
- `actionInfo` (Required): Type: object. Description: The action to be performed on the device. Some actions allow extra parameters.

**Responses:**
- **204**:

---
### POST /devices/actions

**Summary:** Send Actions to Devices

**Description:** Sends an action to multiple devices identified by their device IDs, or the device's MAC / IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. Requires the caller be granted the permission for the respective action on the device's parent device group. Refer to GET /deviceschema and POST /devices/compatibility for the parameters of each action, its applicability to a given device and to verify the device's compatibility prior to execution. Only execute actions against supported and compatible devices. Refer to POST /devices/{deviceId}/actions for supported actions. Note not all actions may be executed against multiple devices.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `bulkActionInfo` (Required): Type: object. Description: Array of devices ids plus the action to be performed on the device. Some actions allow extra parameters.

**Responses:**
- **204**:

---
### PUT /devices/{deviceId}/parentPath

**Summary:** Move Device

**Description:** Relocates a device identified by its device ID, or the device's MAC address when deviceId is prefixed with "mac:" to the specified device group. Requires the caller be granted the "View Group" permission on the source and destination device group.
**(Available Since MobiControl v13.0.0 &amp; Deprecated in v14.0.0 in favor of POST /devicegroups/{path}/members)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier
- `newPath` (Required): Type: object. Description: The reference ID or the path of the device group. When using reference ID, "referenceId:" must be prepended to the ID value. The path where the device should be moved. String body parameters must be enclosed in single quotes.

**Responses:**
- **200**:

---
### PUT /devices/{deviceId}/passcode

**Summary:** Set/Clear Device Passcode

**Description:** Sets or clears the passcode of a device identified by its device ID, or the device's MAC address when deviceId is prefixed with "mac:". Setting a passcode is supported on Android, Android+, Windows Mobile/CE/Desktop, and will otherwise be ignored. Clearing a passcode is supported on iOS. On Windows Phone a new passcode is generated and displayed in the device log in the MobiControl administration console. Requires the caller be granted the "Manage Devices" permission.
If the request is executed correctly, the return code will be 204.
**(Available Since MobiControl v13.0.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier
- `passcode` (Required): Type: object. Description: The new passcode. String body parameters must be enclosed in single quotes.

**Responses:**
- **204**:

---
### POST /devices/customAttributes/upload

**Summary:** Update the Values of Multiple Custom Attributes against Multiple Devices

**Description:** Uploads and sets the Custom Attribute values for multiple devices as identified by their device ID. If the file format and request are acceptable, this API will always return OK, with a list of devices that failed assignment in the body of the response.
**Note:** Duplicate entries (same ID, same attribute name) will result in the last specified value being taken instead of the earlier ones
**(Available Since MobiControl v14.2.0)**

Content-Type of the Request body must be <code>multipart/form-data; boundary={boundary identifier}; </code>
Boundary length must be set to less than or equal to 11 to prevent internal server errors.
Multipart request body must contain the following parts:
Content-Transfer-Encoding of the Request body must be either <code>binary</code> or <code>base64</code>
- file with assignment entries - Contains text encoded file with Content-Type: <code>application/vnd.ms-excel</code>
Content-Disposition: form-data; name="string"; filename="string"


The example below shows set device users request.

Content-Type: multipart/related; boundary=--foo_bar_baz Content-Length: number_of_bytes_in_entire_request_body
--foo_bar_baz Content-Disposition: form-data; name="attributes"; filename="custom_attributes.csv" Content-Transfer-Encoding: Binary Content-Type: application/vnd.ms-excel
text of file --foo_bar_baz```


**Responses:**
- **200**:

---
### PUT /devices/{deviceId}/customAttributes/{customAttributeId}

**Summary:** Update the Value of a Device Custom Attribute

**Description:** Sets or clears the custom attribute of a device identified by its device ID, or the device's MAC address when deviceId is prefixed with "mac:".
Caller must have the “Edit Custom Attribute Values” permission for the device group where the device resides. If the request is executed correctly, the return code will be 204.
**(Available Since MobiControl v13.1.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier
- `customAttributeId` (Required): Type: string. Description: The custom attribute identifier
- `customAttributeValue` (Required): Type: object. Description: The new custom attribute value. Use null to clear the custom attribute. String body parameters must be enclosed in single quotes

**Responses:**
- **204**:

---

### DELETE /devices/{deviceId}/customAttributes/{customAttributeId}

**Summary:** Clear a Single Custom Attribute for a Device

**Description:** Clears a  custom attribute value for a single device identified by its device ID, or the device's MAC / IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. Requires the caller be granted the "Edit Custom Attribute Values" permission for the specified device group.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The target device identifier
- `customAttributeId` (Required): Type: string. Description: The name of the target custom attribute

**Responses:**
- **204**:

---
### PUT /devices/{deviceId}/customAttributes

**Summary:** Update Multiple Custom Attributes for a Device

**Description:** Updates one or more custom attribute values for a single device identified by its device ID, or the device's MAC / IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. Requires the caller be granted the "Edit Custom Attribute Values" permission on the device's parent device group.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The target device identifier
- `values` (Required): Type: object. Description: The new attribute values to set

**Responses:**
- **200**:

---

### GET /devices/{deviceId}/customAttributes

**Summary:** Retrieve Values of Custom Attributes for a Device

**Description:** Returns a list of values for each globally configured custom attribute for a single device identified by its device ID, or the device's MAC / IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. Requires the caller be granted the "View Groups" permission on the device's parent device group.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier

**Responses:**
- **200**: The list of custom atributes that apply to the specified device

---
### GET /devices/{deviceId}/profiles

**Summary:** Retrieve Profiles Associated with a Device

**Description:** Returns the profiles, including the contained payloads and respective statuses, that are associated to a device identified by its device ID, or the device's MAC/IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. Requires the caller be granted the "View Devices" permission on the parent device group where the device resides.
**(Available Since MobiControl v13.2.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier

**Responses:**
- **200**: A list of all device profiles that are currently associated with the given device.

---
### GET /devices/{deviceId}/PackageInstallationInfo

**Summary:** Get the Order of Installation for Packages on a Device

**Description:** Returns the package installation order for a specific device identified by its device ID, or the device's MAC address when deviceId is prefixed with "mac:".
**(Available Since MobiControl v14.2.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier

**Responses:**
- **200**:

---
### GET /devices/{deviceId}/rules

**Summary:** Retrieve Rules Associated with a Device

**Description:** Returns all the MobiControl rules related to a device identified by its device ID, or the device's MAC / IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. Requires the caller be granted the "View Groups" permission on the device's parent device group.
Note: For "DeviceFamily" in the response, "Blackberry", "Scanner", and "WindowsRuntime" are deprecated. "WindowsPhone" is for all Windows Modern devices.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier

**Responses:**
- **200**:

---
### GET /devices/{deviceId}/appPolicies

**Summary:** Retrieve App Policies Associated with a Device

**Description:** Returns all the MobiControl app policies related to a device identified by its device ID, or the device's MAC / IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. Requires the caller be granted the "View Groups" permission on the device's parent device group.
**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier

**Responses:**
- **200**:

---
### POST /devices/{deviceId}/profiles/{profileId}/actions

**Summary:** Perform Device Specific Profile Actions

**Description:** Installs or revokes a profile for the specified device, instead of all devices assigned the profile. Revoked profiles can be reinstalled using the "install" command, but only by an administrator. The "Administratively Removed" status is synonymous of a profile revoked at the device level. Requires the caller be granted "Manage Devices" permission on the parent device group where the device resides.
**(Available Since MobiControl v13.2.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier
- `profileId` (Required): Type: string. Description: The profile reference ID
- `action` (Required): Type: object. Description: The action to perform, accepted values are: 'install' and 'revoke'

**Responses:**
- **204**:

---
### POST /devices/{deviceId}/profiles/{profileId}/{userName}/actions

**Summary:** Perform Device Specific Profile Actions

**Description:** Installs or revokes a profile for the specified device, instead of all devices assigned the profile. Revoked profiles can be reinstalled using the "install" command, but only by an administrator. The "Administratively Removed" status is synonymous of a profile revoked at the device level. Requires the caller be granted "Manage Devices" permission on the parent device group where the device resides.
**(Available Since MobiControl v13.2.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier
- `profileId` (Required): Type: string. Description: The profile reference ID
- `userName` (Required): Type: string. Description: Apple user name
- `action` (Required): Type: object. Description: The action to perform, accepted values are: 'install' and 'revoke'

**Responses:**
- **204**:

---
### POST /devices/{deviceId}/profiles/{profileId}/packages/{packageId}/{version}/actions

**Summary:** Perform a Device Specific Package Action

**Description:** Executes an action against a package assigned and/or installed on a device. Device can be identified by its device ID, or the device's MAC / IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. Requires the caller be granted the "Manage Devices" permission on the device's parent device group.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier
- `profileId` (Required): Type: string. Description: The profile reference identifier
- `packageId` (Required): Type: string. Description: The package reference identifier
- `version` (Required): Type: string. Description: The version of the package
- `action` (Required): Type: object. Description: The action to perform. Accepted value is: 'reinstall'

**Responses:**
- **204**:

---
### GET /devices/{deviceId}/support

**Summary:** Retrieve the Support Contact Information for a Device

**Description:** Returns the support contact information for a device identified by its device ID, or the devices's MAC address when deviceId is prefixed with "mac:". Requires the caller be granted "Manage Devices" permission on the parent device group where the device resides.
**(Available Since MobiControl v13.3.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier

**Responses:**
- **200**: The support contact information for the given device

---
### GET /devices/{deviceId}/certificates

**Summary:** Retrieve Certificates Associated to a Device

**Description:** Returns certificates issued and/or installed to a device identified by its device ID, or the device's MAC / IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. Requires the caller be granted the "View Groups" permission on the device's parent device group.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier

**Responses:**
- **200**: Device certificates

---
### POST /devices/{deviceId}/certificates/{referenceId}/actions

**Summary:** Perform a Device Specific Certificate Action

**Description:** Executes an action against a certificate issued to a device. Device can be identified by its device ID, or the device's MAC / IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. Requires the caller be granted the "Manage Devices" permission on the device's parent device group.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier
- `referenceId` (Required): Type: string. Description: Certificate identifier of the certificate
- `action` (Required): Type: object. Description: Certificate action for the device

**Responses:**
- **204**:

---
### GET /devices/{deviceId}/quarantine

**Summary:** Retrieves Files Quarantined on a Device

**Description:** Returns files quarantined on a device by the anti-virus/malware engine. Device can be identified by its device ID, or the device's MAC / IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. Requires the caller be granted the "View Groups" permission on the device's parent device group.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier

**Responses:**
- **200**: Device quarantine items, files and applications

---
### POST /devices/{deviceId}/user

**Summary:** Set User for a Device

**Description:** Sets the current user of a device to a known Directory or IDP User. Device can be identified by its device ID, or the device's MAC / IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. The user specified must be a known-valid LDAP or IDP user, no validation will be performed on association. Use GET /directories/{directoryConnectionName}/entries to obtain the user information. LDAP user information will be synchronized per the "LDAP Refresh Interval". Requires the caller be granted the "Manage Devices" permission on the device's parent device group.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The target device identifier
- `connectionName` (Required): Type: string. Description: The Directory or IdentityProvider connection that this user originates from. Input SsoEntity GUID for Identity Provider connection
- `user` (Required): Type: object. Description: The Directory or IdentityProvider user to set as the device user
- `type`: Type: string. Description: Connection type. Leave black to select Directory

**Responses:**
- **204**:

---

### DELETE /devices/{deviceId}/user

**Summary:** Delete User for a Device

**Description:** Delete users from device.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The target device identifier

**Responses:**
- **204**:

---
### POST /devices/deviceUsers

**Summary:** Set Users for Multiple Devices

**Description:** Uploads and sets the device user for multiple devices as identified by their device ID. If the file format and request are acceptable, this API will always return OK, with a list of devices that failed assignment in the body of the response
**(Available Since MobiControl v14.2.0)**

Content-Type of the Request body must be <code>multipart/form-data; boundary={boundary identifier}; </code>
Boundary length must be set to less than or equal to 11 to prevent internal server errors.
Multipart request body must contain the following parts:
- file with assignment entries - Contains text encoded file with Content-Type: <code>application/vnd.ms-excel</code>
Content-Disposition: <code>form-data; name="string"; filename="string"</code>
Content-Transfer-Encoding: <code>binary</code> or <code>base64</code>

The example below shows set device users request.

Content-Type: multipart/related; boundary=--foo_bar_baz Content-Length: number_of_bytes_in_entire_request_body
--foo_bar_baz Content-Disposition: form-data; name="userdetails"; filename="tester.csv" Content-Transfer-Encoding: binary Content-Type: application/vnd.ms-excel
text of file --foo_bar_baz```


**Responses:**
- **200**:

---
### GET /devices/{deviceId}/healthAttestation

**Summary:** Retrieve Attestation Information for a Device

**Description:** Returns Windows Health Attestation information for a single device identified by its device ID, or the device's MAC / IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. Requires the caller be granted the "View Groups" permission on the device's parent device group.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier

**Responses:**
- **406**:
- **200**:

---
### GET /devices/{deviceId}/tpmVersions

**Summary:** Get Windows Modern TPM Specification Versions for the Given Device

**Description:** Returns the TPM versions from a Windows Modern device identified by its device ID.
**(Available Since MobiControl v14.2.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier

**Responses:**
- **406**:
- **200**: TPM version object

---
### GET /devices/{deviceId}/appleDepInfo

**Summary:** Returns information about the device's Automated Device Enrollment configuration.

**Description:** Returns Automated Device Enrollment information for a single device identified by its device ID, or the device's MAC or IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. Requires the caller be granted the "View Groups" permission on the device's parent device group.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier

**Responses:**
- **406**:
- **200**:

---
### GET /devices/{deviceId}/appleVppInfo

**Summary:** Returns information about the device's usage of App Store License accounts.

**Description:** Returns information about the usage of App Store License accounts for a single device identified by its device ID, or the device's MAC or IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. Requires the caller be granted the "View Groups" permission on the device's parent device group.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier

**Responses:**
- **200**:

---
### GET /devices/{deviceId}/contentFiles

**Summary:** Retrieve Content Library for a Device

**Description:** Returns files assigned to a device through Content Library. Device can be identified by its device ID, or the device's MAC / IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. Requires the caller be granted the "View Groups" permission on the device's parent device group.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier

**Responses:**
- **200**:

---
### POST /devices/{deviceId}/actions/generateUnlockCode

**Summary:** Generate Bypass Activation Lock Code

**Description:** Returns a code that can be used to bypass Activation Lock for a device identified by its device ID, or the device's MAC / IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. Refer to GET /deviceschema and POST /devices/compatibility for the applicability of the action to a given device and to verify the device's compatibility prior to execution. Only execute actions against supported and compatible devices. Requires the caller be granted the "Bypass Activation Lock" permission on the device's parent device group.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier
- `requestCode` (Required): Type: object. Description: The request code for unlock

**Responses:**
- **200**:

---
### POST /devices/{deviceId}/actions/setwallpaper

**Summary:** Set Device Wallpaper for a Device

**Description:** Uploads and sets the wallpaper of a device identified by its device ID, or the device's MAC / IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. Refer to GET /deviceschema and POST /devices/compatibility for the applicability of the action to a given device and to verify the device's compatibility prior to execution. Only execute actions against supported and compatible devices. Requires the caller be granted the "Set Wallpaper" permission on the device's parent device group.
**(Available Since MobiControl v14.0.0)**

Content-Type of the Request body must be <code>multipart/related; boundary={boundary identifier}</code>
Boundary length must be set to less than or equal to 11 to prevent internal server errors.
Multipart request body must contain the following parts:
- action metadata - Contains json-formatted information with Content-Type:
application/vnd.soti.mobicontrol.setwallpaperaction.metadata+json```
Contains single device ID collection that should match device ID provided in URL
{"DeviceIds":["string"]}```
- image file for Lock screen wallpaper - Contains Binary or Base64 encoded binary image file with Content-Type: <code>image/jpeg</code> or <code>image/png</code>
Content-Transfer-Encoding: base64 or binary
Content-Disposition: form-data; name="LockScreenFile"; filename="string"
- image file for Home screen wallpaper - Contains Binary or Base64 encoded binary image file with Content-Type: image/jpeg or image/png
Content-Transfer-Encoding: base64 or binary
Content-Disposition: form-data; name="HomeScreenFile"; filename="string"
Currently, the maximum size of image file when using this endpoint is <u>5 MB</u>.

The example below shows SetWallpaper action request.

Content-Type: multipart/related; boundary=foo_bar_baz Content-Length: number_of_bytes_in_entire_request_body
--foo_bar_baz Content-Type: application/vnd.soti.mobicontrol.setwallpaperaction.metadata+json
{ "DeviceIds" : "123456" }
--foo_bar_baz Content-Type: image/jpeg Content-Transfer-Encoding: Base64 Content-Disposition: form-data; name="LockScreenFile"; filename="some_image.jpg"
Base64-encoded image data --foo_bar_baz--```
**Cannot execute this API as file upload not supported from this documentation page.**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier

**Responses:**
- **204**: Success
- **400**: Bad request, ie. Invalid file contents or metadata
- **401**: Unauthorized
- **415**: Unsupported content media type
- **422**: Compatibility failure, Invalid file type, Image size is over 5MB

---
### POST /devices/actions/setwallpaper

**Summary:** Set Device Wallpaper for Devices

**Description:** Uploads and sets the wallpaper of multiple devices identified by their device IDs, or the device's MAC / IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. Refer to GET /deviceschema and POST /devices/compatibility for the applicability of the action to a given device and to verify the device's compatibility prior to execution. Only execute actions against supported and compatible devices. Requires the caller be granted the "Set Wallpaper" permission on the device's parent device group.
**(Available Since MobiControl v14.0.0)**

Content-Type of the Request body must be <code>multipart/related; boundary={boundary identifier}</code>
Boundary length must be set to less than or equal to 11 to prevent internal server errors.
Multipart request body must contain the following parts:
- action metadata - Contains json-formatted information with Content-Type:
application/vnd.soti.mobicontrol.setwallpaperaction.metadata+json```
Contains collection of device IDs
{"DeviceIds":["string"]}```
- image file for Lock screen wallpaper - Contains Binary or Base64 encoded binary image file with Content-Type: <code>image/jpeg</code> or <code>image/png</code>
Content-Transfer-Encoding: base64 or binary
Content-Disposition: form-data; name="LockScreenFile"; filename="string"
- image file for Home screen wallpaper - Contains Binary or Base64 encoded binary image file with Content-Type: image/jpeg or image/png
Content-Transfer-Encoding: base64 or binary
Content-Disposition: form-data; name="HomeScreenFile"; filename="string"
Currently, the maximum size of image file when using this endpoint is <u>5 MB</u>.

The example below shows SetWallpaper action request.

Content-Type: multipart/related; boundary=foo_bar_baz Content-Length: number_of_bytes_in_entire_request_body
--foo_bar_baz Content-Type: application/vnd.soti.mobicontrol.setwallpaperaction.metadata+json
{ "DeviceIds" : "123456" }
--foo_bar_baz Content-Type: image/jpeg Content-Transfer-Encoding: Base64 Content-Disposition: form-data; name="LockScreenFile"; filename="some_image.jpg"
Base64-encoded image data --foo_bar_baz--```
**Cannot execute this API as file upload not supported from this documentation page.**

**Responses:**
- **204**: Success
- **400**: Bad request, ie. Invalid file contents or metadata
- **401**: Unauthorized
- **415**: Unsupported content media type
- **422**: Compatibility failure, Invalid file type, Image size is over 5MB

---
### POST /devices/{deviceId}/actions/uploadencryptedfile

**Summary:** Upload Encrypted File to Decrypt

**Description:** Uploads a file that has been encrypted by a device. If the system has the encryption keys, the file will be decrypted and available for download at GET /devices/{deviceId}/actions/downloaddecryptedfile. Refer to GET /deviceschema and POST /devices/compatibility for the applicability of the action to a given device and to verify the device's compatibility prior to execution. Only execute actions against supported and compatible devices. Requires the caller be granted the "Decrypt File" permission on the device's parent device group.
Contains Binary or Base64 encoded binary file with Content-Type: application/octet-stream and Content-Transfer-Encoding: base64 or binary

**(Available Since MobiControl v14.0.0)**

Content-Type of the Request body must be multipart/related; boundary={any boundary identifier} Multipart request body must contain the following parts: Content-Type: application/octet-stream Content-Transfer-Encoding: Base64 Content-Disposition: form-data; name="LockScreenFile"; filename="some_image.jpg" Base64-encoded image data --foo_bar_baz--

**Parameters:**
- `deviceId` (Required): Type: string.

**Responses:**
- **204**: Success
- **400**: Bad request, ie. Invalid file contents or metadata
- **401**: Unauthorized

---
### GET /devices/{deviceId}/actions/downloaddecryptedfile

**Summary:** Download Decrypted File

**Description:** Downloads the decrypted version of the encrypted file uploaded using POST /devices/{deviceId}/actions/uploadencryptedfile.   Refer to GET /deviceschema and POST /devices/compatibility for the applicability of the action to a given device and to verify the device's compatibility prior to execution. Only execute actions against supported and compatible devices. Requires the caller be granted the "Decrypt File" permission on the device's parent device group.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier
- `referenceId` (Required): Type: string. Description: Identifier of the encrypted file

**Responses:**
- **204**: Success
- **400**: Bad request, ie. Invalid file contents or metadata
- **401**: Unauthorized

---
### GET /devices/{deviceId}/applesoftwareupdates

**Summary:** Retrieve Software Updates Information For a Single Device

**Description:** Retrieves information about the software updates that are available for a specific device. Requires the caller be granted the "View Devices" group permission.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier

**Responses:**
- **200**: Available Software Updates for the device with specified Id

---
### GET /devices/{deviceId}/lastKnownLocation

**Summary:** Retrieve Last Known Location of Device

**Description:** Returns the last known location value for a device that has previously been located.
**(Available Since MobiControl v15.0.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: DeviceId

**Responses:**
- **200**: DeviceLocation object

---
### GET /devices/{deviceId}/linuxAvailableOSUpdates

**Summary:** Retrieve available Operating System Update Information For a Single Linux Device

**Description:** Retrieves information about the Operating System updates that are available for a specific device. Requires the caller be granted the "View Devices" group permission.
**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier

**Responses:**
- **200**: Available Operating System Updates for the device with specified Id

---
### GET /devices/{deviceId}/notes

**Summary:** Retrieve Notes for a Device

**Description:** Returns a list of notes that are associated with a device identified by its device ID, or the device's MAC/IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively.
**(Available Since MobiControl v14.0.3)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier

**Responses:**
- **200**:

---

### POST /devices/{deviceId}/notes

**Summary:** Create a Note

**Description:** Creates a new note for a single device identified by its device ID, or the device’s MAC / IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively and outputs the updated note information. Requires the caller be granted the “Manage Notes” permission for the group.
**(Available Since MobiControl v14.0.3)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier
- `note` (Required): Type: object. Description: The note object

**Responses:**
- **200**:

---
### PUT /devices/{deviceId}/notes/{referenceId}

**Summary:** Update a Note

**Description:** Updates a note for a single device identified by its device ID, or the device's MAC / IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively and outputs the updated note information. Requires the caller be granted the “Manage Notes” permission for the group.
**(Available Since MobiControl v14.0.3)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier.
- `referenceId` (Required): Type: string. Description: The note reference identifier.
- `note` (Required): Type: object. Description: The note object

**Responses:**
- **200**:

---

### DELETE /devices/{deviceId}/notes/{referenceId}

**Summary:** Delete a Note

**Description:** Deletes a note for a single device identified by its device ID, or the device's MAC / IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. Requires the caller be granted the "Manage Notes" permission for the group.
**(Available Since MobiControl v14.0.3)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier
- `referenceId` (Required): Type: string. Description: The note identifier

**Responses:**
- **204**:

---
### DELETE /devices/{deviceId}/advancedConfiguration/{configurationName}

**Summary:** Delete Advanced Configuration based on the given DeviceId

**Parameters:**
- `deviceId` (Required): Type: string. Description: The target device identifier
- `configurationName` (Required): Type: string. Description: Only delete Device Advanced Configuration that is targeting to the given configuration name (e.g. AndroidPlusAgentSettings)

**Responses:**
- **204**:

---
### GET /devices/{deviceId}/compliancePolicies

**Summary:** Retrieve the status of all compliance policies assigned to a device

**Description:** Retrieves the status of all compliance policies assigned to the specified device.
**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description:

**Responses:**
- **200**: Successfully get the compliance policies status of a device
- **403**: Unauthorized access

---
### GET /devices/{deviceId}/complianceExecutedActions

**Summary:** Retrieve executable compliance actions triggered on a device

**Description:** Retrieves executable compliance actions.
**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description:

**Responses:**
- **200**: A list of triggered executable actions

---
### POST /devices/{deviceId}/compliancePolicies/{referenceId}/run

**Summary:** Run a compliance policy on a specific device

**Description:** Runs the specified compliance policy on the specified device.
**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: Device Id.
- `referenceId` (Required): Type: string. Description: Reference Id of a compliance policy.

**Responses:**
- **204**: Successfully start compliance policy evaluation for a device
- **403**: Unauthorized access

---
### POST /devices/{deviceId}/decryptActivationLockBypassCode

**Summary:** Decrypts the Activation Lock Bypass Code

**Description:** The Activation Lock Bypass Code is fetched from device and encrypted before saving it in MobiControl Database. This API performs the decryption of encrypted Activation Lock Bypass Code and returns it in plan text for submission on the Mac machine.
Requires the caller be granted the 'View Activation Lock Bypass Code' permission.

**(Available Since MobiControl v2024.0.0)**


**Parameters:**
- `deviceId` (Required): Type: string. Description: DeviceId.

**Responses:**
- **403**: Forbidden.
- **200**: Success.
- **400**: Contract validation failed.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:<br /><ol><li>1805 - Device '{deviceId}' does not have a activation lock bypass code saved in SOTI MobiControl.</li></ol>

---
### GET /devices/{deviceId}/installedApplications/page

**Summary:** Retrieve Installed Applications for a Device

**Description:** Returns a list of applications that are installed on a device identified by its device ID, or the device's MAC address when deviceId is prefixed with "mac:". Pagination, ordering and filtering parameters are available.
**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier
- `filter`: Type: string. Description: filter for the return list
- `Order`: Type: array.
- `Skip`: Type: integer.
- `Take`: Type: integer.

**Responses:**
- **200**:

---
### GET /devices/{deviceId}/XtHubConfiguration

**Summary:** Get XTreme Hub Advanced configuration for a given device

**Description:** Returns the XTreme Hub advanced configuration either derived from parent group or applied to the device itself

**Parameters:**
- `deviceId` (Required): Type: string. Description: Device Id

**Responses:**
- **200**: XtHubConfiguration object

---
### GET /devices/actionScripts

**Summary:** Retrieve All Available Action Scripts Currently Saved on the System

**Description:**

**(Available Since MobiControl v14.0.0)

This API will be deprecated as of MobiControl v2024.1. Replace with GET /deviceScripts/type prior to v2024.1 to avoid service impact.**



**Parameters:**
- `scriptType`: Type: string.

**Responses:**
- **200**: A collection of action scripts

---

### POST /devices/actionScripts

**Summary:** Add a New Device Action Script to the System

**Description:** If an existing action script has the same name as the new script, an Id value of -1 will be returned.
**(Available Since MobiControl v14.0.0)

This API will be deprecated as of MobiControl v2024.1. Replace with POST /deviceScripts prior to v2024.1 to avoid service impact.**


**Parameters:**
- `newScript` (Required): Type: object. Description: The new action script. Max size 10MB.
- `replaceExisting`: Type: boolean. Description: Replace the existing action script with the same name as this new one

**Responses:**
- **200**: The Id of the newly added action script, or -1 if an action script with the same name already exists.

---
### GET /devices/scripts

**Summary:** Retrieve All Available Scripts of Provided Script Types Currently Saved on the System Defaults to ActionScript

**Description:**

**(Available Since MobiControl v15.0.0)

This API will be deprecated as of MobiControl v2024.1. Replace with GET /deviceScripts/type prior to v2024.1 to avoid service impact.**



**Parameters:**
- `scriptTypes`: Type: array.

**Responses:**
- **200**: A collection of action scripts

---
### GET /devices/actionScripts/{id}

**Summary:** Retrieve the Specified Device Action Script

**Description:**

**(Available Since MobiControl v14.0.0)

This API will be deprecated as of MobiControl v2024.1. Replace with GET /deviceScripts/{referenceId} prior to v2024.1 to avoid service impact.**



**Parameters:**
- `id` (Required): Type: integer. Description: The action script identifier

**Responses:**
- **200**: The requested action script if it exists

---

### PUT /devices/actionScripts/{id}

**Summary:** Update the Given Action Script Content

**Description:**

**(Available Since MobiControl v14.0.0)

This API will be deprecated as of MobiControl v2024.1. Replace with PUT /deviceScripts/{referenceId} prior to v2024.1 to avoid service impact.**



**Parameters:**
- `id` (Required): Type: integer. Description: The action script identifier
- `content` (Required): Type: object. Description: The updated content. Max size 10MB.

**Responses:**
- **204**:

---

### DELETE /devices/actionScripts/{id}

**Summary:** Delete the Given Action Script from the System

**Description:**

**(Available Since MobiControl v14.0.0)

This API will be deprecated as of MobiControl v2024.1. Replace with DELETE /deviceScripts/{referenceId} prior to v2024.1 to avoid service impact.**



**Parameters:**
- `id` (Required): Type: integer. Description: The action script identifier

**Responses:**
- **204**:

---
## Directories

### GET /directories/connections

**Summary:** Retrieve the Names of All Currently Configured Directory Service Connections.

**Description:** This returns the names of all currently configured directory server connections.

**(Available Since MobiControl v14.0.0)**

**Responses:**
- **200**: A list of the connection names.

---
### GET /directories/{directoryConnectionName}/entries

**Summary:** Retrieve Directory Service Users and/or Groups.

**Description:** Returns Directory Service users and/or groups for a given connection based on the specified query parameters. The searchString requires one or more characters
         and is used as the keyword in the search pattern of the user and/or group as defined in the MobiControl Directory Service connection settings. The response will include
         properties specific to the object types returned (user or group).

**(Available Since MobiControl v13.3.0)**

**Parameters:**
- `directoryConnectionName` (Required): Type: string. Description: The directory connection that the search is to be performed on. Must be double URL-encoded (e.g. SOTI%2520Directory%2520Service). When called from this page, it should be encoded only once (SOTI%20Directory%20Service).
- `searchString` (Required): Type: string. Description: Value to use as the search keyword in the defined Directory Service connection search pattern.
- `type`: Type: string. Description: Search directory for users and/or groups. Leave blank to search both Users and Groups.
- `memberOf`: Type: array. Description: Limit results to members of this list of group SID values.

**Responses:**
- **500**: Failed to retrieve data from directory due to an unexpected error. Please consult the Management Server logs for more information.

---
### GET /directories/entries

**Summary:** Retrieve All Directory Services Users and/or Groups.

**Description:** Returns Directory Service users and/or groups for all connections based on the specified query parameters. The searchString required one or more characters
         and is used as the keyword in the search pattern of the users and/or groups as defined in the MobiControl Directory Service connection settings. The response will include
         properties specific to the object types returned(users or groups).

**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `searchString` (Required): Type: string. Description: Value to use as the search keyword in the defined Directory Service connection search pattern.
- `type`: Type: string. Description: Search directory for users and/or groups. Leave blank to search both Users and Groups.
- `memberOf`: Type: array. Description: Limit results to members of this list of group SID values.

**Responses:**
- **500**: Failed to retrieve data from directory due to an unexpected error. Please consult the Management Server logs for more information.

---
### GET /directoryTypes/ldap/syncFrequency

**Summary:** Returns the frequency for synchronization of Users Info with Directory Servers.

**Description:**
Returns the frequency at which the enrolled users information within MobiControl will be synchronized with the configured Directory Servers

Requires the caller be granted the "Web Console Access" permission.

**(Available Since MobiControl v15.4.0)**

**Responses:**
- **200**: Returns LDAP Directory Service Sync frequency settings.
- **401**: Unauthorized access.
- **403**: Forbidden.

---

### PUT /directoryTypes/ldap/syncFrequency

**Summary:** Updates the frequency for synchronization of Users Info with Directory Servers.

**Description:**
Updates the frequency at which the enrolled users information within MobiControl will be synchronized with the configured Directory Servers. Request format { ""Period"": ""DD.HH:MM:SS"" }

where DD = Day(s); HH=Hour(s) (Range:0-23); MM=Minute(s); SS=Second(s)

Examples:

Format to set as 2 days will be { ""Period"": ""2.0:00:00"" }

Format to set as 2 hours will be { ""Period"": ""2:00:00"" }

The value { ""Period"": ""24:00:00"" } will mean 24 days.

Requires the caller to be granted "Manage Servers and Global Settings" permission.

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `request` (Required): Type: object. Description: Define the values in the prescribed format for the sync frequency.

**Responses:**
- **204**: Successfully set LDAP Directory Service Sync frequency settings.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.

---
### GET /directoryTypes

**Summary:** Returns a list of all configured LDAP and Azure directories.

**Description:** This returns a list of all configured LDAP and AZURE Directories

Requires the caller be granted the "View Directory Services" permission.

**(Available Since MobiControl v15.3.0)**

**Responses:**
- **200**: Successfully returned LDAP and AZURE Directories.
- **401**: Unauthorized access.
- **403**: Forbidden.

---
### GET /directoryTypes/ldapAndAzureByAppTypes

**Summary:** Returns a list of configured LDAP and Azure directories.

**Description:** Returns a list of configured LDAP directories and Azure directories using only custom Azure applications.
         Additionally, Azure application type parameter can be used to return the Azure directories with default Azure applications.

Requires the caller be granted the "View Directory Services" permission.

**(Available Since MobiControl v2024.0.0)**

**Parameters:**
- `azureAppTypes`: Type: array. Description: List of Azure application types.

**Responses:**
- **200**: Successfully returned LDAP and Azure directories.
- **401**: Unauthorized access.
- **403**: Forbidden.

---
### GET /directoryTypes/ldap/{referenceId}

**Summary:** Returns the specified LDAP Directory details.

**Description:** Returns the specified LDAP Directory details against its reference ID

Requires the caller be granted the "Web Console Access" permission.

**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Identifier for the LDAP Directory connection to be retrieved.

**Responses:**
- **200**: Successfully returned LDAP Directory.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.

---

### PUT /directoryTypes/ldap/{referenceId}

**Summary:** Updates the specified LDAP Directory details.

**Description:** This updates the existing LDAP Directory connection using its requested Id. This returns the updated connection details

Requires the caller be granted the "Manage Directory Services" permission.

**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Identifier for the LDAP Directory connection to be updated.
- `request` (Required): Type: object. Description: LDAP Directory connection details.

**Responses:**
- **200**: Successfully updated LDAP Directory.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.

---

### DELETE /directoryTypes/ldap/{referenceId}

**Summary:** Deletes the specified LDAP Directory.

**Description:** Deletes the specified LDAP Directory connection under MobiControl

Requires the caller be granted the "Manage Directory Services" permission.

**(Available Since MobiControl v15.3.0)**.

**Parameters:**
- `referenceId` (Required): Type: string. Description: Identifier for the LDAP Directory connection to be deleted.

**Responses:**
- **204**: Successfully deleted LDAP Directory.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.

---
### GET /directoryTypes/ldap/defaultSchemas

**Summary:** Returns the default schema of LDAP attributes.

**Description:** This returns the default schema of LDAP attributes

Requires the caller be granted the "Web Console Access" permission.

**(Available Since MobiControl v15.3.0)**

**Responses:**
- **200**: Successfully returned LDAP schema.
- **401**: Unauthorized access.
- **403**: Forbidden.

---
### GET /directoryTypes/ldap/providerTypes

**Summary:** Returns the context provider type.

**Description:** This returns the context provider type i.e the types of Directories available

Requires the caller be granted the "Web Console Access" permission.

**(Available Since MobiControl v15.3.0)**

**Responses:**
- **200**: Successfully returned context provider type.
- **401**: Unauthorized access.
- **403**: Forbidden.

---
### GET /directoryTypes/ldap

**Summary:** Returns a list of all LDAP Directories.

**Description:** This returns a list of all LDAP Directories

Requires the caller be granted the "Web Console Access" permission.

**(Available Since MobiControl v15.3.0)**

**Responses:**
- **200**: Successfully Returns a list of LDAP Directories.
- **401**: Unauthorized access.
- **403**: Forbidden.

---

### POST /directoryTypes/ldap

**Summary:** Creates a new LDAP Directory.

**Description:** This creates a new LDAP Directory connection under MobiControl

Requires the caller be granted the "Manage Directory Services" permission.

**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `request` (Required): Type: object. Description: Contract for creating the LDAP Directory connection.

**Responses:**
- **201**: Successfully created LDAP Directory.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.

---
### POST /directoryTypes/ldap/actions/testConnection

**Summary:** Creates a LDAP Directory Test connection request.

**Description:** This is for testing the LDAP Directory connection. This returns the test connection result

Requires the caller be granted the "Manage Directory Services" permission.

**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `request` (Required): Type: object. Description: Contract for creating the LDAP Directory test connection.

**Responses:**
- **200**: Successfully tested connection.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.

---
### GET /directoryTypes/azure

**Summary:** Returns a list of all Azure Directories.

**Description:** This returns a list of all Azure Directories.

Requires the caller be granted the "View Directory Services" permission

**(Available Since MobiControl v15.4.0)**
From v15.5.0 onward, communication to Azure Directory is done through Microsoft Graph API instead of Azure Graph API. The 'AzureGraphApiAddress' field should contain a valid Microsoft Graph API base address.

**Responses:**
- **200**: Successfully Returns a list of Azure Directories.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.

---

### POST /directoryTypes/azure

**Summary:** Creates a new Azure Directory.

**Description:** This returns created Azure directory contract.

Requires the caller to be granted "Manage Directory Services" permission

**(Available Since MobiControl v15.4.0)**
From v15.5.0 onward, communication to Azure Directory is done through Microsoft Graph API instead of Azure Graph API. The 'AzureGraphApiAddress' field should contain a valid Microsoft Graph API base address.

**Parameters:**
- `azureGroup` (Required): Type: object. Description: The Azure group object.

**Responses:**
- **200**: Successfully created a new Azure Directory.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>6300 - Duplicate connection name not allowed.</li><li>6313 - Azure Graph API incorrect.</li><li>6316 - Microsoft Single Sign-On application is already referenced.</li><li>6317 - Azure tenant is already referenced in another Azure connection with the same app type.</li><li>6319 - Application belongs to another tenant.</li><li>6322 - Azure AD Join Cloud Enrollment application is already referenced.</li></ol>

---
### GET /directoryTypes/azureByAppTypes

**Summary:** Returns a list of configured Azure directories.

**Description:** Returns a list of configured Azure directories using only custom Azure applications. Additionally, Azure application type parameter can be used to return the Azure directories with default Azure applications.

Requires the caller be granted the "View Directory Services" permission.

**(Available Since MobiControl v2024.0.0)**

**Parameters:**
- `azureAppTypes`: Type: array. Description: List of Azure app types.

**Responses:**
- **200**: Successfully returned Azure directories.
- **401**: Unauthorized access.
- **403**: Forbidden.

---
### GET /directoryTypes/azure/{referenceId}

**Summary:** Returns the specified Azure Directory based on referenceId.

**Description:** This returns specified Azure Directory based on referenceId.

Requires the caller be granted the "Web Console Access" permission

**(Available Since MobiControl v15.4.0)**
From v15.5.0 onward, communication to Azure Directory is done through Microsoft Graph API instead of Azure Graph API. The 'AzureGraphApiAddress' field should contain a valid Microsoft Graph API base address.

**Parameters:**
- `referenceId` (Required): Type: string. Description: The Azure reference identifier.

**Responses:**
- **200**: Successfully Returns the specified Azure Directory.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.

---

### PUT /directoryTypes/azure/{referenceId}

**Summary:** Updates the specified Azure directory profile for requested referenceId.

**Description:** This is for updating the existing Azure directory.

Requires the caller to be granted "Manage Directory Services" permission

**(Available Since MobiControl v15.4.0)**
From v15.5.0 onward, communication to Azure Directory is done through Microsoft Graph API instead of Azure Graph API. The 'AzureGraphApiAddress' field should contain a valid Microsoft Graph API base address.

**Parameters:**
- `referenceId` (Required): Type: string. Description: The Azure reference identifier.
- `azureGroup` (Required): Type: object. Description: The Azure group object.

**Responses:**
- **200**: Successfully updated the specified Azure directory profile.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>6300 - Duplicate connection name not allowed.</li><li>6313 - Azure Graph API incorrect.</li><li>6316 - Microsoft Single Sign-On application is already referenced.</li><li>6317 - Azure tenant is already referenced in another Azure connection with the same app type.</li><li>6319 - Application belongs to another tenant.</li><li>6322 - Azure AD Join Cloud Enrollment application is already referenced.</li></ol>

---

### DELETE /directoryTypes/azure/{referenceId}

**Summary:** Deletes the specified Azure directory.

**Description:** This is for deleting the Azure connection record based on referenceId.

Requires the caller to be granted "Manage Directory Services" permission.

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The Azure reference identifier.

**Responses:**
- **200**: Successfully record deleted.
- **204**: No Content Found.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>6302 - No record found for the given Id</li><li>6303 - Cannot delete Azure connection, because it's been referenced.</li></ol>

---
### GET /directoryTypes/azure/tenants

**Summary:** Returns a list of all Azure Tenants.

**Description:** This returns a list of all Azure Tenants.

Requires the caller be granted the "Web Console Access" permission.

**(Available Since MobiControl v15.4.0)**

**Responses:**
- **200**: Successfully Returns a list of Azure Tenants.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.

---

### POST /directoryTypes/azure/tenants

**Summary:** Creates a new Azure Tenant.

**Description:** This returns created Azure Tenant contract.

Requires the caller to be granted "Manage Directory Services" permission.

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `azureTenant` (Required): Type: object. Description: The Azure tenant object.

**Responses:**
- **201**: Successfully created a new Azure Tenant.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>6304 - Duplicate Azure Tenant Id not allowed.</li><li>6305 - Duplicate Name for Azure Tenant not allowed.</li><li>6306 - Duplicate Azure Tenant Name not allowed.</li><li>6311 - Duplicate Azure Tenant Metadata Endpoint Address not allowed.</li><li>6312 - Azure Tenant Metadata Endpoint Address incorrect.</li></ol>

---
### GET /directoryTypes/azure/tenants/{tenantId}

**Summary:** Returns the specified Azure Tenant based on requested tenantId.

**Description:** This returns Azure Tenant based on requested tenantId.

Requires the caller be granted the "Web Console Access" permission.

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `tenantId` (Required): Type: string. Description: The Azure tenant identifier.

**Responses:**
- **200**: Successfully Returns the specified Azure Tenant.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.

---

### PUT /directoryTypes/azure/tenants/{tenantId}

**Summary:** Updates the specified Azure Tenant for requested tenantId.

**Description:** This is for updating the existing Azure Tenant.

Requires the caller to be granted "Manage Directory Services" permission.

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `tenantId` (Required): Type: string. Description: The Azure tenant identifier.
- `azureTenant` (Required): Type: object. Description: The Azure tenant object.

**Responses:**
- **200**: Successfully updated the specified Azure Tenant.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>6302 - Azure Tenant ID do not exist.</li><li>6305 - Duplicate Name for Azure Tenant not allowed.</li><li>6306 - Duplicate Azure Tenant Name not allowed.</li><li>6311 - Duplicate Azure Tenant Metadata Endpoint Address not allowed.</li><li>6312 - Azure Tenant Metadata Endpoint Address incorrect.</li>.
         </ol>

---

### DELETE /directoryTypes/azure/tenants/{tenantId}

**Summary:** Deletes the specified Azure Tenant.

**Description:** This is for deleting the Azure tenant based on tenantId.

Requires the caller to be granted "Manage Directory Services" permission.

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `tenantId` (Required): Type: string. Description: The Azure tenant identifier.

**Responses:**
- **200**: Successfully record deleted.
- **204**: No Content Found.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>6302 - Azure Tenant ID do not exist.</li><li>6301 - Azure Tenant is referenced.</li></ol>

---
### GET /directoryTypes/azure/tenants/{tenantId}/applications

**Summary:** Returns a list of all Azure Applications based on TenantId.

**Description:** This returns all Azure Applications based on TenantId.

Requires the caller be granted the "Web Console Access" permission.

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `tenantId` (Required): Type: string. Description: The Azure tenant identifier.

**Responses:**
- **200**: Successfully Returns a list of Azure Applications.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.

---

### POST /directoryTypes/azure/tenants/{tenantId}/applications

**Summary:** Creates a new Azure Application.

**Description:** This returns created Azure Application contract.

Requires the caller to be granted "Manage Directory Services" permission.

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `tenantId` (Required): Type: string. Description: The tenant identifier.
- `azureApplication` (Required): Type: object. Description: The Azure application object.

**Responses:**
- **201**: Successfully created a new Azure Application.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>6302 - Azure Tenant ID do not exist.</li><li>6309 - Duplicate Azure Application Name not allowed.</li><li>6310 - Duplicate Azure Application Client ID not allowed.</li><li>6318 - Changes on Microsoft Single Sign-On application are not allowed.</li></ol>

---

### PUT /directoryTypes/azure/tenants/{tenantId}/applications

**Summary:** Updates the specified Azure Application for requested applicationId.

**Description:** This is for updating an existing Azure Application.

Requires the caller to be granted "Manage Directory Services" permission.

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `tenantId` (Required): Type: string. Description: The tenant identifier.
- `azureApplication` (Required): Type: object. Description: The Azure application object.

**Responses:**
- **200**: Successfully updated the specified Azure Application.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>6302 - Azure Tenant ID do not exist.</li><li>6309 - Duplicate Azure Application Name not allowed.</li><li>6310 - Duplicate Azure Application Client ID not allowed.</li><li>6318 - Changes on Microsoft Single Sign-On application are not allowed.</li></ol>

---
### GET /directoryTypes/azure/tenants/applications/{applicationId}

**Summary:** Returns the specified Azure Application based on requested applicationId.

**Description:** This returns Azure Application based on requested applicationId

Requires the caller be granted the "Web Console Access" permission.

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `applicationId` (Required): Type: string. Description: The application reference identifier.

**Responses:**
- **200**: Successfully Returns the specified Azure Application.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.

---

### DELETE /directoryTypes/azure/tenants/applications/{applicationId}

**Summary:** Deletes the specified Azure Application.

**Description:** This is for deleting the Azure application based on applicationId.

Requires the caller to be granted "Manage Directory Services" permission.

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `applicationId` (Required): Type: string. Description: The Azure application identifier.

**Responses:**
- **200**: Successfully record deleted.
- **204**: No Content Found.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>6308 - Azure Application is referenced.</li><li>6318 - Changes on Microsoft Single Sign-On application are not allowed.</li></ol>

---
## Email

### GET /emailProfiles

**Summary:** Get All Email Profiles

**Description:** This returns all email profiles.
**(Available Since MobiControl v14.2.0)**

**Responses:**
- **200**:

---
### GET /emailProfiles/{name}

**Summary:** Retrieve a Single Email Profile

**Description:** This returns a single email profile based on the specific query parameters.
**(Available Since MobiControl v14.2.0)**

**Parameters:**
- `name` (Required): Type: string. Description: The name of the profile

**Responses:**
- **200**:

---
## Enrollment Configuration

### GET /enrollment/userUnenrollAction

**Summary:** Returns the settings for the user-initiated unenroll action

**Description:**
This returns the settings of the actions to be performed when the device is unenrolled by end-user
Requires the caller be granted the "Web Console Access" permission
**(Available Since MobiControl v15.3.0)**

**Responses:**
- **200**: Successfully set log levels
- **401**: Unauthorized access
- **403**: Forbidden

---

### PUT /enrollment/userUnenrollAction

**Summary:** Updates the settings for the user-initiated unenroll action

**Description:**
This updates the settings of the actions to be performed when the device is unenrolled by end-user
Requires the caller to be granted "Manage Servers and Global Settings" permission
**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `unenrollActionSettings` (Required): Type: object. Description: Define the values in key value format for the action to be taken when a device is unenrolled by the end-user. Check Model for details.

**Responses:**
- **204**: Successfully set user unenrollment settings
- **400**: Contract validation failed
- **401**: Unauthorized access
- **403**: Forbidden

---
## Enrollment Rules

### GET /enrollment/rules

**Summary:** Returns a list of the summary of all the enrollment rules

**Description:**
Requires the caller to be granted the "MobiControl Access" permission.

**(Available Since MobiControl v15.3.0)**

Returns a list of the summary of all the enrollment rules, including whether the rule is the default rule for that platform.


**Responses:**
- **200**:

---
### GET /enrollment/settings

**Summary:** Returns additional device enrollment information.

**Description:**
Requires the caller to be granted the "MobiControl Access" permission.

**(Available Since MobiControl v15.3.0)**

**Responses:**
- **200**:

---
### POST /enrollment/{ruleId}/actions/{actionName}

**Summary:** Performs the specified action on the specified Add Device Rule.

**Description:**
Requires the caller to be granted the "Manage Enrollment Policies" permission.

**(Available Since MobiControl v15.3.0)**
The only supported value for {actionName} is 'setDefault'. Sets the specified Add Device Rule as the Default Add Device Rule for that platform.

**Parameters:**
- `ruleId` (Required): Type: string.
- `actionName` (Required): Type: string.

**Responses:**
- **204**:

---
## External Services

### GET /externalServices/status

**Summary:** Gets the Status of SOTI Services.

**Description:** Get the status of SOTI Services that are used by MobiControl. Requires the caller be granted "View System Health" permission.
**(Available Since MobiControl v15.3.0)**

**Responses:**
- **200**:
- **401**: Unauthorized access
- **403**: Forbidden

---
## Geofences

### POST /geofences

**Summary:** Adds a New Geofence

**Description:** Adds a new geofence with the given name and vertices.
Name must be unique.
For a geofence of N vertices, N+1 vertices must be specified in the input with the last vertex exactly equal to the first vertex.
Requires the caller be granted the "Create Geofence" permission.

**Parameters:**
- `geofenceAddRequest` (Required): Type: object.

**Responses:**
- **200**: Returns the newly created geofence.
- **400**: Contract validation failed
- **403**: Unauthorized access
- **422**: Geofence request validation failed

---
### DELETE /geofences/{name}

**Summary:** Removes a Geofence

**Description:** Removes a geofence by name. The geofence to be removed must not be currently used by any rule. Requires the caller be granted "Remove Geofence" permission.

**Parameters:**
- `name` (Required): Type: string.

**Responses:**
- **204**: Successfully removed the geofence with the specified name
- **403**: Unauthorized access
- **422**: Geofence is been referenced by at least one rule.

---

### GET /geofences/{name}

**Summary:** Retrieves a Single Geofence

**Description:** Retrieves a single geofence by name. Requires the caller be granted "View Geofence" permission.

**Parameters:**
- `name` (Required): Type: string.

**Responses:**
- **200**: Returns the geofence with specified name
- **403**: Unauthorized access

---

### PUT /geofences/{name}

**Summary:** Renames a Geofence

**Description:** Renames an existing geofence. The geofence to be renamed must exists. The new name must be unique. Requires the caller be granted "Rename Geofence" permission.

**Parameters:**
- `name` (Required): Type: string.
- `geofenceName` (Required): Type: object.

**Responses:**
- **204**: Successfully renamed the geofence
- **400**: Contract validation failed
- **403**: Unauthorized access
- **422**: Geofence with specified name already exists

---
### GET /geofences/summary

**Summary:** Retrieves a Summary of All Geofences

**Description:** Retrieves a summary of all geofences. Requires the caller be granted "View Geofence" permission.

**Responses:**
- **200**: Returns a list of geofence summaries

---
## Google Domain Management

### POST /android/googledomainbindings/{referenceId}/actions/{enterpriseAction}

**Summary:** Execute an action on a Google Domain binding.

**Description:** Sends an action to an Google Domain binding.

Requires the caller be granted the "Manage Android Enterprise Bindings" permission.

**(Available Since MobiControl v15.2.0)**

         Supported Actions:.
         - Sync: Sync approved Managed Google Play Store applications with MobiControl.

**Parameters:**
- `referenceId` (Required): Type: string. Description: Google Domain binding identifier.
- `enterpriseAction` (Required): Type: string. Description: The action to be performed on the Google Domain binding.
- `productId`: Type: string. Description: ProductId to handle in case exists.

**Responses:**
- **204**:

---
### GET /android/googledomainbindings

**Summary:** Retrieve all Google Domain bindings.

**Description:** This returns all Google Domain bindings.

Requires the caller be granted the "Web Console Access" permission.
**(Available Since MobiControl v15.2.0)**

**Responses:**
- **200**: Returns Google Domain bindings.
- **401**: Unauthorized access.
- **403**: Forbidden.

---

### POST /android/googledomainbindings

**Summary:** Bind Google domain with MobiControl.

**Description:** This returns Google Domain binding.
**(Available Since MobiControl v15.2.0)**
Requires the caller be granted the "Manage Android Enterprise Bindings" permission.


**Parameters:**
- `request` (Required): Type: object. Description: Request information.

**Responses:**
- **200**: Returns google domain binding.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.

---

### DELETE /android/googledomainbindings

**Summary:** Delete Google domain from MobiControl.

**Description:** Delete the binding from MobiControl**(Available Since MobiControl v15.2.0)**
Requires the caller be granted the "Manage Android Enterprise Bindings" permission.


**Parameters:**
- `request` (Required): Type: object. Description: Request information.

**Responses:**
- **204**: Successfully Delete the Google Domain.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.

---
### GET /android/googledomainbindings/{referenceId}

**Summary:** Retrieves Google Domain binding with specified reference id.

**Description:** This returns a Google Domain binding.
**(Available Since MobiControl v15.2.0)**
         Requires the caller be granted the "Web Console Access" permission.


**Parameters:**
- `referenceId` (Required): Type: string. Description: Google Domain binding identifier.

**Responses:**
- **200**: Returns Google Domain binding for specified reference id.
- **401**: Unauthorized access.
- **403**: Forbidden.

---
### GET /android/googledomainbindings/{referenceId}/apps

**Summary:** Retrieve approved applications for a Google Domain binding.

**Description:** Returns a list of approved applications from the Managed Google Play Store for the provided Google Domain binding.

**(Available Since MobiControl v15.2.0)**
         Requires the caller be granted the "Web Console Access" permission..


**Parameters:**
- `referenceId` (Required): Type: string. Description: Google Domain binding identifier.
- `appName`: Type: string. Description: Filter apps by name.
- `isApproved`: Type: boolean. Description: Filter apps by approved status.

**Responses:**
- **200**:

---
### GET /android/googledomainbindings/{referenceId}/secondarydomains

**Summary:** Retrieves Secondary Domains of Google Domain binding identifier.

**Description:** This returns the secondary domains of Google Domain binding.
**(Available Since MobiControl v15.2.0)**
         Requires the caller be granted the "Web Console Access" permission..


**Parameters:**
- `referenceId` (Required): Type: string. Description: Google Domain binding identifier.

**Responses:**
- **200**: Returns secondary domains of google domain binding.
- **401**: Unauthorized access.
- **403**: Forbidden.

---
### POST /android/googledomainbindings/{referenceId}/secondarydomains/{secondaryDomain}

**Summary:** Add the secondary domain to primary domain.

**Description:** This returns primary Google Domain binding of secondary domain.
**(Available Since MobiControl v15.2.0)**
Requires the caller be granted the "Manage Android Enterprise Bindings" permission.


**Parameters:**
- `referenceId` (Required): Type: string. Description: Google Domain binding identifier.
- `secondaryDomain` (Required): Type: string. Description: Secondary domain of google Domain binding.

**Responses:**
- **200**: Returns Google Domain binding.
- **401**: Unauthorized access.
- **403**: Forbidden.

---

### DELETE /android/googledomainbindings/{referenceId}/secondarydomains/{secondaryDomain}

**Summary:** Remove the secondary domain from primary domain.

**Description:** This returns Google Domain binding.
**(Available Since MobiControl v15.2.0)**
Requires the caller be granted the "Manage Android Enterprise Bindings" permission.


**Parameters:**
- `referenceId` (Required): Type: string. Description: Google Domain binding identifier.
- `secondaryDomain` (Required): Type: string. Description: Secondary domain of google Domain binding.

**Responses:**
- **200**: Successfully Delete the Managed Google Play.
- **401**: Unauthorized access.
- **403**: Forbidden.

---
## Health Attestation

### GET /windows/healthattestation/server/configuration

**Summary:** Gets the current Health Attestation Server Summary.

**Description:** This gets the current Health Attestation Server summary.

Requires the caller to be granted Global Setting permission.

** (Available Since MobiControl v15.3.0)**

**Responses:**
- **200**:
- **401**: Unauthorized access.
- **403**: Forbidden.

---

### PUT /windows/healthattestation/server/configuration

**Summary:** Sets the Health Attestation Server configuration.

**Description:** This updates the Health Attestation Server configuration.
         This API confirms that the server is reachable by attempting to establish a connection before saving the configuration.

Requires the caller to be granted Global Setting permission.

** (Available Since MobiControl v15.3.0)**

**Parameters:**
- `serverConfiguration` (Required): Type: object.

**Responses:**
- **204**: Server configuration updated.
- **400**: Invalid request.
- **401**: Unauthorized access.
- **403**: Forbidden.

---

### DELETE /windows/healthattestation/server/configuration

**Summary:** Delete the current Health Attestation Server configuration.

**Description:** This will delete the current Health Attestation Server configuration and set the default configuration.
         The default configuration uses the Microsoft Servers: https://has.spserv.microsoft.com/HealthAttestation/ValidateHealthCertificate/v1

Requires the caller to be granted Global Setting permission.

** (Available Since MobiControl v15.3.0)**

**Responses:**
- **204**: Server configuration deleted.
- **401**: Unauthorized access.
- **403**: Forbidden.

---
## Identity Providers

### GET /identityProviders/connections

**Summary:** Retrieve the names of all currently configured Identity Provider(IDP) connections.

**Description:** Retrieves all Identity Provider connections configured within a MobiControl environment.

Requires the caller be granted the "View Directory Services" permission.

**(Available Since MobiControl v14.3.0)**

**Responses:**
- **200**: A list of the connection names.

---
### GET /identityProviders/{identityProviderReferenceId}/Users

**Summary:** Retrieve Identity Provider Users.

**Description:** Returns Identity Provider users for a given Identity Provider connection based on the specified query parameters. The searchString requires one or more characters
         and is used as the keyword in the search pattern of the user as defined in the MobiControl Identity Provider connection settings.

Requires the caller be granted the "Lookup Directory Users and Group Membership" permission.

**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `identityProviderReferenceId` (Required): Type: string. Description: Identity Provider Reference Id.
- `searchString` (Required): Type: string. Description: Value to use as the search keyword in the defined Identity Provider connection search pattern.

**Responses:**
- **200**:

---
### GET /identityProviders/{identityProviderReferenceId}/LdapEntities

**Summary:** Retrieve Identity Provider Users.

**Description:** Returns Identity Provider Ldap users for a given Identity Provider connection based on the specified query parameters. The searchString requires one or more characters
         and is used as the keyword in the search pattern of the user as defined in the MobiControl Identity Provider connection settings.

Requires the caller be granted the "Lookup Directory Users and Group Membership" permission.

**Parameters:**
- `identityProviderReferenceId` (Required): Type: string. Description: Identity Provider Reference Id.
- `searchString` (Required): Type: string. Description: Value to use as the search keyword in the defined Identity Provider connection search pattern.
- `type`: Type: string. Description: The type of object that can be searched in a directory.

**Responses:**
- **500**: Failed to retrieve data from directory due to an unexpected error. Please consult the Management Server logs for more information.

---
### GET /identityProviders

**Summary:** Retrieve all Identity Providers configurations.

**Description:** Retrieve the configuration information for all identity providers.

Requires the caller be granted the "View Directory Services" permission.

**(Available Since MobiControl v15.0.0)**

**Responses:**
- **200**:

---

### POST /identityProviders

**Summary:** Create an Identity Provider.

**Description:** Creates a new Identity Provider

Requires the caller be granted the "Manage Servers and Global Settings" permission.

**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `identityProvider` (Required): Type: object. Description: contract to create a new identity Provider.

**Responses:**
- **400**: Contract validation exception.
- **401**: Unauthorized access.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>1 - Missing mandatory parameter Name.</li><li>1 - Missing mandatory parameter Identity Provider Entity ID.</li><li>1 - Missing mandatory parameter Identity Provider URL.</li><li>1 - Missing mandatory parameter Certificates.</li><li>1 - Missing mandatory parameter Directory.</li><li>1 - Missing mandatory parameter List Attribute.</li><li>1 - Missing mandatory parameter Base64 Content.</li><li>2 - Parameter Identity Provider URL has invalid value string.</li><li>2 - Parameter Logout URL has invalid value string.</li><li>2 - Parameter Identity Provider Metadata URL has invalid value string.</li><li>2 - Parameter LdapConnectionReferenceId has invalid value string.</li><li>2500 - Invalid Certificate format for '{0}' provider. The certificate should be in X509 format.</li></ol>

---

### PUT /identityProviders

**Summary:** Update an existing Identity Provider.

**Description:** Updates an existing Identity Provider

Requires the caller be granted the "Manage Servers and Global Settings" permission.

**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `identityProvider` (Required): Type: object. Description: contract to update the existing identity Provider.

**Responses:**
- **400**: Contract validation exception.
- **401**: Unauthorized access.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>1 - Missing mandatory parameter Name.</li><li>1 - Missing mandatory parameter Identity Provider Entity ID.</li><li>1 - Missing mandatory parameter Identity Provider URL.</li><li>1 - Missing mandatory parameter Certificates.</li><li>1 - Missing mandatory parameter Directory.</li><li>1 - Missing mandatory parameter List Attribute.</li><li>2 - Parameter Identity Provider URL has invalid value string.</li><li>2 - Parameter Logout URL has invalid value string.</li><li>2 - Parameter Identity Provider Metadata URL has invalid value string.</li><li>2 - Parameter LdapConnectionReferenceId has invalid value string.</li><li>2500 - Invalid Certificate format for '{0}' provider. The certificate should be in X509 format.</li><li>2501 - Entity with Id '{0}' does not exist</li><li>2503 - This Identity Provider is referenced by other object(s) and cannot be modified or deleted.</li></ol>

---
### GET /identityProviders/{name}

**Summary:** Retrieve Identity Providers (IdP)configuration for a specified IdP name.

**Description:** Retrieve the configuration information for specified identity provider.

Requires the caller be granted the "View Directory Services" permission.

**(Available Since MobiControl v15.0.0)**

**Parameters:**
- `name` (Required): Type: string.

**Responses:**
- **200**:

---
### POST /identityProviders/sotiIdp

**Summary:** Configure SOTI Identity Provider.

**Description:** This allows the configuration of SOTI Identity as an Identity Provider (IdP) to MobiControl, by entering the Client ID &amp; Client Secret information received from SOTI Identity.
         Once this configuration has been completed, all IdP user management will occur in SOTI Identity and not in MobiControl.
         MobiControl will only manage Local Users which were not migrated to SOTI Identity.  This configuration will not impact permissions.  Client ID &amp; Client Secret can be retrieved from
         SOTI Identity when SOTI Professional Services activates SOTI Identity on SalesForce.

Requires the caller be granted the "Manage Servers and Global Settings" permission.

**(Available Since MobiControl v15.0.0)**

**Parameters:**
- `identityProvider` (Required): Type: object. Description: Mobicontrol Client ID and Secret from SOTI Identity.

**Responses:**
- **200**:

---

### PUT /identityProviders/sotiIdp

**Summary:** Updating the SOTI Identity Provider connection.

**Description:** Update the client secret of the Identity Provider for Soti Identity.

Requires the caller be granted the "Manage Servers and Global Settings" permission.

**(Available Since MobiControl v15.0.0)**

**Parameters:**
- `data` (Required): Type: object. Description:

**Responses:**
- **204**:

---
### POST /identityProviders/sotiIdp/actions/sync

**Summary:** Syncs available providers/consumers list from the SOTI Identity.

**Description:** This API triggers a reminder to sync the available list of  providers/consumers from SOTI Identity.

Requires the caller be granted the "Manage Console Authentication" permission.

**(Available Since MobiControl v2024.0.0)**

**Parameters:**
- `syncProviders` (Required): Type: boolean. Description: if set to true, syncs providers.
- `syncConsumers` (Required): Type: boolean. Description: if set to true, syncs consumers.

**Responses:**
- **204**: The operation has completed successfully.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:<br /><ol><li>3103 - SOTI Identity is not configured.</li></ol>

---
### DELETE /identityProviders/{referenceId}

**Summary:** Deleting the identity provider connection.

**Description:** Delete Identity Provider for a given connection based on the specified ReferenceID. The ReferenceID can be obtained by running the GET/IdentityProviders api.
         Using this API will remove all references to the Identity Provider, including all users and user groups / roles which were used.

Requires the caller be granted the "Manage Servers and Global Settings" permission.

**(Available Since MobiControl v15.0.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id of Identity Provider.

**Responses:**
- **204**:

---
### POST /identityProviders/validatesotiidp

**Summary:** Validate the Client Credentials.

**Description:** Validate the Soti Identity Client Credentials.

Requires the caller be granted the "Manage Servers and Global Settings" permission.
         **(Available Since MobiControl v15.3.0)**

**Parameters:**
- `identityProvider` (Required): Type: object. Description: SotiIdentityProvider.

**Responses:**
- **200**: Returns Boolean value.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.

---
### GET /identityProviders/defaultidpuserattributesschema

**Summary:** Gets the default IdP User Attributes Schema.

**Description:** Requires the caller be granted the "View Directory Services" permission.

**Responses:**
- **200**:

---
### GET /identityProviders/certificate

**Summary:** Returns the MobiControl IdP certificate.

**Description:** Returns the MobiControl IdP certificate required for binding MobiControl with an IDP

Requires the caller be granted the "Web Console Access" permission.

**(Available Since MobiControl v15.3.0)**

**Responses:**
- **401**: Unauthorized access.

---
### GET /identityProviders/metadata

**Summary:** Returns the MobiControl IdP metadata.

**Description:** Returns the MobiControl IdP metadata  required for binding MobiControl with an IDP

Requires the caller be granted the "Web Console Access" permission.

**(Available Since MobiControl v15.3.0)**

**Responses:**
- **401**: Unauthorized access.

---
## Ios Enrollment Policies

### POST /enrollmentPolicies/apple/iOS

**Summary:** Creates a new iOS enrollment policy.

**Description:** This API creates a new iOS enrollment policy.



         Requires the caller be granted the "Manage Enrollment Policies" permission.

**(Available since MobiControl v15.6.0)**


**Parameters:**
- `request` (Required): Type: object. Description: Request.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>7403 -  The database already contains enrollment policy named '{0}'. Please enter a different name.</li><li>7404 -  The database already contains enrollment policy tag '{0}'. Please enter a different enrollment policy tag.</li><li>7410 -  Authorization policy referenced with this enrollment policy is associated with another enrollment policy.</li><li>7803 -  Authorization policy referenced with this enrollment policy is other than No Password, Password, LDAP or Idp type.</li><li>7805 -  Prevent Un-enrollment setting can only be enabled if Supervise Device setting is also enabled.</li></ol>

---
### GET /enrollmentPolicies/apple/iOS/{referenceId}

**Summary:** Returns the details of specified iOS enrollment policy.

**Description:** This API returns the details of specified iOS enrollment policy.



         Requires the caller be granted the "View Enrollment Policies" permission.

**(Available since MobiControl v15.6.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Unique identifier for an enrollment policy.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.

---

### DELETE /enrollmentPolicies/apple/iOS/{referenceId}

**Summary:** Deletes the specified iOS enrollment policy.

**Description:** This API deletes the iOS enrollment policy



         Requires the caller be granted the "Manage Enrollment Policies" permission.

**(Available since MobiControl v15.6.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Unique identifier for an enrollment policy.

**Responses:**
- **204**: No Content.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>1223: Can't delete an enrollment policy which leverages ADE and has ADE devices assigned to it</li><li>1224: Can't delete an enrollment policy which is set as default policy for an ADE account</li><li>7401: Can't delete default enrollment policy</li><li>7402: The deployment server failed to reach the enrollment service. Please check your network connections and settings</li><li>7405: Action can't be performed on the specified Enrollment Policy as MobiControl license is not valid.</li><li>7407: Calling the enrollment service is time out.</li></ol>

---

### PUT /enrollmentPolicies/apple/iOS/{referenceId}

**Summary:** Updates the specified iOS enrollment policy.

**Description:** This API updates the specified iOS enrollment policy




         Requires the caller be granted the 'Manage Enrollment Policies' permission.

**(Available since MobiControl v15.6.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: iOS Enrollment Policy Reference Id.
- `updateIosEnrollmentPolicy` (Required): Type: object. Description: Ios Enrollment Policy.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>7403 - The database already contains enrollment policy named &lt;policy name&gt;. Please enter a different name.</li><li>7410 - Authorization policy referenced with this enrollment policy is associated with another enrollment policy.</li><li>7800 - Automated device enrollment option can't be disabled.</li><li>7801 - Cannot update or remove apple business manager account for this specified enrollment policy.</li><li>7803 -  Authorization policy referenced with this enrollment policy is other than No Password, Password, LDAP or Idp type.</li></ol>

---
### POST /enrollmentPolicies/apple/iOS/{referenceId}/actions/email

**Summary:** Emails specified iOS Enrollment Policy details.

**Description:** This API emails specified iOS Enrollment Policy details to the targeted recipient



         Requires the caller be granted the 'Manage Enrollment Policies' permission.

**(Available since MobiControl v15.6.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Unique Identifier for an Enrollment Policy.
- `request` (Required): Type: object. Description: Parameters required for dispatching email.

**Responses:**
- **204**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>6021 - Failed to send email.</li></ol>

---
### PUT /enrollmentPolicies/apple/iOS/{referenceId}/actions/sync

**Summary:** Updates the specified iOS enrollment policy profile.

**Description:** This API updates the specified iOS enrollment policy profile.



         Requires the caller be granted the "Manage Enrollment Policies" permission.

**(Available since MobiControl v15.6.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Unique identifier for an enrollment policy.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>7407: Calling the enrollment service is time out.</li><li>7405: Update profile action can't be performed on the specified Enrollment Policy as MobiControl license is not valid.</li><li>7402: The deployment server failed to reach the enrollment service. Please check your network connections and settings.</li></ol>

---
## Jobs

### GET /jobs

**Summary:** Gets list of jobs.

**Responses:**
- **200**:

---
## License Management

### GET /license

**Summary:** Returns the license information.

**Description:** This API returns the license information along with family wise usage count.



         Requires the caller be granted the "View License Information" permission.

**(Available Since MobiControl v2024.0.0)**


**Responses:**
- **200**: Success.
- **403**: Forbidden.

---
### PUT /license/offlineActivation

**Summary:** Uploads license file to activate MobiControl.

**Description:** This API uploads license file to activate MobiControl.



         Note: Only applicable for on premise instances.



         Requires the caller be granted the "Manage License Information" permission.

**(Available Since MobiControl v2024.0.0)**


**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.
         <br />The following ErrorCode values can be returned.<br /><ol><li>[3401]: Product activation failed.</li><li>[3402]: Product activation failed with server error message.</li><li>[3406]: Product activation failed: Decommissioned registration code is provided for the activation.</li><li>[3410]: Product Activation failed: Entered registration code does not belong to MobiControl.</li><li>[3411]: Product activation failed: Entered installation id is incorrect.</li><li>[3412]: Product activation failed: The current product version is higher than the maximum allowed version.</li><li>[3413]: Product activation failed: The current assembly version is higher than the maximum allowed version.</li><li>[3414]: Product activation failed: The license expired before the release date.</li><li>[3415]: Product activation failed: Sorry, this registration code has expired! Please contact SOTI sales representative</li><li>[3416]: Product activation failed: Your new registration code has a lower device license count than the current number of enrolled devices in Mobicontrol. Please use a registration code that has an appropriate number of device licenses.</li></ol>

---
### PUT /license/updateRegistrationCode

**Summary:** Updates the registration key of MobiControl.

**Description:** This API updates the registration key of MobiControl.



         Note: Only applicable for on premise instances.



         Requires the caller be granted the "Manage License Information" permission.

**(Available Since MobiControl v2024.0.0)**


**Parameters:**
- `registrationInfo` (Required): Type: object.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.
         <br />The following ErrorCode values can be returned.<br /><ol><li>[3401]: Product activation failed.</li><li>[3402]: Product activation failed with server error message.</li><li>[3403]: product activation failed: This registration code has already been activated on another computer</li><li>[3404]: Product activation failed: Activation cannot be completed before the deployment date that was specified at the time of purchase.</li><li>[3405]: Product activation failed: Your Subscription is expired</li><li>[3406]: Product activation failed: Decommissioned registration code is provided for the activation.</li><li>[3407]: Product activation failed: The key you are attempting to activate has expired</li><li>[3408]: Product activation failed: Maximum allowed number of enrollment profiles was reached already</li><li>[3409]: Product activation failed: This Installation Id has already been used on another computer</li><li>[3410]: Product Activation failed: Entered registration code does not belong to MobiControl.</li><li>[3411]: Product activation failed: Entered installation id is incorrect.</li><li>[3412]: Product activation failed: The current product version is higher than the maximum allowed version.</li><li>[3413]: Product activation failed: The current assembly version is higher than the maximum allowed version.</li><li>[3414]: Product activation failed: The license expired before the release date.</li><li>[3415]: Product activation failed: Sorry, this registration code has expired! Please contact SOTI sales representative</li><li>[3416]: Product activation failed: Your new registration code has a lower device license count than the current number of enrolled devices in Mobicontrol. Please use a registration code that has an appropriate number of device licenses.</li><li>[3417]: Product Activation failed: Failed to establish communication with SOTI Services. </li></ol>

---
## Linux Enrollment Policies

### DELETE /enrollmentPolicies/linux/{referenceId}

**Summary:** Deletes the linux enrollment policy.

**Description:** This API deletes the specified linux policy



         Requires the caller be granted the "Manage Enrollment Policies" permission.

**(Available since MobiControl v15.6.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Unique identifier for an enrollment policy.

**Responses:**
- **204**: No Content.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>7401: Can't delete default enrollment policy</li></ol>

---

### GET /enrollmentPolicies/linux/{referenceId}

**Summary:** Returns the linux enrollment policy details.

**Description:** This API returns the details of specified linux enrollment policy



         Requires the caller be granted the "View Enrollment Policies" permission.

**(Available since MobiControl v15.6.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Unique identifier for an enrollment policy.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.

---

### PUT /enrollmentPolicies/linux/{referenceId}

**Summary:** Updates the specified Linux enrollment policy.

**Description:** This API updates the specified Linux enrollment policy.



         Requires the caller be granted the "Manage Enrollment Policies" permission.

**(Available since MobiControl v15.6.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Unique identifier for an enrollment policy.
- `request` (Required): Type: object. Description:

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>7403 -  The database already contains enrollment policy named '{0}'. Please enter a different name.</li><li>7410 - Authorization policy referenced with this enrollment policy is associated with another enrollment policy.</li><li>7600 -  Authorization policy referenced with this enrollment policy has terms and conditions associated with it.</li><li>7601 -  Authorization policy referenced with this enrollment policy is other than No Password, Password or LDAP type.</li></ol>

---
### POST /enrollmentPolicies/linux

**Summary:** Creates a new Linux enrollment policy.

**Description:** This API creates a new Linux enrollment policy



         Requires the caller be granted the "Manage Enrollment Policies" permission.

**(Available since MobiControl v15.6.0)**


**Parameters:**
- `request` (Required): Type: object. Description: Linux Enrollment Policy.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>7410 - Authorization policy referenced with this enrollment policy is associated with another enrollment policy.</li><li>7600: Authorization policy referenced with this enrollment policy has terms and conditions associated with it.</li><li>7601: Authorization policy referenced with this enrollment policy is other than No Password, Password or LDAP type.</li><li>7603: The database already contains enrollment policy named {0}. Please enter a different name.</li></ol>

---
### GET /enrollmentPolicies/linux/{referenceId}/actions/downloadConfig

**Summary:** Returns the linux enrollment policy INI config file.

**Description:** This API returns the INI config file of specified linux enrollment policy



         Requires the caller be granted the "View Enrollment Policies" permission.

**(Available Since MobiControl v15.6.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Unique identifier for an enrollment policy.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.

---
### POST /enrollmentPolicies/linux/{referenceId}/actions/email

**Summary:** Emails linux Enrollment Policy details.

**Description:** This API emails linux Enrollment Policy details to the targetted recipient



         Requires the caller be granted the 'Manage Enrollment Policies' permission.

**(Available since MobiControl v15.6.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Unique identifier for an enrollment policy.
- `parameter` (Required): Type: object. Description: Parameters required for dispatching email.

**Responses:**
- **204**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>6021 - Failed to send email.</li></ol>

---
### GET /enrollmentPolicies/linux/{referenceId}/agents/{agentReferenceId}

**Summary:** Returns the linux enrollment policy Agent Installer.

**Description:** This API returns the Agent Installer of specified linux enrollment policy



         Requires the caller be granted the "View Enrollment Policies" permission.

**(Available Since MobiControl v15.6.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Unique identifier for an enrollment policy.
- `agentReferenceId` (Required): Type: string. Description: Unique identifier for linux agents.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.

---
## Locate Timeout

### PUT /devices/locate/timeOut

**Summary:** Updates the Locate Timeout value

**Description:** This updates the timeout duration in seconds to be used by MobiControl when it is trying to locate a device
Requires the caller be granted the "Manage Servers and Global Settings" permission
**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `locateTimeout` (Required): Type: object. Description: Maximum duration in seconds to locate a device

**Responses:**
- **204**: Successfully add Locate Timeout
- **400**: Contract validation failed
- **401**: Unauthorized access
- **403**: Forbidden

---

### GET /devices/locate/timeOut

**Summary:** Returns the Locate Timeout value

**Description:** This returns the timeout duration in seconds to be used by MobiControl when it is trying to locate a device
Requires the caller be granted the "Web Console Access" permission
**(Available Since MobiControl v15.4.0)**

**Responses:**
- **200**: Returns Locate Timeout
- **401**: Unauthorized access
- **403**: Forbidden

---
## Logs

### GET /logs/events

**Summary:** Retrieve Event Log Descriptions

**Description:** Retrieves global event log descriptions. Requires the caller be granted "Web Console Access" permission.
**(Available Since MobiControl v14.0.0)**

**Responses:**
- **200**: Returns list of events with descriptions for event names and event alert messages.

---
### GET /logs/summary/device/{deviceId}

**Summary:** Retrieve Summary of Logs for a Device

**Description:** Returns a count of logs specific to a device and specified time period. Device can be identified by its device ID, or the device's MAC / IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. Requires the caller be granted the "View Groups" permission on the device's parent device group.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier
- `startDate` (Required): Type: string. Description: The start date. Example: 2015-12-19T16:39:57-02:00
- `endDate` (Required): Type: string. Description: The end date. Example: 2015-12-19T16:39:57-02:00

**Responses:**
- **200**: Returns logs summary for a device identified by its device ID, or the device's MAC address when deviceId is prefixed with "mac:"

---
### GET /logs/device/{deviceId}

**Summary:** Retrieve Logs for a Device

**Description:** Retrieve device event logs specific to a device identified by its device ID, or the device's MAC / IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. Limit the results to matching criteria such as event severity and date range. Requires the caller be granted the "View Groups" permission on the device's parent device group.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier
- `startDate` (Required): Type: string. Description: The start date. Example: 2015-12-19T16:39:57-02:00
- `endDate` (Required): Type: string. Description: The end date. Example: 2015-12-19T16:39:57-02:00
- `logSeverities`: Type: array. Description: List of log severities to include into result set
- `logSources`: Type: array. Description: List of log sources to include into result set
- `order`: Type: string. Description: Defines the sorting order by property. Pass the value as -property for descending, and +property for ascending.
- `skip`: Type: integer. Description: Input the first X (count) entries that should not be returned.
- `take`: Type: integer. Description: Input the number of entries to be returned, after skipping over the 'skip' count.

**Responses:**
- **200**: Returns logs for a device identified by its device ID, or the device's MAC address when deviceId is prefixed with "mac:"

---
### GET /logs/server/{serverIdentity}

**Summary:** Gets the logs by server.

**Description:** Retrieve server logs for a specific server identified by its server Identity. Limit the results to matching criteria such as server type, log Severities, log Sources, and date range.
**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `serverIdentity` (Required): Type: string. Description: The server identifier.
- `serverType` (Required): Type: string. Description: Type of the server.
- `startDate` (Required): Type: string. Description: The start date.
- `endDate` (Required): Type: string. Description: The end date.
- `logSeverities`: Type: array. Description: The log severities.
- `logSources`: Type: array. Description: The log sources.
- `order`: Type: string. Description: Defines the sorting order by property. Pass the value as -property for descending, and +property for ascending.
- `skip`: Type: integer. Description: Input the first X (count) entries that should not be returned.
- `take`: Type: integer. Description: Input the number of entries to be returned, after skipping over the 'skip' count.

**Responses:**
- **200**:

---
### GET /logs/servertype/{serverType}

**Summary:** Gets the type of the logs by server.

**Description:** Retrieve server logs for servers identified by the server Type. Limit the results to matching criteria such as server type, log Severities, log Sources, and date range.
**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `serverType` (Required): Type: string. Description: Type of the server.
- `startDate` (Required): Type: string. Description: The start date.
- `endDate` (Required): Type: string. Description: The end date.
- `logSeverities`: Type: array. Description: The log severities.
- `logSources`: Type: array. Description: The log sources.
- `order`: Type: string. Description: Defines the sorting order by property. Pass the value as -property for descending, and +property for ascending.
- `skip`: Type: integer. Description: Input the first X (count) entries that should not be returned.
- `take`: Type: integer. Description: Input the number of entries to be returned, after skipping over the 'skip' count.

**Responses:**
- **200**:

---
### GET /logs/device/{deviceId}/availableAgentLogTypes

**Summary:** Retrieve Device-side Log Types for a Device

**Description:** Retrieve available types of device-side (agent) logs that can be retrieved for a device identified by its device ID, or the device's MAC / IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. Requires the caller be granted the "Download Agent Logs" permission on the device's parent device group.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier

**Responses:**
- **200**: A list of AgentLogType available for device with given ID.

---
### GET /logs/summary/group/{path}

**Summary:** Retrieve Summary of Logs for a Device Group

**Description:** Returns a count of logs specific to devices within a device group and specified time period. Device group can be identified by its reference ID (recommended) or path. Requires the caller be granted the "View Groups" permission for the specified device group.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `path` (Required): Type: string. Description: The device group identifier for parent device group taken from Reference ID. Deprecated: Can also be a path of parent device group. Must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).
- `startDate` (Required): Type: string. Description: The start date. Example: 2015-12-19T16:39:57-02:00
- `endDate` (Required): Type: string. Description: The end date. Example: 2015-12-19T16:39:57-02:00

**Responses:**
- **200**: Returns logs summary for a device group identified by its path

---
### GET /logs/group/{path}

**Summary:** Retrieve Logs for a Device Group

**Description:** Retrieve event logs for devices within a specific device group identified by its reference ID (recommended) or path. Limit the results to matching criteria such as event severity and date range. Requires the caller be granted the "View Groups" permission for the specified device group.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `path` (Required): Type: string. Description: The device group identifier for parent device group taken from Reference ID. Deprecated: Can also be a path of parent device group. Must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).
- `startDate` (Required): Type: string. Description: The start date. Example: 2015-12-19T16:39:57-02:00
- `endDate` (Required): Type: string. Description: The end date. Example: 2015-12-19T16:39:57-02:00
- `logSeverities`: Type: array. Description: List of log severities to include into result set
- `logSources`: Type: array. Description: List of log sources to include into result set
- `order`: Type: string. Description: Defines the sorting order by property. Pass the value as -property for descending, and +property for ascending.
- `skip`: Type: integer. Description: Input the first X (count) entries that should not be returned.
- `take`: Type: integer. Description: Input the number of entries to be returned, after skipping over the 'skip' count.

**Responses:**
- **200**: Returns logs for a device group by its path

---
## Mac Enrollment Policies

### POST /enrollmentPolicies/apple/macOS

**Summary:** Creates a new macOS enrollment policy.

**Description:** This API creates a new macOS enrollment policy.



         Requires the caller be granted the "Manage Enrollment Policies" permission.

**(Available since MobiControl v15.6.0)**


**Parameters:**
- `request` (Required): Type: object. Description: Request.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>7403 -  The database already contains enrollment policy named '{0}'. Please enter a different name.</li><li>7404 -  The database already contains enrollment policy tag '{0}'. Please enter a different enrollment policy tag.</li><li>7410 -  Authorization policy referenced with this enrollment policy is associated with another enrollment policy.</li><li>7803 -  Authorization policy referenced with this enrollment policy is other than No Password, Password, LDAP or Idp type.</li><li>7805 - Prevent Un-enrollment setting can only be enabled if Supervise Device setting is also enabled.</li></ol>

---
### PUT /enrollmentPolicies/apple/macOS/{referenceId}

**Summary:** Updates the specified macOS enrollment policy.

**Description:** This API updates the specified macOS enrollment policy



         Requires the caller be granted the 'Manage Enrollment Policies' permission.

**(Available since MobiControl v15.6.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: MacOs Enrollment Policy Reference Identifier.
- `updateMacEnrollmentPolicy` (Required): Type: object. Description: Update Mac Enrollment Policy.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>7403 - The database already contains enrollment policy named &lt;policy name&gt;. Please enter a different name.</li><li>7410 - Authorization policy referenced with this enrollment policy is associated with another enrollment policy.</li><li>7800 - Automated device enrollment option can't be disabled.</li><li>7801 - Cannot update or remove apple business manager account for this specified enrollment policy.</li><li>7803 -  Authorization policy referenced with this enrollment policy is other than No Password, Password, LDAP or Idp type.</li><li>7805 - Prevent Un-enrollment setting can only be enabled if Supervise Device setting is also enabled.</li></ol>

---

### GET /enrollmentPolicies/apple/macOS/{referenceId}

**Summary:** Returns the details of specified macOS enrollment policy.

**Description:** This API returns the details of specified macOS enrollment policy.



         Requires the caller be granted the "View Enrollment Policies" permission.

**(Available since MobiControl v15.6.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Unique identifier for an enrollment policy.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.

---

### DELETE /enrollmentPolicies/apple/macOS/{referenceId}

**Summary:** Deletes the specified macOS enrollment policy.

**Description:** This API deletes the macOS enrollment policy



         Requires the caller be granted the "Manage Enrollment Policies" permission.

**(Available since MobiControl v15.6.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Unique identifier for an enrollment policy.

**Responses:**
- **204**: No Content.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>1223: Can't delete an enrollment policy which leverages ADE and has ADE devices assigned to it</li><li>1224: Can't delete an enrollment policy which is set as default policy for an ADE account</li><li>7401: Can't delete default enrollment policy</li><li>7402: The deployment server failed to reach the enrollment service. Please check your network connections and settings</li><li>7405: Action can't be performed on the specified Enrollment Policy as MobiControl license is not valid.</li><li>7407: Calling the enrollment service is time out.</li></ol>

---
### PUT /enrollmentPolicies/apple/macOS/{referenceId}/actions/sync

**Summary:** Updates the specified macOS enrollment policy profile.

**Description:** This API updates the specified macOS enrollment policy profile.



         Requires the caller be granted the "Manage Enrollment Policies" permission.

**(Available since MobiControl v15.6.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Unique identifier for an enrollment policy.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>7407: Calling the enrollment service is time out.</li><li>7405: Update profile action can't be performed on the specified Enrollment Policy as MobiControl license is not valid.</li><li>7402: The deployment server failed to reach the enrollment service. Please check your network connections and settings.</li></ol>

---
### POST /enrollmentPolicies/apple/macOS/{referenceId}/actions/email

**Summary:** Emails specified macOS Enrollment Policy details.

**Description:** This API emails specified macOS Enrollment Policy details to the targeted recipient



         Requires the caller be granted the 'Manage Enrollment Policies' permission.

**(Available since MobiControl v15.6.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Unique Identifier for an Enrollment Policy.
- `request` (Required): Type: object. Description: Parameters required for dispatching email.

**Responses:**
- **204**: No Content.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>6021 - Failed to send email.</li></ol>

---
## Mac File Vault Certificate

### GET /fileVault/certificate

**Summary:** Returns the macOS Personal Recovery Key encryption certificate metadata.

**Description:** Returns the details/metadata about the certificate used for macOS FileVault Personal Recovery Key encryption.



         Requires the caller be granted the "Manage PRK Encryption Certificate" permission.

**(Available since MobiControl v15.6.2)**


**Responses:**
- **200**: Success.
- **403**: Forbidden.

---

### POST /fileVault/certificate

**Summary:** Create new Personal Recovery Key encryption certificate for FileVault.

**Description:** Create new Personal Recovery Key encryption certificate for macOS FileVault, using the p12 certificate.

Content-Type of the request body must be multipart/related; boundary={any boundary identifier}.

Multipart body request must contain the following parts:


         --&lt;boundary&gt;
         Content-Type: application/x-pkcs12.metadata+json
         {"password": "&lt;password&gt;"}


         --&lt;boundary&gt;
         Content-Type: application/x-pkcs12
         Content-Transfer-Encoding: base64
         Content-Disposition: attachment; filename="&lt;filename&gt;"
         &lt;base64 representation of the certificate file&gt;


         --&lt;boundary&gt;
         ```


**(Available since MobiControl v15.6.2)**
Requires the caller be granted the 'Manage PRK Encryption Certificate' permission.

**Responses:**
- **403**: Unauthorized access.
- **204**: Success.
- **400**: Contract validation failed.
- **415**: Unsupported content type.
- **422**: Violated logical condition. The following ErrorCode values can be returned:.<br /><ol><li>8201 - Use p12 file.</li><li>8202 - Certificate has expired. Try again with different certificate.</li><li>8203 - The password for the certificate is invalid. Please correct it and try again.</li><li>8204 - Invalid file. Please try again.</li></ol>

---
## Mail Servers

### POST /mailServers

**Summary:** Creates a New Email Server

**Description:** Creates a new mail server. Requires the caller be granted "Manage Exchange Servers" permission.

**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `server` (Required): Type: object. Description: The server to create

**Responses:**
- **200**: Successfully created the mail server '{0}'.
- **400**: Failed to create a mail server due to an invalid parameter. Please consult the Management Server logs for more information.
- **401**: Failed to create a mail server because the user from IP '{0}' is not authenticated.
- **403**: Failed to create a mail server because the user is not authorized.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:<br /><ol><li>3904 - Failed to create the mail server '{0}' because the name already exists.</li></ol>
- **500**: Failed to create a mail server due to an unexpected error. Please consult the Management Server logs for more information.

---

### GET /mailServers

**Summary:** Retrieves all mail servers

**Description:** Gets all mail servers.

**(Available Since MobiControl v15.1.0)**

**Responses:**
- **200**:
- **401**: Failed to retrieve all mail servers because the user from IP '{0}' is not authenticated.
- **403**: Failed to retrieve all mail servers because the user is not authorized.
- **500**: Failed to retrieve all mail servers due to an unexpected error. Please consult the Management Server logs for more information.

---
### DELETE /mailServers/{referenceId}

**Summary:** Deletes server entry

**Description:** Deletes the specified mail server. Requires the caller be granted "Manage Exchange Servers" permission.

**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: server identifier

**Responses:**
- **200**: Successfully deleted the mail server '{0}'.
- **400**: Failed to delete a mail server due to an invalid parameter. Please consult the Management Server logs for more information.
- **401**: Failed to delete a mail server because the user from IP 'X' is not authenticated.
- **403**: Failed to delete a mail server because the user is not authorized.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:<br /><ol><li>3910 - Failed to delete the mail server '{0}' because the server is currently used in the following compliance policies: {1}.</li></ol>
- **500**: Failed to rename a mail server due to an unexpected error. Please consult the Management Server logs for more information.

---

### GET /mailServers/{referenceId}

**Summary:** Retrieves mail server by ID

**Description:** Gets a mail server by ID.

**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `referenceId` (Required): Type: string.

**Responses:**
- **200**:
- **400**: Failed to retrieve a mail server due to an invalid parameter. Please consult the Management Server logs for more information.
- **401**: Failed to retrieve a mail server because the user from IP '{0}' is not authenticated.
- **403**: Failed to retrieve a mail server because the user is not authorized.
- **500**: Failed to retrieve a mail server due to an unexpected error. Please consult the Management Server logs for more information.

---
### POST /mailServers/exchange/certificate

**Summary:** Generates a certificate with private key

**Description:** **(Available Since MobiControl v15.3.0)**

**Responses:**
- **200**: Successfully generated a new certificate for Exchange Server connection.
- **401**: Failed to generate new Exchange Server connection certificate because the user from IP '{0}' is not authenticated.
- **403**: Failed to generate new Exchange Server connection certificate because the user is not authorized.
- **500**: Failed to generate the Exchange Server connection certificate due to an unexpected error. Please consult the Management Server logs for more information.

---
### PUT /mailServers/exchange/{referenceId}/connection

**Summary:** Updates Exchange Server connection setting

**Description:** Updates connection settings for the specified mail server. Requires the caller be granted "Manage Exchange Servers" permission.

**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Server ID
- `settings` (Required): Type: object. Description: Connection settings

**Responses:**
- **200**: Successfully updated the Exchange Server connection '{0}'.
- **400**: Failed to update an Exchange Server connection due to an invalid parameter. Please consult the Management Server logs for more information.
- **401**: Failed to update an Exchange Server connection because the user from IP '{0}' is not authenticated.
- **403**: Failed to update an Exchange Server connection because the user is not authorized.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:<br /><ol><li>3903 - Failed to update an Exchange Server connection because the mail server was not found.</li><li>3906 - Failed to update the Exchange Server connection '{0}' due to a too long password.</li><li>3908 - Failed to create the Exchange Server connection '{0}' due to a too long password.</li><li>3912 - Failed to update the Exchange Server connection '{0}' because the certificate has expired.</li><li>3913 - Failed to update the Exchange Server connection '{0}' because the certificate was not found.</li></ol>
- **500**: Failed to update an Exchange Server connection due to an unexpected error. Please consult the Management Server logs for more information.

---

### GET /mailServers/exchange/{referenceId}/connection

**Summary:** Gets Exchange Server connection settings

**Description:** Gets Exchange connection settings for the specified mail server.

**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Unique identifier for a Email Server

**Responses:**
- **200**: Return the connection settings info
- **400**: Failed to retrieve an Exchange Server connection due to an invalid parameter. Please consult the Management Server logs for more information.
- **401**: Failed to retrieve an Exchange Server connection because the user from IP '{0}' is not authenticated.
- **403**: Failed to retrieve an Exchange Server connection because the user is not authorized.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:<br /><ol><li>3903 - Failed to retrieve an Exchange Server connection because the mail server was not found.</li><li>3905 - Failed to retrieve an Exchange Server '{0}' connection due to an unknown error.</li></ol>
- **500**: Failed to retrieve an Exchange Server connection due to an unexpected error. Please consult the Management Server logs for more information.

---
### GET /mailServers/exchange/{referenceId}/publicKey

**Summary:** Retrieves the public part of a generated certificate stored in the db

**Description:** **(Available Since MobiControl v15.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string.

**Responses:**
- **200**:
- **400**: Failed to retrieve the Exchange Server connection certificate due to an invalid parameter. Please consult the Management Server logs for more information.
- **401**: Failed to retrieve the Exchange Server connection certificate because the user from IP '{0}' is not authenticated.
- **403**: Failed to retrieve the Exchange Server connection certificate because the user is not authorized.
- **500**: Failed to retrieve the Exchange Server connection certificate due to an unexpected error. Please consult the Management Server logs for more information.

---
### GET /mailServers/exchange/regions

**Summary:** Retrieves list of regions endpoints

**Description:** **(Available Since MobiControl v15.3.0)**

**Responses:**
- **200**:
- **401**: Failed to retrieve the Azure national clouds because the user from IP '{0}' is not authenticated.
- **403**: Failed to retrieve the Azure national clouds because the user is not authorized.
- **500**: Failed to retrieve the Azure national clouds due to an unexpected error. Please consult the Management Server logs for more information.

---
### PUT /mailServers/{referenceId}/name

**Summary:** Rename an existing Email Server

**Description:** Renames the specified email server. Requires the caller be granted "Manage Exchange Servers" permission.

**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Server ID
- `newName` (Required): Type: object. Description: New server name

**Responses:**
- **200**: Successfully renamed the mail server '{0}' to '{1}'.
- **400**: Failed to rename a mail server due to an invalid parameter. Please consult the Management Server logs for more information.
- **401**: Failed to rename a mail server because the user from IP '{0}' is not authenticated.
- **403**: Failed to rename a mail server because the user is not authorized.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:<br /><ol><li>3904 - Failed to rename the mail server to '{0}' because the name already exists.</li></ol>
- **500**: Failed to rename a mail server due to an unexpected error. Please consult the Management Server logs for more information.

---
### POST /mailServers/exchange/actions/test

**Summary:** Tests Exchange Server connection

**Description:** Tests the Exchange server connection using the settings specified.

**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `settings` (Required): Type: object. Description: Connection settings

**Responses:**
- **200**: Successfully tested the Exchange Server connection to '{0}'.
- **400**: Failed to test an Exchange Server connection due to an invalid parameter. Please consult the Management Server logs for more information.
- **401**: Failed to test an Exchange Server connection because the user from IP '{0}' is not authenticated.
- **403**: Failed to test an Exchange Server connection because the user is not authorized.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:<br /><ol><li>3911 - Failed to test the Exchange Server connection to '{0}' because you may not have the appropriate permissions to manage this Exchange Server.</li><li>3915 - Failed to test the Exchange Server connection to '{0}' because could not recover password from persisted connection.</li></ol>
- **500**: Failed to test an Exchange Server connection due to an unexpected error. Please consult the Management Server logs for more information.

---
### PUT /mailServers/exchange/{referenceId}/actions/test

**Summary:** Tests an existing or modified Exchange Server connection

**Description:** Tests the Exchange server connection using the settings specified.

**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Server ID
- `settings` (Required): Type: object. Description: (Optional) Updated connection settings

**Responses:**
- **200**: Successfully tested the Exchange Server connection to '{0}'.
- **400**: Failed to test an Exchange Server connection due to an invalid parameter. Please consult the Management Server logs for more information.
- **401**: Failed to test an Exchange Server connection because the user from IP '{0}' is not authenticated.
- **403**: Failed to test an Exchange Server connection because the user is not authorized.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:<br /><ol><li>3911 - Failed to test the Exchange Server connection to '{0}' because you may not have the appropriate permissions to manage this Exchange Server.</li><li>3915 - Failed to test the Exchange Server connection to '{0}' because could not recover password from persisted connection.</li></ol>
- **500**: Failed to test an Exchange Server connection due to an unexpected error. Please consult the Management Server logs for more information.

---
### GET /mailServers/{referenceId}/logs

**Summary:** Returns Management Server Logs for specific Email Server.

**Description:** This API returns the Management Server Logs for specific Email Server.


         Requires the caller be granted the "Manage Global Settings and Servers" permission.

**(Available since MobiControl v2024.0.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Unique identifier for a Email Server.
- `logSeverities`: Type: array. Description: The log severities.
- `startDate`: Type: string. Description: The start date.
- `endDate`: Type: string. Description: The end date.
- `orderByDesc`: Type: boolean. Description: if set to true [order by desc].
- `skip`: Type: integer. Description: The skip.
- `take`: Type: integer. Description: The take.

**Responses:**
- **200**: Success
- **400**: Contract validation failed
- **401**: Unauthorized access
- **403**: Forbidden

---
### GET /mailServers/{referenceId}/logs/summary

**Summary:** Fetches the count of Logs in specified Mail Server.

**Description:** API to get the count of Logs in specified Mail Server.


         Requires the caller be granted the "Manage Global Settings and Servers" permission.

**(Available since MobiControl v2024.0.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Unique identifier for a Mail Server.
- `logSeverities`: Type: array. Description: The log severities.
- `startDate`: Type: string. Description: The start date.
- `endDate`: Type: string. Description: The end date.

**Responses:**
- **200**: Success
- **400**: Contract validation failed
- **401**: Unauthorized access
- **403**: Forbidden

---
## Managed Google Play Management

### POST /android/managedGooglePlayBindings/{referenceId}/actions/{enterpriseAction}

**Summary:** Execute an action on a Managed Google Play binding.

**Description:** Sends an action to an Managed Google Play binding.
**(Available Since MobiControl v15.4.0)**

         Supported Actions:
         - Sync: Sync approved Managed Google Play Store applications with MobiControl.
Requires the caller be granted the "Manage Android Enterprise Bindings" permission.


**Parameters:**
- `referenceId` (Required): Type: string. Description: Managed Google Play binding identifier.
- `enterpriseAction` (Required): Type: string. Description: The action to be performed on the Google Domain binding.
- `productId`: Type: string. Description: ProductId to handle in case exists.

**Responses:**
- **200**: Successfully execute an action on a Managed Google Play binding.
- **401**: Unauthorized access.
- **403**: Forbidden.

---
### GET /android/managedGooglePlayBindings

**Summary:** Returns the list of Managed Google Play bindings.

**Description:** Returns the list of bindings for Managed Google Play under MobiControl.

Requires the caller be granted the "Web Console Access" permission.

**(Available Since MobiControl v15.4.0)**

**Responses:**
- **401**: Unauthorized access.
- **403**: Forbidden.
- **200**: Successfully returned list of enterprises.

---
### DELETE /android/managedGooglePlayBindings/{referenceId}

**Summary:** Deletes the binding for Managed Google Play.

**Description:** Deletes the binding for Managed Google Play under MobiControl.

Requires the caller be granted the "Manage Android Enterprise Bindings" permission.

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Identifier of the binding for Managed Google Play.

**Responses:**
- **204**: Successfully deleted the google play bindings.
- **400**: Contract validation failed.
- **401**: Unauthorized access.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>1104 - Unable to delete Enterprise Binding.&lt;exceptionMessage&gt;</li><li>1114 - Unable to delete Enterprise Binding. Please check your connectivity to SOTI Services and try again.</li><li>1115 -The Enterprise has Add Device Rules and/or App Catalog Rules associated with it and cannot be removed. Please delete the following Add Device Rules and App Catalog Rules from your server and try again:
         <br /> Add Device: &lt;addDeviceRules&gt;
         <br /> App Catalog: &lt;appCalatalogs&gt;  </li></ol>

---
### GET /android/managedGooglePlayBindings/{referenceId}/apps

**Summary:** Retrieve approved applications for a Managed Google Play binding.

**Description:** Returns a list of approved applications from the Managed Google Play Store for the provided Managed Google Play binding.

**(Available Since MobiControl v15.4.0)**
         Requires the caller be granted the "Web Console Access" permission..


**Parameters:**
- `referenceId` (Required): Type: string. Description: Managed Google Play binding identifier.
- `appName`: Type: string. Description: Application bundle id.
- `isApproved`: Type: boolean. Description: @deprecated. true if app is approved.

**Responses:**
- **200**: Returns approved applications for a Managed Google Play binding.
- **401**: Unauthorized access.
- **403**: Forbidden.

---
## Microsoft365 App Protection Policies

### POST /microsoft365/appProtectionPolicies/settings

**Summary:** Creates a new Microsoft App Protection Policy integration connection.

**Description:** Creates a new Microsoft App Protection Policy integration connection to prepare for Microsoft 365 integration.



         Requires the caller to be granted the "Manage Microsoft 365 Integration" permission.

**(Available Since MobiControl v15.6.0)**

**Parameters:**
- `settings` (Required): Type: object. Description: Microsoft App Protection Policy integration settings.

**Responses:**
- **204**: Success (No content).
- **400**: Invalid parameter.
         <ol><li>Failed to save the Microsoft App Protection Policy integration settings because it is missing in request.</li><li>Failed to save the Microsoft App Protection Policy integration settings because the name is missing.</li><li>Failed to save the Microsoft App Protection Policy integration settings because the name exceeded the 50-character limit.</li><li>Failed to save the Microsoft App Protection Policy integration settings because the Azure tenant ID is missing.</li><li>Failed to save the Microsoft App Protection Policy integration settings because the Azure tenant ID is invalid.</li></ol>
- **401**: Unauthorized Access.
- **403**: Forbidden Access.
- **422**: Violated logical condition.<br /><ol><li>8726 - Failed to save the Microsoft App Protection Policy integration settings because a connection already exists.</li></ol>

---

### GET /microsoft365/appProtectionPolicies/settings

**Summary:** Returns the Microsoft App Protection Policy integration settings.

**Description:** Retrieves Microsoft App Protection Policy integration settings to prepare for Microsoft 365 integration.



         Requires the caller to be granted the "Manage Microsoft 365 Integration" permission.

**(Available Since MobiControl v15.6.0)**

**Responses:**
- **200**: Success.
- **204**: Success (No content).
- **401**: Unauthorized Access.
- **403**: Forbidden Access.

---

### DELETE /microsoft365/appProtectionPolicies/settings

**Summary:** Deletes the Microsoft App Protection Policy integration.

**Description:** Disconnects the Microsoft App Protection Policy integration. This will delete the connection from the console and unlink your Microsoft account from MobiControl.



         Requires the caller to be granted the "Manage Microsoft 365 Integration" permission.

**(Available Since MobiControl v15.6.0)**

**Responses:**
- **204**: Success (No content).
- **401**: Unauthorized Access.
- **403**: Forbidden Access.
- **422**: Violated logical condition.<br /><ol><li>8707 - Failed to disconnect the Microsoft App Protection Policy integration because there is no connection.</li><li>8708 - Failed to disconnect the Microsoft App Protection Policy integration because of error(s). Please consult the Management Server logs for more information.</li><li>8714 - Failed to disconnect the Microsoft App Protection Policy integration because of SOTI Service communication error(s). Please consult the Management Server logs for more information.</li><li>8716 - Failed to disconnect the Microsoft App Protection Policy integration because access to SOTI Service was forbidden.</li><li>8718 - Failed to disconnect the Microsoft App Protection Policy integration because access to SOTI Service was unauthorized.</li><li>8720 - Failed to disconnect the Microsoft App Protection Policy integration because invalid request was sent to SOTI Service.</li><li>8722 - Failed to disconnect the Microsoft App Protection Policy integration because SOTI Service is unavailable.</li><li>8724 - Failed to disconnect the Microsoft App Protection Policy integration because of SOTI Service internal error(s). Please contact SOTI for support.</li></ol>

---
### GET /microsoft365/appProtectionPolicies

**Summary:** Returns a list of Microsoft App Protection policies.

**Description:** Retrieves Microsoft App Protection policies from Microsoft Endpoint Manager.



         Requires the caller to be granted the "Manage Microsoft 365 Integration" permission.

**(Available Since MobiControl v15.6.0)**

**Responses:**
- **200**: Success.
- **401**: Unauthorized Access.
- **403**: Forbidden Access.
- **422**: Violated logical condition.<br /><ol><li>8707 - Failed to retrieve Microsoft App Protection policies because there is no connection.</li><li>8708 - Failed to retrieve Microsoft App Protection policies because of error(s). Please consult the Management Server logs for more information.</li><li>8714 - Failed to retrieve Microsoft App Protection policies because of SOTI Service communication error(s). Please consult the Management Server logs for more information.</li><li>8716 - Failed to retrieve Microsoft App Protection policies because access to SOTI Service was forbidden.</li><li>8718 - Failed to retrieve Microsoft App Protection policies because access to SOTI Service was unauthorized.</li><li>8720 - Failed to retrieve Microsoft App Protection policies because invalid request was sent to SOTI Service.</li><li>8722 - Failed to retrieve Microsoft App Protection policies because SOTI Service is unavailable.</li><li>8724 - Failed to retrieve Microsoft App Protection policies because of SOTI Service internal error(s). Please contact SOTI for support.</li></ol>

---
### POST /microsoft365/appProtectionPolicies/android

**Summary:** Creates a new Microsoft App Protection policy for Android.

**Description:** Creates a new Microsoft App Protection policy for Android.



         Requires the caller to be granted the "Manage Microsoft 365 Integration" permission.

**(Available Since MobiControl v15.6.0)**

**Parameters:**
- `policy` (Required): Type: object. Description: Android App Protection policy.

**Responses:**
- **200**: Success.
- **400**: Invalid parameter.
         <ol><li>Failed to create a new Microsoft App Protection policy because the policy data is missing.</li><li>Failed to create a new Microsoft App Protection policy because the policy name is missing.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because the policy name exceeded the 100-character limit.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because the policy description exceeded the 2000-character limit.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because the policy is missing 'Disable Save As' when 'Allowed Outbound Destinations' is set to 'Policy Managed Apps'.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because the policy is missing 'Allowed Outbound Destinations' when 'Disable Save As' is true.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because the policy 'Allowed Outbound Destinations' should be set to 'Policy Managed Apps' when 'Disable Save As' is true.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because the Data Storage Location '{location}' is not supported.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because Unmanaged Web Browser data is missing.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because Unmanaged Web Browser ID is missing.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because Unmanaged Web Browser Name is missing.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because Unmanaged Web Browser ID exceeded the 200-character limit.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because Unmanaged Web Browser Name exceeded the 200-character limit.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because the PIN type 'PIN Type' is invalid.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because the minimum PIN length 'Min PIN Length' is invalid.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because Days Before Reset PIN value 'n' is not within allowable range 1-65535.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because Days Before Reset PIN value 'n' is not 0 when Reset PIN is disabled.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because Access Requirement Timeout value 'n' is not within allowable range 1-65535.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because the target group ID '{group ID}' is invalid.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because duplicate target group ID '{group ID}' found in the request.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because the policy managed apps are missing.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because of empty or invalid target application name.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because of empty or invalid target application ID.</li></ol>
- **401**: Unauthorized Access.
- **403**: Forbidden Access.
- **422**: Violated logical condition.<br /><ol><li>8709 - Failed to create the Microsoft App Protection policy '{display name}' because there is no connection.</li><li>8710 - Failed to create the Microsoft App Protection policy '{display name}' because of error(s). Please consult the Management Server logs for more information.</li><li>8715 - Failed to create the Microsoft App Protection policy '{display name}' because of SOTI Service communication error(s). Please consult the Management Server logs for more information.</li><li>8717 - Failed to create the Microsoft App Protection policy '{display name}' because access to SOTI Service was forbidden.</li><li>8719 - Failed to create the Microsoft App Protection policy '{display name}' because access to SOTI Service was unauthorized.</li><li>8721 - Failed to create the Microsoft App Protection policy '{display name}' because invalid request was sent to SOTI Service.</li><li>8723 - Failed to create the Microsoft App Protection policy '{display name}' because SOTI Service is unavailable.</li><li>8725 - Failed to create the Microsoft App Protection policy '{display name}' because of SOTI Service internal error(s). Please contact SOTI for support.</li></ol>

---
### POST /microsoft365/appProtectionPolicies/ios

**Summary:** Creates a new Microsoft App Protection policy for iOS.

**Description:** Creates a new Microsoft App Protection policy for iOS.



         Requires the caller to be granted the "Manage Microsoft 365 Integration" permission.

**(Available Since MobiControl v15.6.0)**

**Parameters:**
- `policy` (Required): Type: object. Description: iOS App Protection policy.

**Responses:**
- **200**: Success.
- **400**: Invalid parameter.
         <ol><li>Failed to create a new Microsoft App Protection policy because the policy data is missing.</li><li>Failed to create a new Microsoft App Protection policy because the policy name is missing.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because the policy name exceeded the 100-character limit.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because the policy description exceeded the 2000-character limit.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because the policy is missing 'Disable Save As' when 'Allowed Outbound Destinations' is set to 'Policy Managed Apps'.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because the policy is missing 'Allowed Outbound Destinations' when 'Disable Save As' is true.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because the policy 'Allowed Outbound Destinations' should be set to 'Policy Managed Apps' when 'Disable Save As' is true.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because the Data Storage Location '{location}' is not supported.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because Unmanaged Web Browser Protocol is missing.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because Unmanaged Web Browser Protocol exceeded the 200-character limit.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because the PIN type 'PIN Type' is invalid.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because the minimum PIN length 'Min PIN Length' is invalid.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because Days Before Reset PIN value 'n' is not within allowable range 1-65535.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because Days Before Reset PIN value 'n' is not 0 when Reset PIN is disabled.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because Access Requirement Timeout value 'n' is not within allowable range 1-65535.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because the target group ID '{group ID}' is invalid.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because duplicate target group ID '{group ID}' found in the request.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because the policy managed apps are missing.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because of empty or invalid target application name.</li><li>Failed to create the Microsoft App Protection policy '{display name}' because of empty or invalid target application ID.</li></ol>
- **401**: Unauthorized Access.
- **403**: Forbidden Access.
- **422**: Violated logical condition.<br /><ol><li>8709 - Failed to create the Microsoft App Protection policy '{display name}' because there is no connection.</li><li>8710 - Failed to create the Microsoft App Protection policy '{display name}' because of error(s). Please consult the Management Server logs for more information.</li><li>8715 - Failed to create the Microsoft App Protection policy '{display name}' because of SOTI Service communication error(s). Please consult the Management Server logs for more information.</li><li>8717 - Failed to create the Microsoft App Protection policy '{display name}' because access to SOTI Service was forbidden.</li><li>8719 - Failed to create the Microsoft App Protection policy '{display name}' because access to SOTI Service was unauthorized.</li><li>8721 - Failed to create the Microsoft App Protection policy '{display name}' because invalid request was sent to SOTI Service.</li><li>8723 - Failed to create the Microsoft App Protection policy '{display name}' because SOTI Service is unavailable.</li><li>8725 - Failed to create the Microsoft App Protection policy '{display name}' because of SOTI Service internal error(s). Please contact SOTI for support.</li></ol>

---
### DELETE /microsoft365/appProtectionPolicies/{appFamily}/{policyId}

**Summary:** Deletes the specified Microsoft App Protection policy.

**Description:** Deletes the specified Microsoft App Protection policy.



         Requires the caller to be granted the "Manage Microsoft 365 Integration" permission.

**(Available Since MobiControl v15.6.0)**

**Parameters:**
- `appFamily` (Required): Type: string. Description: App Protection policy family.
- `policyId` (Required): Type: string. Description: Policy ID.

**Responses:**
- **204**: Success (No content).
- **400**: Invalid parameter.
         <ol><li>Failed to delete the specified Microsoft App Protection policy because the policy ID is missing.</li><li>Failed to delete the specified Microsoft App Protection policy because the policy ID '{policy ID}' is invalid.</li><li>Failed to delete the specified Microsoft App Protection policy of ID '{policy ID}' because the policy family '{App family}' is not supported.</li></ol>
- **401**: Unauthorized Access.
- **403**: Forbidden Access.
- **422**: Violated logical condition.<br /><ol><li>8709 - Failed to delete the specified Microsoft App Protection policy of ID '{policy ID}' because there is no connection.</li><li>8710 - Failed to delete the specified Microsoft App Protection policy of ID '{policy ID}' because of error(s). Please consult the Management Server logs for more information.</li><li>8711 - Failed to delete the specified Microsoft App Protection policy of ID '{policy ID}' because the policy was not found.</li><li>8715 - Failed to delete the specified Microsoft App Protection policy of ID '{policy ID}' because of SOTI Service communication error(s). Please consult the Management Server logs for more information.</li><li>8717 - Failed to delete the specified Microsoft App Protection policy of ID '{policy ID}' because access to SOTI Service was forbidden.</li><li>8719 - Failed to delete the specified Microsoft App Protection policy of ID '{policy ID}' because access to SOTI Service was unauthorized.</li><li>8721 - Failed to delete the specified Microsoft App Protection policy of ID '{policy ID}' because invalid request was sent to SOTI Service.</li><li>8723 - Failed to delete the specified Microsoft App Protection policy of ID '{policy ID}' because SOTI Service is unavailable.</li><li>8725 - Failed to delete the specified Microsoft App Protection policy of ID '{policy ID}' because of SOTI Service internal error(s). Please contact SOTI for support.</li></ol>

---
### GET /microsoft365/appProtectionPolicies/azureGroups

**Summary:** Returns a list of Microsoft Azure Active Directory groups.

**Description:** Returns a list of Microsoft Azure Active Directory groups.



         Requires the caller to be granted the "Manage Microsoft 365 Integration" permission.

**(Available Since MobiControl v15.6.0)**

**Parameters:**
- `filter` (Required): Type: string. Description: Filter for group name.

**Responses:**
- **200**: Success.
- **400**: Invalid parameter.
         <ol><li>Failed to retrieve Microsoft Azure Active Directory groups summary because the filter exceeded the 120-character limit.</li></ol>
- **401**: Unauthorized Access.
- **403**: Forbidden Access.
- **422**: Violated logical condition.<br /><ol><li>8707 - Failed to retrieve Microsoft Azure Active Directory groups summary because there is no connection.</li><li>8708 - Failed to retrieve Microsoft Azure Active Directory groups summary because of error(s). Please consult the Management Server logs for more information.</li><li>8714 - Failed to retrieve Microsoft Azure Active Directory groups summary because of SOTI Service communication error(s). Please consult the Management Server logs for more information.</li><li>8716 - Failed to retrieve Microsoft Azure Active Directory groups summary because access to SOTI Service was forbidden.</li><li>8718 - Failed to retrieve Microsoft Azure Active Directory groups summary because access to SOTI Service was unauthorized.</li><li>8720 - Failed to retrieve Microsoft Azure Active Directory groups summary because invalid request was sent to SOTI Service.</li><li>8722 - Failed to retrieve Microsoft Azure Active Directory groups summary because SOTI Service is unavailable.</li><li>8724 - Failed to retrieve Microsoft Azure Active Directory groups summary because of SOTI Service internal error(s). Please contact SOTI for support.</li></ol>

---
### GET /microsoft365/appProtectionPolicies/android/{policyId}

**Summary:** Returns the specified Android App Protection policy.

**Description:** Retrieves the specified Android App Protection policy detail information from Microsoft Endpoint Manager.



         Requires the caller to be granted the "Manage Microsoft 365 Integration" permission.

**(Available Since MobiControl v15.6.0)**

**Parameters:**
- `policyId` (Required): Type: string. Description: Policy ID of the App Protection policy.

**Responses:**
- **200**: Success.
- **400**: Invalid parameter.
         <ol><li>Failed to retrieve the specified Microsoft App Protection policy information because the policy ID is missing.</li><li>Failed to retrieve the specified Microsoft App Protection policy information because the policy ID '{policy ID}' is invalid.</li></ol>
- **401**: Unauthorized Access.
- **403**: Forbidden Access.
- **422**: Violated logical condition.<br /><ol><li>8709 - Failed to retrieve the specified Microsoft App Protection policy information of ID '{policy ID}' because there is no connection.</li><li>8710 - Failed to retrieve the specified Microsoft App Protection policy information of ID '{policy ID}' because of error(s). Please consult the Management Server logs for more information.</li><li>8711 - Failed to retrieve the specified Microsoft App Protection policy information of ID '{policy ID}' because the policy was not found.</li><li>8715 - Failed to retrieve the specified Microsoft App Protection policy information of ID '{policy ID}' because of SOTI Service communication error(s). Please consult the Management Server logs for more information.</li><li>8717 - Failed to retrieve the specified Microsoft App Protection policy information of ID '{policy ID}' because access to SOTI Service was forbidden.</li><li>8719 - Failed to retrieve the specified Microsoft App Protection policy information of ID '{policy ID}' because access to SOTI Service was unauthorized.</li><li>8721 - Failed to retrieve the specified Microsoft App Protection policy information of ID '{policy ID}' because invalid request was sent to SOTI Service.</li><li>8723 - Failed to retrieve the specified Microsoft App Protection policy information of ID '{policy ID}' because SOTI Service is unavailable.</li><li>8725 - Failed to retrieve the specified Microsoft App Protection policy information of ID '{policy ID}' because of SOTI Service internal error(s). Please contact SOTI for support.</li></ol>

---

### PUT /microsoft365/appProtectionPolicies/android/{policyId}

**Summary:** Updates the specified Android App Protection policy.

**Description:** Updates the specified Android App Protection policy.



         Requires the caller to be granted the "Manage Microsoft 365 Integration" permission.

**(Available Since MobiControl v15.6.0)**

**Parameters:**
- `policyId` (Required): Type: string. Description: App Protection policy Id.
- `policy` (Required): Type: object. Description: App Protection policy to be updated.

**Responses:**
- **204**: Success (No content).
- **400**: Invalid parameter.
         <ol><li>Failed to update the specified Microsoft App Protection policy because the policy ID is missing or invalid.</li><li>Failed to update the specified Microsoft App Protection policy because the policy data is missing.</li><li>Failed to update the specified Microsoft App Protection policy because the policy name is missing.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because the policy name exceeded the 100-character limit.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because the policy description exceeded the 2000-character limit.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because the policy is missing 'Disable Save As' when 'Allowed Outbound Destinations' is set to 'Policy Managed Apps'.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because the policy is missing 'Allowed Outbound Destinations' when 'Disable Save As' is true.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because the policy 'Allowed Outbound Destinations' should be set to 'Policy Managed Apps' when 'Disable Save As' is true.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because the Data Storage Location '{location}' is not supported.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because Unmanaged Web Browser data is missing.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because Unmanaged Web Browser ID is missing.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because Unmanaged Web Browser Name is missing.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because Unmanaged Web Browser ID exceeded the 200-character limit.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because Unmanaged Web Browser Name exceeded the 200-character limit.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because the PIN type 'PIN Type' is invalid.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because the minimum PIN length 'Min PIN Length' is invalid.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because Days Before Reset PIN value 'n' is not within allowable range 1-65535.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because Days Before Reset PIN value 'n' is not 0 when Reset PIN is disabled.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because Access Requirement Timeout value 'n' is not within allowable range 1-65535.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because the target group ID '{group ID}' is invalid. </li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because duplicate target group ID '{group ID}' found in the request.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because the policy managed apps are missing.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because of empty or invalid target application name.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because of empty or invalid target application ID.</li></ol>
- **401**: Unauthorized Access.
- **403**: Forbidden Access.
- **422**: Violated logical condition.<br /><ol><li>8709 - Failed to update the specified Microsoft App Protection policy '{display name}' because there is no connection.</li><li>8710 - Failed to update the specified Microsoft App Protection policy '{display name}' because of error(s). Please consult the Management Server logs for more information.</li><li>8711 - Failed to update the specified Microsoft App Protection policy '{display name}' because the policy was not found.</li><li>8715 - Failed to update the specified Microsoft App Protection policy '{display name}' because of SOTI Service communication error(s). Please consult the Management Server logs for more information.</li><li>8717 - Failed to update the specified Microsoft App Protection policy '{display name}' because access to SOTI Service was forbidden.</li><li>8719 - Failed to update the specified Microsoft App Protection policy '{display name}' because access to SOTI Service was unauthorized.</li><li>8721 - Failed to update the specified Microsoft App Protection policy '{display name}' because invalid request was sent to SOTI Service.</li><li>8723 - Failed to update the specified Microsoft App Protection policy '{display name}' because SOTI Service is unavailable.</li><li>8725 - Failed to update the specified Microsoft App Protection policy '{display name}' because of SOTI Service internal error(s). Please contact SOTI for support.</li></ol>

---
### GET /microsoft365/appProtectionPolicies/ios/{policyId}

**Summary:** Returns the specified iOS App Protection policy.

**Description:** Retrieves the specified iOS App Protection policy detail information from Microsoft Endpoint Manager.



         Requires the caller to be granted the "Manage Microsoft 365 Integration" permission.

**(Available Since MobiControl v15.6.0)**

**Parameters:**
- `policyId` (Required): Type: string. Description: Policy ID of the App Protection policy.

**Responses:**
- **200**: Success.
- **400**: Invalid parameter.
         <ol><li>Failed to retrieve the specified Microsoft App Protection policy information because the policy ID is missing.</li><li>Failed to retrieve the specified Microsoft App Protection policy information because the policy ID '{policyId}' is invalid.</li></ol>
- **401**: Unauthorized Access.
- **403**: Forbidden Access.
- **422**: Violated logical condition.<br /><ol><li>8709 - Failed to retrieve the specified Microsoft App Protection policy information of ID '{policy ID}' because there is no connection.</li><li>8710 - Failed to retrieve the specified Microsoft App Protection policy information of ID '{policy ID}' because of error(s). Please consult the Management Server logs for more information.</li><li>8711 - Failed to retrieve the specified Microsoft App Protection policy information of ID '{policy ID}' because the policy was not found.</li><li>8715 - Failed to retrieve the specified Microsoft App Protection policy information of ID '{policy ID}' because of SOTI Service communication error(s). Please consult the Management Server logs for more information.</li><li>8717 - Failed to retrieve the specified Microsoft App Protection policy information of ID '{policy ID}' because access to SOTI Service was forbidden.</li><li>8719 - Failed to retrieve the specified Microsoft App Protection policy information of ID '{policy ID}' because access to SOTI Service was unauthorized.</li><li>8721 - Failed to retrieve the specified Microsoft App Protection policy information of ID '{policy ID}' because invalid request was sent to SOTI Service.</li><li>8723 - Failed to retrieve the specified Microsoft App Protection policy information of ID '{policy ID}' because SOTI Service is unavailable.</li><li>8725 - Failed to retrieve the specified Microsoft App Protection policy information of ID '{policy ID}' because of SOTI Service internal error(s). Please contact SOTI for support.</li></ol>

---

### PUT /microsoft365/appProtectionPolicies/ios/{policyId}

**Summary:** Updates the specified iOS App Protection policy.

**Description:** Updates the specified iOS App Protection policy.



         Requires the caller to be granted the "Manage Microsoft 365 Integration" permission.

**(Available Since MobiControl v15.6.0)**

**Parameters:**
- `policyId` (Required): Type: string. Description: App Protection policy Id.
- `policy` (Required): Type: object. Description: App Protection policy to be updated.

**Responses:**
- **204**: Success (No content).
- **400**: Invalid parameter.
         <ol><li>Failed to update the specified Microsoft App Protection policy because the policy data is missing.</li><li>Failed to update the specified Microsoft App Protection policy because the policy name is missing.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because the policy name exceeded the 100-character limit.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because the policy description exceeded the 2000-character limit.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because the policy is missing 'Disable Save As' when 'Allowed Outbound Destinations' is set to 'Policy Managed Apps'.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because the policy is missing 'Allowed Outbound Destinations' when 'Disable Save As' is true.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because the policy 'Allowed Outbound Destinations' should be set to 'Policy Managed Apps' when 'Disable Save As' is true.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because the Data Storage Location '{location}' is not supported.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because Unmanaged Web Browser Protocol is missing.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because Unmanaged Web Browser Protocol exceeded the 200-character limit.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because the PIN type 'PIN Type' is invalid.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because the minimum PIN length 'Min PIN Length' is invalid.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because Days Before Reset PIN value 'n' is not within allowable range 1-65535.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because Days Before Reset PIN value 'n' is not 0 when Reset PIN is disabled.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because Access Requirement Timeout value 'n' is not within allowable range 1-65535.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because the target group ID '{group ID}' is invalid.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because duplicate target group ID '{group ID}' found in the request.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because the policy managed apps are missing.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because of empty or invalid target application name.</li><li>Failed to update the specified Microsoft App Protection policy '{display name}' because of empty or invalid target application ID.</li></ol>
- **401**: Unauthorized Access.
- **403**: Forbidden Access.
- **422**: Violated logical condition.<br /><ol><li>8709 - Failed to update the specified Microsoft App Protection policy '{display name}' because there is no connection.</li><li>8710 - Failed to update the specified Microsoft App Protection policy '{display name}' because of error(s). Please consult the Management Server logs for more information.</li><li>8711 - Failed to update the specified Microsoft App Protection policy '{display name}' because the policy was not found.</li><li>8715 - Failed to update the specified Microsoft App Protection policy '{display name}' because of SOTI Service communication error(s). Please consult the Management Server logs for more information.</li><li>8717 - Failed to update the specified Microsoft App Protection policy '{display name}' because access to SOTI Service was forbidden.</li><li>8719 - Failed to update the specified Microsoft App Protection policy '{display name}' because access to SOTI Service was unauthorized.</li><li>8721 - Failed to update the specified Microsoft App Protection policy '{display name}' because invalid request was sent to SOTI Service.</li><li>8723 - Failed to update the specified Microsoft App Protection policy '{display name}' because SOTI Service is unavailable.</li><li>8725 - Failed to update the specified Microsoft App Protection policy '{display name}' because of SOTI Service internal error(s). Please contact SOTI for support.</li></ol>

---
## Microsoft365 Conditional Access

### GET /microsoft365/conditionalAccess/settings

**Summary:** Gets Latest Microsoft 365 Integration Status.

**Description:** Returns Microsoft 365 Integration status and the time when the last sync time.Requires the caller to be granted the "Manage Microsoft 365 Integration" permission.

**(Available Since MobiControl v15.5.0)**

**Responses:**
- **200**: Success.
- **204**: Success(No content).
- **403**: User is not authorized or reference does not exist.

---

### POST /microsoft365/conditionalAccess/settings

**Summary:** Updates Microsoft 365 Integration Credentials.

**Description:** Updates the Azure Tenant ID to prepare for Microsoft 365 Integration. Requires the caller to be granted the "Manage Microsoft 365 Integration" permission.

**(Available Since MobiControl v15.5.0)**

**Parameters:**
- `settings` (Required): Type: object. Description: Microsoft 365 Integration Credentials.

**Responses:**
- **204**: Success.
- **400**: Bad request due to invalid parameters.
- **403**: User is not authorized or reference does not exist.
- **422**: Violated logical condition. The following ErrorCode values can be returned.<br /><ol><li>8700 - The tenant already exists</li></ol>

---
### POST /microsoft365/conditionalAccess/onboarding

**Summary:** Initiates the Microsoft 365 Integration.

**Description:** Initiates the Microsoft 365 Integration, the user will be prompted to log in and accept permissions for the SOTI MobiControl Device Compliance application on the Microsoft Azure portal. Requires the caller to be granted the "Manage Microsoft 365 Integration" permission.

**(Available Since MobiControl v15.5.0)**

**Responses:**
- **204**: Success.
- **403**: User is not authorized or reference does not exist.
- **422**: Violated logical condition. The following ErrorCode values can be returned.<br /><ol><li>8701 - Failed to initiate the Microsoft 365 Integration because the connection failed.</li><li>8704 - Failed to initiate the Microsoft 365 Integration because there is no account found.</li></ol>

---
### POST /microsoft365/conditionalAccess/offboarding

**Summary:** Deletes the Microsoft 365 Integration.

**Description:** Deletes the Microsoft 365 Integration, this will permanently delete Name from the console and unlink your Microsoft account from MobiControl. Requires the caller to be granted the "Manage Microsoft 365 Integration" permission.

**(Available Since MobiControl v15.5.0)**

**Responses:**
- **204**: Success.
- **403**: User is not authorized or reference does not exist.
- **422**: Violated logical condition. The following ErrorCode values can be returned.<br /><ol><li>8702 -  Failed to delete the Microsoft 365 Integration because the account is being used by one or more Compliance Policies.</li><li>8703 -  Failed to delete the Microsoft 365 Integration because there is no account found.</li><li>8705 -  Failed to delete the Microsoft 365 Integration because the connection failed.</li><li>8706 -  Failed to delete the Microsoft 365 Integration because there are pending actions involving the account that are being processed.</li><li>8730 -  Failed to delete the Microsoft 365 Integration because the account is being used by a Microsoft Single Sign-On connection.</li><li>8731 -  Failed to delete the Microsoft 365 Integration because there are active devices registered in Azure.</li></ol>

---
## Microsoft365 Mobile Apps

### GET /microsoft365/mobileApps

**Summary:** Returns a list of Microsoft Azure managed applications.

**Description:** Returns a list of Microsoft Azure Application(s).



         Requires the caller to be granted the "Manage Microsoft 365 Integration" permission.

**(Available Since MobiControl v2024.0.0)**

**Parameters:**
- `filter` (Required): Type: string. Description: Filter for application name.
- `appFamily` (Required): Type: string. Description: Application family.

**Responses:**
- **200**: Success.
- **400**: Invalid parameter.
         <ol><li>Failed to retrieve Microsoft Azure application(s) because the filter exceeded the 120-character limit.</li></ol>
- **401**: Unauthorized Access.
- **403**: Forbidden Access.
- **422**: Violated logical condition.<br /><ol><li>8707 - Failed to retrieve Microsoft Azure application(s) because there is no connection.</li><li>8708 - Failed to retrieve Microsoft Azure application(s) because of error(s). Please consult the Management Server logs for more information.</li><li>8714 - Failed to retrieve Microsoft Azure application(s) because of SOTI Service communication error(s). Please consult the Management Server logs for more information.</li><li>8716 - Failed to retrieve Microsoft Azure application(s) because access to SOTI Service was forbidden.</li><li>8718 - Failed to retrieve Microsoft Azure application(s) because access to SOTI Service was unauthorized.</li><li>8720 - Failed to retrieve Microsoft Azure application(s) because invalid request was sent to SOTI Service.</li><li>8722 - Failed to retrieve Microsoft Azure application(s) because SOTI Service is unavailable.</li><li>8724 - Failed to retrieve Microsoft Azure application(s) because of SOTI Service internal error(s). Please contact SOTI for support.</li></ol>

---
## Packages

### GET /packages

**Summary:** Retrieve a List of Packages

**Description:** Returns a list of all packages in the system including versions of a package. Requires the caller be granted the "View Packages" permission.
**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `deviceFamilies`: Type: string. Description: Only return packages that are targeting one of the families in this list. Provided as a comma-separated list of Device Family. To get list of All packages user needs to leave device families as blank or pass all device families as comma separated.
- `packageName`: Type: string. Description: Package Name search string
- `Order`: Type: array.
- `Skip`: Type: integer.
- `Take`: Type: integer.

**Responses:**
- **200**: A list of packages

---

### POST /packages

**Summary:** Upload Package

**Description:**

**Packages**




**(Available Since MobiControl v14.0.0)**

Uploads a new package (*.pcg file), or a new version of an existing package. A new version of an existing package will be created when the name of the upload package matches an existing package, and when the version of the new package is greater than the existing package version. Requires the caller be granted the "Manage Packages" permission.

Content-Type of the Request body must be <code>multipart/related; boundary={boundary identifier}</code>
Boundary length must be set to less than or equal to 11 to prevent internal server errors.
Multipart request body must contain the following parts:
- package metadata - Contains json-formatted package information with Content-Type:
application/vnd.soti.mobicontrol.package.metadata+json```
- package file - Contains binary package file with Content-Type:
application/vnd.soti.mobicontrol.package```

Optional headers
Content-Transfer-Encoding: binary
Content-Disposition: attachment; filename="{package-filename}"

Request Metadata
{"DeviceFamily" : "AndroidPlus"}
Currently, the maximum size of package file to be uploaded when using this endpoint is <u>2 GB</u>.

The example below shows package upload request.

Content-Type: multipart/related; boundary=foo_bar_baz Content-Length: number_of_bytes_in_entire_request_body
--foo_bar_baz Content-Type: application/vnd.soti.mobicontrol.package.metadata+json
{ "DeviceFamily" : "AndroidPlus" }
--foo_bar_baz Content-Type: application/vnd.soti.mobicontrol.package Content-Transfer-Encoding: Binary Content-Disposition: attachment; filename="package_file_name.pcg"
Binary package data --foo_bar_baz--```


**Applications**

**(Available Since MobiControl v15.0.0)**
In addition to upload package, this interface also uploads an Android application (.apk file) by converting it into a package (.pcg file). If the name and version for the package are not provided, then the name and version will be generated from the manifest file of the Android application (.apk file). A new version of an existing package will be created when the name of the upload Android application file matches an existing package, and when the version of the new Android application file is greater than the existing package version. Requires the caller be granted the "Manage Packages" permission.


Content-Type of the Request body must be <code>multipart/related; boundary={boundary identifier}</code>
Boundary length must be set to less than or equal to 11 to prevent internal server errors.
Multipart request body must contain the following parts:
- application metadata - Contains json-formatted application information with Content-Type:
application/vnd.android.application.metadata+json```
- application file - Contains application file with Content-Type:
application/vnd.android.application```

Optional headers
Content-Transfer-Encoding: binary
Content-Disposition: attachment; filename="{application-filename}"

Request Metadata
{"DeviceFamily" : "AndroidPlus", "PackageName": "package", "PackageVersion": "1.0"}
The "PackageName" and "PackageVersion" are optional parameters.
Currently, the maximum size of package file or the Android application file to be uploaded when using this endpoint is <u>2 GB</u>.

The example below shows application upload request.

Content-Type: multipart/related; boundary=foo_bar_baz Content-Length: number_of_bytes_in_entire_request_body
--foo_bar_baz Content-Type: application/vnd.android.application.metadata+json
{ "DeviceFamily" : "AndroidPlus", "PackageName": "package", "PackageVersion": "1.0"}
--foo_bar_baz Content-Type: application/vnd.android.application
Content-Disposition: attachment; filename="application_name.apk"
application data --foo_bar_baz--```


**Responses:**
- **200**: Package created successfully
- **400**: Bad request, ie. Invalid application or package file contents or metadata
- **401**: Unauthorized
- **415**: Unsupported content media type
- **422**: Package verification failure, ie. Invalid Application or Package Platform or Version

---
### GET /packages/{referenceId}/versions

**Summary:** Retrieves Versions of a Package

**Description:** Returns a list of versions for a package identified by its reference ID. Requires the caller be granted the "View Packages" permission.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The Reference ID

**Responses:**
- **200**: The package versions

---
### GET /packages/{referenceId}

**Summary:** Retrieve a Package

**Description:** Returns a package in the system including last version of a package. Requires the caller be granted the "View Packages" permission.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The Reference ID

**Responses:**
- **200**: package

---

### DELETE /packages/{referenceId}

**Summary:** Delete Package with its all versions

**Description:** Delete Package with its all versions.
**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: reference id of package

**Responses:**
- **204**:

---
### POST /packages/v2

**Summary:** Upload package metadata, package files and script files for multiple platforms to generate a Package

**Description:**

**Packages**




**(Available Since MobiControl v15.3.0)**

Uploads package creation metadata, package script files (i.e. pre-install/post-install/pre-uninstall/post-uninstall), package files, package prompt. A new version of Package will be created/generated and stored in Mobicontrol. Requires the caller to be granted the "Manage Packages" permission.

Content-Type of the Request body must be <code>multipart/related; boundary={boundary identifier}</code>
Boundary length must be set to less than or equal to 11 to prevent internal server errors.
Multipart request body must contain the following parts:
- package metadata - Contains json-formatted package information with Content-Type:
application/vnd.soti.mobicontrol.packagearchive.metadata+json
OR
application/vnd.soti.mobicontrol.packagearchive.metadata```
- script file - Contains binary script file with Content-Type:
application/octet-stream```
- package file - Contains binary package file with Content-Type:
application/octet-stream```

Optional headers
Content-Transfer-Encoding: binary
Content-Disposition: attachment; filename="{package-filename}"

**Request Metadata**
**PackageName** field is a required field with maximum length of 100 characters.
**PackageVersion** is a required field and denotes version and is a required field.
**PackagePlatform** is a required field and can have possible values - Android/AndroidPlus/Linux/WindowsDesktop/WindowsCE/WindowsModern/Printer
**AdditionalSize** is a optional field and can have integer value
**ScriptFiles** is a optional field and is a array of script file objects.
**PackageFiles** is a required field and is array of package file objects.
**PackagePrompt** is a optional field that represents object with properties for Package Message Prompt.

**ScriptFile Object** is json object with following format

{ "FileName":"PostInstallScript.cmd", "ScriptTrigger":"PostInstall", "FileSourceType":"Binary" } ```
<dl><dt>**FileName**</dt><dd>FileName field is required while adding a script file and is used to for setting the file name in package.</dd><dt>**ScriptTrigger**</dt><dd>ScriptTrigger field is required while adding a script file and can have possible value of PreInstall / PostInstall / PreUnInstall / PostUnInstall.</dd><dt>**FileSourceType**</dt><dd>FileSourceType field is required while adding a script file and can have possible value of Binary / Url.</dd></dl>

**PackageFile Object** is json object with following format

{ "FileName":"Books.apk", "FileSourceType":"Binary" }  ```
<dl><dt>**FileName**</dt><dd>FileName field is required while adding a package file and is used to for setting the file name in package.</dd><dt>**FileSourceType**</dt><dd>FileSourceType field is required while adding a script file and can have possible value of Binary / Url.</dd></dl>

**PackagePrompt Object** is json object with following format

{ "ShowPromptBeforeInstall": false, "PromptMessage":"Install package PackageName now?", "PromptMessageTimeout":10 }```
<dl><dt>**ShowPromptBeforeInstall**</dt><dd>ShowPromptBeforeInstall is optional field which can have possible values true / false.</dd><dt>**PromptMessage**</dt><dd>PromptMessage is optional field and can have alphanumeric character upto 130 characters.</dd><dt>**PromptMessageTimeout**</dt><dd>PromptMessageTimeout is optional field and can have value between 10 seconds to 300 seconds. Defaults to 10 seconds.</dd></dl>

Currently, the maximum size of package file to be uploaded when using this endpoint is <u>2 GB</u>.

The example below shows package upload request.

Content-Type: multipart/related; boundary=foo_bar_baz Content-Length: number_of_bytes_in_entire_request_body

--foo_bar_baz
Content-Type: application/vnd.soti.mobicontrol.packagearchive.metadata+json

{
"PackageName":"Test Package 1", "PackageVersion":"6.4.0", "PackagePlatform":"Android", "AdditionalSize":"1024",
"ScriptFiles": [{ "FileName":"PreInstallScripts.cmd", "ScriptTrigger": "PreInstall", "FileSourceType": "Binary" },
		   { "FileName":"PostInstallScript.cmd", "ScriptTrigger":"PostInstall", "FileSourceType":"Binary" },
		   { "FileName":"PreUninstallScript.cmd", "ScriptTrigger":"PreUninstall", "FileSourceType":"Binary" },
		   { "FileName":"PostUninstallScript.cmd", "ScriptTrigger":"PostUninstall", "FileSourceType":"Binary" }
	     ],
"PackageFiles": [{ "FileName":"Books.apk", "FileSourceType":"Binary" } ],
"PackagePrompt": { "ShowPromptBeforeInstall": false, "PromptMessage":"Install package PackageName now?", "PromptMessageTimeout":10 }
}

--foo_bar_baz
Content-Type: application/octet-stream
Content-Transfer-Encoding: Binary
Content-Disposition: attachment; filename="PreInstall.cmd"

Binary package script file for pre install

--foo_bar_baz
Content-Type: application/octet-stream
Content-Transfer-Encoding: Binary
Content-Disposition: attachment; filename="PostInstall.cmd"

Binary package script file for post install

--foo_bar_baz
Content-Type: application/octet-stream
Content-Transfer-Encoding: Binary
Content-Disposition: attachment; filename="PreUnInstall.cmd"

Binary package script file for pre uninstall

--foo_bar_baz
Content-Type: application/octet-stream
Content-Transfer-Encoding: Binary
Content-Disposition: attachment; filename="PostUnInstall.cmd"

Binary package script file for post uninstall

--foo_bar_baz
Content-Type: application/octet-stream
Content-Transfer-Encoding: Binary
Content-Disposition: attachment; filename="chrome.apk"

Binary package file e.g. apk, exe, reg, cab

--foo_bar_baz--```



**Responses:**
- **200**: Package created successfully
- **400**: Bad request, ie. Invalid application or package file contents or metadata
- **401**: Unauthorized
- **415**: Unsupported content media type
- **422**: Package verification failure, ie. Invalid Application or Package Platform or Version

---
### GET /packages/job/{referenceId}

**Summary:** Retrieve a Package Job which contains status of the Package Creation/Generation

**Description:** Returns a package generation job in the system. Requires the caller be granted the "View Packages" permission. Currently there is a limitation on fetching the completed jobs. The endpoint returns inprogress jobs and pending jobs. For completed jobs, please check packages under MobiControl UI - Packages Tab.
**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The Job Reference ID

**Responses:**
- **200**: Package Generation Job

---
### GET /packages/DownloadGeneralFile/{fileName}

**Summary:** Downloads any type of general types

**Description:** Download any general file type identified by the file name eg: McStudio.exe
**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `fileName` (Required): Type: string. Description: File Name

**Responses:**
- **403**: Unauthorized access or the file does not exist
- **200**: Returns the expected file

---
### DELETE /packages/{referenceId}/versions/{versionString}

**Summary:** Delete Package version

**Description:** Delete Package version.
**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: reference id of package
- `versionString` (Required): Type: string. Description: version string of package
- `buildVersion` (Required): Type: string. Description: build version of package

**Responses:**
- **204**:

---
### GET /packages/{referenceId}/profileStatuses

**Summary:** Retrieve a List of Profiles by Package

**Description:** Returns a list of profile status for a package. Requires the caller be granted the "View Package" and "View Profile" global permission.
**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description:
- `versionString`: Type: string. Description:

**Responses:**
- **200**:

---
### GET /packages/{referenceId}/logs

**Summary:** Get Package Logs

**Description:** Returns a list of logs associated with a package. Requires the caller be granted the "View Packages" global permission.
**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The package identifier
- `startDate` (Required): Type: string. Description: The start date. Example: 2015-12-19T16:39:57-02:00
- `endDate` (Required): Type: string. Description: The end date. Example: 2015-12-19T16:39:57-02:00
- `version`: Type: string. Description: Version of Package
- `logSeverities`: Type: array. Description: List of log severities to include into result set
- `Order`: Type: array.
- `Skip`: Type: integer.
- `Take`: Type: integer.

**Responses:**
- **200**: Returns a list of a logs based on a package reference id and version
- **403**: Unauthorized access or package reference does not exist

---
### GET /packages/{referenceId}/logs/summary

**Summary:** Get Package Logs

**Description:** Returns logs summary associated with a package. Requires the caller be granted the "View Packages" global permission.
**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The package identifier
- `startDate` (Required): Type: string. Description: The start date. Example: 2015-12-19T16:39:57-02:00
- `endDate` (Required): Type: string. Description: The end date. Example: 2015-12-19T16:39:57-02:00
- `version`: Type: string. Description: Version of Package

**Responses:**
- **200**: Returns a list of a logs based on a package reference id and version
- **403**: Unauthorized access or package reference does not exist

---
### GET /packages/{referenceId}/executionStatuses/{versionString}

**Summary:** Retrieve a List of Execution Status by Package

**Description:** Returns a list of profile status for a package. Requires the caller be granted the "View Package" global permission.
**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The package identifier
- `versionString` (Required): Type: string. Description: Version of Package

**Responses:**
- **200**:

---
### GET /packages/{referenceId}/version/{version}/download

**Summary:** Download Package of selected Version

**Description:** Download Package of selected Version
**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The Package identifier
- `version` (Required): Type: string. Description: Version of Package

**Responses:**
- **200**:

---
## Product

### PUT /product/registrationCode

**Summary:** Set Product Registration Code

**Description:** Sets a product registration code and activates product with SOTI Services. No authorization is required for this endpoint while the product is unlicensed/unregistered or a previous registration code has expired. Once successfully activated, and unauthorized attempt to call this endpoint will fail.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `registrationCode` (Required): Type: object. Description: The registration data

**Responses:**
- **204**: Product was successfully activated
- **400**: Bad request, i.e. missing or invalid registration code
- **403**: Forbidden, authorization is required to use this method if product was registered before
- **422**: Product activation failed, see error message for details

---
### PUT /product/licenceFile

**Summary:** Uploads and Sets Offline Product License File

**Description:** Uploads and sets a product license file when access to SOTI Services for product registration is not possible. No authorization is required for this endpoint while the product is unlicensed/unregistered or a previous registration code has expired. Once successfully activated, and unauthorized attempt to call this endpoint will fail.
**(Available Since MobiControl v14.0.0)**

Content-Type of the Request body must be <code>multipart/related; boundary={boundary identifier}</code>
Boundary length must be set to less than or equal to 11 to prevent internal server errors.
Multipart request body must contain the following parts:
Optional headers
Content-Type-Encoding: base64
Content-Disposition: attachment; filename="{license-filename}"


The example below shows offline activation request.

Content-Type: multipart/related; boundary=foo_bar_baz Content-Length: number_of_bytes_in_entire_request_body
--foo_bar_baz Content-Type: text/xml Content-Type-Encoding: base64 Content-Disposition: attachment; filename="license.xml"
Base64-encoded license data --foo_bar_baz--```

Note: No authorization is required to set license file after installation of a new product or expiry of a previous registration code. Once product is successfully activated, an unauthorized attempt to set license file will fail.


**Responses:**
- **204**: Product was successfully activated
- **400**: Bad request, i.e. missing or invalid license file
- **403**: Forbidden, authorization is required to use this method if product was registered before
- **415**: Unsupported content media type
- **422**: Product activation failed, see error message for details

---
### GET /product/eula

**Summary:** Retrieve Text of MobiControl EULA

**Description:** Retrieve the text of the MobiControl End User License Agreement for the current version.
**(Available Since MobiControl v14.0.0)**

**Responses:**
- **200**: The text of the End User License Agreement was returned successfully
- **403**: Forbidden, authorization is required to use this method

---
## Profiles

### GET /profiles

**Summary:** Get a List of Profiles

**Description:** Returns a list of all profiles in the system. Requires the caller be granted the "View Profiles" global permission. Results will be limited to profiles where the caller is granted at least the "Read" profile-specific permission.

Note: For "DeviceFamily" in the response, "Blackberry", "Scanner", and "WindowsRuntime" are deprecated. "WindowsPhone" is for all Windows Modern devices.

**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `NameContains`: Type: string. Description: Only return profiles whose name contains this value. Must
be URL-encoded when using special characters (e.g.
a/profilename - a%2fprofilename). When called from this
page, it should not be encoded (a/profilename).
- `WithStatuses`: Type: string. Description: Only return profiles that have statuses that match one of the
values in this list. Provided as a comma-separated list of
ProfileVersionStatus values.
- `ForFamilies`: Type: string. Description: Only return profiles that are targeting one of the families
in this list. Provided as a comma-separated list of
DeviceFamily values.
- `HasDraft`: Type: boolean. Description: Only return profiles that have a current draft. When false,
only return profiles that do not have a draft. If null, then
do not take draft status into account
- `HasSchedule`: Type: boolean. Description: Only return profiles that currently have a schedule. When false,
only return profiles that do not have a schedule. If null, then
do not take schedule status into account
- `AutoInstallOnly`: Type: boolean. Description: Only return profiles that are automatically installed.
When false, this only returns profiles that are self-installed.
If null, then do not take install method into account.
- `Order`: Type: array.
- `Skip`: Type: integer.
- `Take`: Type: integer.

**Responses:**
- **200**: Returns a list of profiles
- **403**: Unauthorized access or profile reference does not exist

---

### POST /profiles

**Summary:** Creates a New Profile

**Description:** Creates a new profile in the system. Requires the caller be granted the "Manage Profiles" global permission.

Note: For "DeviceFamily" in the response, "Blackberry", "Scanner", and "WindowsRuntime" are deprecated. "WindowsPhone" is for all Windows Modern devices.

**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `profileRequest` (Required): Type: object. Description: The details of the profile to be created

**Responses:**
- **200**: Returns the newly created profile
- **400**: Contract validation failed
- **403**: Unauthorized access
- **422**: Profile request validation failed

---
### PUT /profiles/{referenceId}/packages

**Summary:** Add Packages to Profile

**Description:** Add packages to a profile in the system.
         Requires the caller be granted the "Manage Profiles" global permission.

Note: For "DeviceFamily" in the response, "Blackberry", "Scanner", and "WindowsRuntime" are deprecated. "WindowsPhone" is for all Windows Modern devices.

**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference Id of the profile
- `packageInfos` (Required): Type: object. Description: The package info collection to be added to the profile

**Responses:**
- **200**: Returns the profile that the package is added to
- **403**: Unauthorized access or profile reference does not exist
- **422**: Request validation failed

---

### GET /profiles/{referenceId}/packages

**Summary:** Get Package Info of a Profile

**Description:** Returns a list of packages associated with a profile.
         Requires the caller be granted the "View Profiles" global permission.
         Supported sort fields: InstallationOrder, ReferenceId, Version, Name, Size.

**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference Id of the profile
- `Order`: Type: array.
- `Skip`: Type: integer.
- `Take`: Type: integer.

**Responses:**
- **200**: Returns a list of packages based on a profile reference id
- **403**: Unauthorized access or profile reference does not exist

---
### PUT /profiles/{referenceId}/assignment

**Summary:** Assign the Profile

**Description:** Assigns a profile to target groups or devices. Requires the caller be granted the "Manage Profiles" global permissions and the "Read and Write" profile-specific permission.

Only the following filter properties are supported:
         - OSVersion- Manufacturer- Model- Family- PasscodeEnabled- IsEncrypted- IsSupervised- LastAgentConnectTime- LastAgentDisconnectTime- IsAgentOnline- PrinterAdminServer.Name- Memory.TotalMemory- Memory.AvailableMemory- Memory.TotalStorage- Memory.AvailableStorage- Memory.TotalExternalStorage- Memory.AvailableExternalStorage- SIMCarrierNetwork- CellularCarrier- SelectedApn- SupportedApis- OEMVersion (Android / Android+ only)- HAS APPLICATION- HAS UserGroup
The syntax for HAS APPLICATION and HAS UserGroup is different from the device filters.

HAS APPLICATION Examples:
         - HAS APPLICATION WITH (NAME = 'AngryBirds')- NOT HAS APPLICATION WITH (NAME = 'AngryBirds')- HAS APPLICATION WITH (NAME = 'AngryBirds' AND VERSION = '3.2.1')- HAS APPLICATION WITH (NAME = 'AngryBirds' AND VERSION &gt;&lt; '3.2.1')- HAS APPLICATION WITH (NAME = 'AngryBirds' AND VERSION &gt; '1.2.1')- HAS APPLICATION WITH (NAME = 'AngryBirds' AND VERSION &gt;= '1.2.1')- HAS APPLICATION WITH (NAME = 'AngryBirds' AND VERSION &lt; '8.1')- HAS APPLICATION WITH (NAME = 'AngryBirds' AND VERSION &lt;= '8.1')- HAS APPLICATION WITH (NAME = 'AngryBirds' AND VERSION BETWEEN '8.1' AND '10')
HAS UserGroup examples when filtering directory service groups (i.e. LDAP or Azure AD):
         - HAS UserGroup WITH (Name = 'Sales' AND ConnectionName = 'LdapConn1')- HAS UserGroup WITH (Sid = '1111-1111-1111-1111')
HAS UserGroup examples when filtering IdP groups:
         - HAS UserGroup WITH (IdPGroupName = 'Sales' AND IdPConnectionName = 'SSO_Connection1')
Note: For "Family" in the response, "Blackberry", "Scanner", and "WindowsRuntime" are deprecated. "WindowsPhone" is for all Windows Modern devices.


**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference Id of the profile
- `profileAssignment` (Required): Type: object. Description: The profile assignment details

**Responses:**
- **200**: Returns the profile that the package is added to
- **403**: Unauthorized access or profile reference does not exist
- **422**: Request validation failed

---

### GET /profiles/{referenceId}/assignment

**Summary:** Get Assignment Information of a Profile

**Description:** Returns the assignment information, targets and options of a profile. Requires the caller be granted the "Manage Profiles" global permission.

**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference Id of the profile
- `versionNumber`: Type: integer. Description: The version number of the profile

**Responses:**
- **200**: Returns the assignment information about a profile
- **403**: Unauthorized access or profile reference or the profile version does not exist

---
### POST /profiles/{referenceId}/assignment/targetDeviceGroups

**Summary:** Add new Target Device Groups to the Profile assignment

**Description:** Assigns new Target Device Groups to the Profile . Requires the caller be granted the "Manage Profiles" global permissions and the "Read and Write" profile-specific permission.

**(Available Since MobiControl v15.2.1 and v15.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference Id of the profile
- `deviceGroupPaths` (Required): Type: object. Description: List of device group paths. The reference ID or the path of the device group. When using reference ID, "referenceId:" must be prepended to the ID value. When using Path it must be (e.g. \\\\\\\\My Company\\\\Sales Devices).<br></br> POST Payload e.g. <br></br>while using paths ["\\\\\\\\My Company\\\\Sales Devices","\\\\\\\\My Company\\\\Management Devices"] <br></br> while using reference ids ["referenceId:9cae0e6e-dac7-4a80-afe9-481ceb87930f", "referenceId:72f4191f-379d-47a9-a87d-86a2c7a780b7"]

**Responses:**
- **200**: Returns the profile that the package is added to
- **403**: Unauthorized access or profile reference does not exist
- **422**: Request validation failed

---
### DELETE /profiles/{referenceId}/assignment/targetDeviceGroups/{deviceGroupPath}

**Summary:** Remove a Target Device Group from a Profile assignment

**Description:** Remove a Target Device Group from a Profile.  Requires the caller be granted "Manage Groups" permission for the specified device group.

**Parameters:**
- `referenceId` (Required): Type: string. Description: Profile Reference Id
- `deviceGroupPath` (Required): Type: string. Description: The reference ID or the path of the device group. When using reference ID, "referenceId:" must be prepended to the ID value. Path must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).

**Responses:**
- **200**: Device Group has been excluded from profile
- **403**: Unauthorized access or profile reference does not exist
- **422**: Request validation failed

---
### POST /profiles/{referenceId}/assignment/targetDevices

**Summary:** Add new Target Devices to the Profile assignment

**Description:** Assigns new Target Devices to the Profile. Requires the caller be granted the "Manage Profiles" global permissions and the "Read and Write" profile-specific permission.

**(Available Since MobiControl v15.2.1 and v15.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference Id of the profile
- `deviceIds` (Required): Type: object. Description: List of device Ids. POST Payload e.g. ["DeviceReferenceId1","DeviceReferenceId2"]

**Responses:**
- **200**: Returns the profile that the package is added to
- **403**: Unauthorized access or profile reference does not exist
- **422**: Request validation failed

---
### DELETE /profiles/{referenceId}/assignment/targetDevices/{deviceId}

**Summary:** Remove a Device from a Profile Assignment

**Description:** Remove a Device from a Profile Assignment. Requires the caller be granted the "Manage Profiles" global permissions and the "Read and Write" profile-specific permission.

**(Available Since MobiControl v15.2.1 and v15.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Profile Reference Id Name
- `deviceId` (Required): Type: string. Description: Device Id

**Responses:**
- **200**: Device has been excluded from profile
- **403**: Unauthorized access or profile reference does not exist
- **422**: Request validation failed

---
### GET /profiles/{referenceId}

**Summary:** Get a Profile

**Description:** To retrieve a single profile with the profile reference id being the input parameter.

**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference Id of the profile

**Responses:**
- **200**: Returns a single profile based on a profile reference id
- **403**: Unauthorized access or profile reference does not exist

---

### DELETE /profiles/{referenceId}

**Summary:** Delete a Profile

**Description:** Requires the caller be granted the "Manage Profiles" global permission and the "Read and Write" profile-specific permission.

**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference Id of the profile

**Responses:**
- **204**: No Content
- **403**: Unauthorized access or profile reference does not exist

---
### GET /profiles/{referenceId}/versions/{versionNumber}/packages

**Summary:** Get Packages of a Profile Version

**Description:** Returns a list of packages associated with a specific version of a profile.
         Requires the caller be granted the "View Profiles" global permission.

Supported sort fields: InstallationOrder, ReferenceId, Version, Name, Size.

**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference Id of the profile
- `versionNumber` (Required): Type: integer. Description: The version number of the profile
- `Order`: Type: array.
- `Skip`: Type: integer.
- `Take`: Type: integer.

**Responses:**
- **200**: Returns a list of packages based on a profile reference id
- **403**: Unauthorized access or profile reference or profile version does not exist

---
### GET /profiles/{referenceId}/logs

**Summary:** Get Profile Logs

**Description:** Returns a list of logs associated with a profile.
         Requires the caller be granted the "View Profiles" global permission.
         Ordering is restricted to Timestamp.

**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference Id of the profile
- `logSeverities`: Type: array. Description: Return the logs whose severity matches that from the array
- `startDate`: Type: string. Description: Return the logs whose date is startDate or later
- `endDate`: Type: string. Description: Only return the logs whose date is endDate or before
- `Order`: Type: array.
- `Skip`: Type: integer.
- `Take`: Type: integer.

**Responses:**
- **200**: Returns a list of a logs based on a profile reference id
- **403**: Unauthorized access or profile reference does not exist

---
### GET /profiles/{referenceId}/deviceAssignmentSummary

**Summary:** Get Device Assignment Status Summary of a Profile

**Description:** Return the device assignment status summary for a given profile. Requires the caller be granted the "View Profiles" global permission.

**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference Id of the profile

**Responses:**
- **200**: Returns a device status summary based on a profile reference id
- **403**: Unauthorized access or profile reference does not exist

---
### GET /profiles/{referenceId}/userAssignmentSummary

**Summary:** Get User Assignment Status Summary of a Profile

**Description:** Return the user assignment status summary for a given profile. Requires the caller be granted the "View Profiles" global permission.

**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference Id of the profile

**Responses:**
- **200**: Returns a user status summary based on a profile reference id
- **403**: Unauthorized access or profile reference does not exist

---
### GET /profiles/{referenceId}/versions

**Summary:** Get Version Info of a Profile

**Description:** Returns a list of versions for a profile. Requires the caller be granted the "View Profiles" global permission.

**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference Id of the profile

**Responses:**
- **200**: Returns a list of versions for a profile
- **403**: Unauthorized access or profile reference does not exist

---
### POST /profiles/{referenceId}/actions/disable

**Summary:** Disable a Profile

**Description:** Disable this profile, this keeps the profile active for all currently assigned groups and devices but new assignments cannot be made to it.
         Requires the caller be granted the "Manage Profiles" global permission and the "Read and Write" profile-specific permission.

**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference Id of the profile

**Responses:**
- **200**: Returns the profile based on a profile reference id, after performing disable action
- **403**: Unauthorized access or profile reference does not exist

---
### POST /profiles/{referenceId}/actions/revoke

**Summary:** Revoke a Profile

**Description:** Revoking a profile removes its configurations and packages from a device. You can reapply revoked profiles to devices in the future.
         Requires the caller be granted the "Manage Profiles" global permission and the "Read and Write" profile-specific permission.

**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference Id of the profile

**Responses:**
- **200**: Returns the profile based on a profile reference id, after performing revoke action
- **403**: Unauthorized access or profile reference does not exist

---
### GET /profiles/{referenceId}/logs/summary

**Summary:** Get Profile logs summary

**Description:** Returns logs summary associated with a Profile.
         Requires the caller be granted the "View Profile" global permission.

**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference Id of the profile
- `startDate`: Type: string. Description: Return the logs whose date is startDate or later
- `endDate`: Type: string. Description: Return the logs whose date is endDate or before

**Responses:**
- **200**: Returns a list of a logs based on a profile reference id
- **403**: Unauthorized access or profile reference does not exist

---
### POST /profiles/{referenceId}/actions/retry

**Summary:** Retry Installing a Profile

**Description:** Re-installation will be attempted on devices where the profile is either "Failed" or "Partially Installed". Returns the profile based on a profile reference id, after performing a retry action.

Requires the caller be granted the "Manage Profiles" global permission and the "Read and Write" profile-specific permission.

**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference Id of the profile

**Responses:**
- **200**: Returns the profile based on a profile reference id, after performing retry action
- **403**: Unauthorized access or profile reference does not exist

---
### PUT /profiles/{referenceId}/name

**Summary:** Updates profile name

**Description:** Updates the name of the profile to the given value.
         This name cannot be empty and must be unique.
         Requires the caller be granted the "Manage Profiles" global permission and the "Read-Write" profile-specific permission.

**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference Id of the profile
- `name` (Required): Type: object. Description: The new name for the profile

**Responses:**
- **204**: Returns a new profile with the specified name
- **403**: Unauthorized access or profile reference does not exist

---
### PUT /profiles/{referenceId}/description

**Summary:** Updates profile description

**Description:** Updates the description of the profile to the given value.
         Blank values will clear the description.
         Requires the caller be granted the "Manage Profiles" global permission and the "Read-Write" profile-specific permission.

**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference Id of the profile
- `description` (Required): Type: object. Description: The new description for the profile

**Responses:**
- **204**: Returns a new profile with the specified description
- **403**: Unauthorized access or profile reference does not exist

---
### GET /profiles/digests

**Summary:** Get Profile Digest info for a device group

**Description:** Returns the profile information for the provided path and device platform.

**(Available Since MobiControl v2024.0.0)**

**Parameters:**
- `PathId`: Type: string. Description: When using a reference ID, it must be prepended to the ID value, "referenceId:" (e.g. referenceId%3A7e39724b-6120-4c1f-96a8-c04d4570a974).
When using path, Root of path must be prepended with "\\\\", where the first slash is an escape character. For example: "\\\\My Company" or "\\\\My Company\\Management Devices".
- `DevicePlatform`: Type: string. Description: The DevicePlatform enum value.
- `Skip`: Type: integer. Description: How many records to skip.
- `Take`: Type: integer. Description: How many records to take.

**Responses:**
- **200**: Returns the digest information about a profile
- **403**: Unauthorized access or profile reference or the profile version does not exist
- **422**: Device Platform not specified

---
### PUT /profiles/{referenceId}/profileInfo

**Summary:** Updates the information of the specified Profile.

**Description:** This API updates the name and description of the specified Profile.
         Requires the caller be granted the "Manage Profiles" global permission and the "Read-Write" profile-specific permission.

**(Available Since MobiControl v2024.0.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Unique identifier for a Profile.
- `profile` (Required): Type: object. Description: The new name and description for the profile.

**Responses:**
- **204**: Returns a new profile with the specified name and description
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:<br /><ol><li>[118]: Profile name '{Name}' already exists for specified family."</li></ol>

---
### POST /profiles/actions/export

**Summary:** Exports given profiles so that they can be imported into another instance.

**Description:** This API exports the reference IDs and password by making a zip file
         Requires the caller be granted the "Manage Profiles" global permission

**(Available Since MobiControl v2024.0.0)**

**Parameters:**
- `exportProfilesParameters` (Required): Type: object. Description: Contains the password as well as a string array of referenceIds when entered in a JSON format.

**Responses:**
- **403**: Not enough permissions
- **422**: Error extracting profile payload

---
### POST /profiles/actions/import

**Summary:** Imports given profiles with the correct password key values and imports the archive file in a multipart data-form.

**Description:** This API imports the profiles by getting a zip file and a password
         Requires the caller be granted the "Manage Profiles" global permission

**(Available Since MobiControl v2024.0.0)**

**Responses:**
- **403**: Insufficient permissions
- **422**: Generic error for payload import failure

---
## Reports

### GET /reports/devices

**Summary:** Downloads CSV of Device Search Result

**Description:** Downloads results of a given search filter as CSV. Requires the caller be granted the "View Groups" permission for the specified device group.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `fields` (Required): Type: string. Description: Comma separated field names to be included in the report
- `format`: Type: string. Description: File format [Currently only csv is supported.]
- `groupPath`: Type: string. Description: The group path.The reference ID or the path of the device group. When using reference ID, "referenceId:" must be prepended to the ID value Must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).
- `filter`: Type: string. Description: Filter string
- `timeZoneOffset`: Type: integer. Description: Time zone offset from UTC
- `timeZoneId`: Type: string. Description: Time zone ID generated from current web browser
- `includeSubgroups`: Type: boolean. Description: When group path is specified, determines whether descendant groups should also be included.
- `order`: Type: string. Description: Defines the sorting order by property. Pass the value as -property for descending, and +property for ascending.
- `skip`: Type: integer. Description: Input the first X (count) entries that should not be returned.
- `take`: Type: integer. Description: Input the number of entries to be returned, after skipping over the 'skip' count.

**Responses:**
- **200**: OK
- **400**: Field names are missing
- **401**: Unauthorized
- **422**: Invalid search filter or parameters
- **500**: Internal search engine error

---
### POST /reports/devices/actions/emailReport

**Summary:** Create the new resource to send the desired report

**Description:** **(Available Since MobiControl v14.2.0)**

**Parameters:**
- `parameters` (Required): Type: object. Description:

**Responses:**
- **204**: Operation successful
- **400**: Field names are missing
- **401**: Unauthorized
- **422**: Invalid search filter or parameters or the specified email profile did not exist
- **500**: Internal search engine error

---
### GET /reports/device/{deviceId}/agentLog

**Summary:** Download Device-side Log for a Device

**Description:** Downloads device-side (agent) log for a device identified by its device ID, or the device's MAC / IMEI address when prefixed with "mac:" or "imei_meid_esn:" respectively. Requires the caller be granted the "Download Agent Logs" permission on the device's parent device group.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier
- `agentLogType` (Required): Type: string. Description: log type

**Responses:**
- **200**:

---
### POST /reports/packages/actions/emailReport

**Summary:** Email packages report based upon filter criteria and configured packages columns to targeted recipient

**Description:** **(Available Since MobiControl v14.3.0)**

**Parameters:**
- `parameters` (Required): Type: object. Description:

**Responses:**
- **204**:

---
### GET /reports/packages

**Summary:** Downloads CSV of Package Search Result

**Description:** Downloads packages results of a given search filter as CSV. Requires the caller be granted the "View Packages" permission.
**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `reportHeaderFields` (Required): Type: string. Description: Comma separated field names to be included in the report
- `deviceFamilies`: Type: string. Description: Only return packages that are targeting one of the families in this list. Provided as a comma-separated list of Device Family. To get list of All packages user needs to leave device families as blank or pass all device families as comma separated.
- `packageName`: Type: string. Description: Package Name search string
- `format`: Type: string. Description: File format [Currently only csv is supported.]
- `timeZoneOffset`: Type: integer. Description: Time zone offset from UTC (in Minutes)

**Responses:**
- **200**:

---
### GET /reports/profiles

**Summary:** Download CSV of Profiles Search Result

**Description:** Download profiles results of a given search filter as CSV. Requires the caller be granted the "View Profiles" permission.
**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `reportHeaderFields` (Required): Type: string. Description: Comma separated field names to be included in the report
- `format`: Type: string. Description: File format [Currently only csv is supported.]
- `timeZoneOffset`: Type: integer. Description: Time zone offset from UTC (in Minutes)
- `nameContains`: Type: string. Description: Only return profiles whose name contains this value
- `withStatuses`: Type: string. Description: Only return profiles that have statuses that match one of the values in this list. Provided as a comma-separated list of ProfileVersionStatus values.
- `forFamilies`: Type: string. Description: Only return profiles that are targeting one of the families in this list. Provided as a comma-separated list of DeviceFamily values
- `hasDraft`: Type: boolean. Description: Only return profiles that have a current draft. When false, only return profiles that do not have a draft. If null, then do not take draft status into account
- `hasSchedule`: Type: boolean. Description: Only return profiles that currently have a schedule. When false, only return profiles that do not have a schedule. If null, then do not take schedule status into account
- `autoInstallOnly`: Type: boolean. Description: Only return profiles that are automatically installed. When false, this only returns profiles that are self-installed. If null, then do not take install method into account.

**Responses:**
- **200**:

---
### POST /reports/profiles/actions/emailReport

**Summary:** Email profile report based upon filter criteria and configured profiles columns to targeted recipient

**Description:** **(Available Since MobiControl v14.3.0)**

**Parameters:**
- `parameters` (Required): Type: object. Description:

**Responses:**
- **204**:

---
### GET /reports/compliancepolicies

**Summary:** Download CSV of filtered compliance policies

**Description:** Download profiles results of a given search filter as CSV. Requires the caller be granted the "View Profiles" permission.
**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `reportHeaderFields` (Required): Type: string. Description: Comma separated field names to be included in the report
- `format`: Type: string. Description: File format [Currently only csv is supported.]
- `timeZoneOffset`: Type: integer. Description: Time zone offset from UTC (in Minutes)
- `families`: Type: array. Description: If specified, return only policies for the selected families
- `nameContains`: Type: string. Description: If specified, return only policies where the name contains the specified string
- `statuses`: Type: array. Description: If specified, return only policies having the selected status(es)
- `isAssigned`: Type: boolean. Description:

**Responses:**
- **200**:

---
### POST /reports/compliancepolicies/actions/emailReport

**Summary:** Email compliance policy report based upon filter criteria and configured profiles columns to targeted recipient

**Description:** **(Available Since MobiControl v15.1.0)**

**Parameters:**
- `parameters` (Required): Type: object. Description:

**Responses:**
- **204**:

---
## Role Management

### GET /security/principal/roles

**Summary:** Returns all roles.

**Description:** Returns an array of all roles.

Requires the caller be granted the "Manage Console Security" or "Lookup Users and Group Membership" permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `searchString`: Type: string. Description: Role name search string.
- `order`: Type: string. Description: Defines the sorting order by property. Pass the value as -property for descending, and +property for ascending.
- `skip`: Type: integer. Description: Input the first X (count) entries that should not be returned.
- `take`: Type: integer. Description: Input the number of entries to be returned, after skipping over the 'skip' count.

**Responses:**
- **200**: Successfully returns a list of roles.
- **400**: Contract validation Failed.
- **403**: Forbidden.

---

### POST /security/principal/roles

**Summary:** Creates a new role.

**Description:** Creates a single role.

Requires the caller be granted the "Manage Console Security" permission.

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `role` (Required): Type: object. Description: Role.

**Responses:**
- **200**: Successfully creates a single role.
- **400**: Contract validation Failed.
- **403**: Forbidden.

---
### GET /security/principal/roles/{referenceId}

**Summary:** Returns the specified role.

**Description:** Returns the details of a given role.

Requires the caller be granted the "Manage Console Security" or "Lookup Users and Group Membership" permission.

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Role reference id.

**Responses:**
- **200**: Successfully returns a single role.
- **400**: Contract validation Failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6512: Insufficient View Permission</li></ol>

---

### PUT /security/principal/roles/{referenceId}

**Summary:** Updates the specified role.

**Description:** Updates the role referred to by the referenceId.

Requires the caller be granted the "Manage Console Security" permission.

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Role reference id.
- `role` (Required): Type: object. Description: Role.

**Responses:**
- **200**: Successfully edits a single role.
- **400**: Contract validation Failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6511: Insufficient Edit Permission</li></ol>

---

### DELETE /security/principal/roles/{referenceId}

**Summary:** Deletes the specified role.

**Description:** Deletes the role referred to by the referenceId.

Requires the caller be granted the "Manage Console Security" permission.

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Role reference id.

**Responses:**
- **204**: Successfully deletes a single role.
- **400**: Contract validation Failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6510: Deletion not allowed</li><li>6511: Insufficient Edit Permission</li><li>6516: Deletion not allowed</li><li>6518: Directory deletion is restricted under SOTI MobiControl, please delete through SOTI Identity</li><li>6519: Deletion not allowed</li></ol>

---
### GET /security/principal/roles/{referenceId}/users

**Summary:** Returns a list of users for a role.

**Description:** This API retrieves all the users that are mapped to a role specified by its Reference Id.

Requires the caller be granted the 'Web Console Access', 'Manage Console Security' and  'Lookup Users and Group Membership' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id for a role.
- `searchString`: Type: string. Description: String to match the user names.

**Responses:**
- **200**: Successfully returns a list of users.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6512: Insufficient View Permission</li></ol>

---

### PUT /security/principal/roles/{referenceId}/users

**Summary:** Updates the specified users for a role.

**Description:** This API updates the users that map to a role

Requires the caller be granted the 'Manage Console Security' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference id of a role.
- `userReferenceIds` (Required): Type: object. Description: Reference id's for users.

**Responses:**
- **200**: Successfully returns a list of users.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6511: Insufficient Edit Permission</li><li>6520: Partially Updated</li></ol>

---
### GET /security/principal/roles/{referenceId}/userGroups

**Summary:** Returns a list of directories for a role.

**Description:** This API retrieves all the directories mapped to a role specified by its Reference Id.

Requires the caller be granted the 'Manage Console Security' or 'Lookup Users and Group Membership' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference id of a role.

**Responses:**
- **200**: Successfully returns a list of directories.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6512: Insufficient View Permission</li></ol>

---

### PUT /security/principal/roles/{referenceId}/userGroups

**Summary:** Updates the specified directories for a role.

**Description:** This API updates the directories that map to a role

Requires the caller be granted the 'Manage Console Security' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference id of a role.
- `userGroupReferenceIds` (Required): Type: object. Description: Reference Id's for directories.

**Responses:**
- **200**: Returns a list of directories.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6511: Insufficient Edit Permission</li><li>6520: Partially Updated</li></ol>

---
### GET /security/principal/roles/{referenceId}/catalogueItemReference

**Summary:** Returns the catalogue reference for a role.

**Description:** This API retrieves the catalogue reference ID for a role

Requires the caller be granted the 'Manage Console Security' or ' Lookup Users and Group Membership' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id for a role.

**Responses:**
- **200**: Successfully returns the specified catalogue reference id.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6512: Insufficient View Permission</li></ol>

---

### POST /security/principal/roles/{referenceId}/catalogueItemReference

**Summary:** Creates a catalogue item for a role.

**Description:** This API creates a new catalogue item for a role

Requires the caller be granted the 'Manage Console Security' or 'Lookup Users and Group Membership' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id for a role.

**Responses:**
- **200**: Successfully returns the specified catalogue reference id.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6511: Insufficient Edit Permission</li><li>6514: Insufficient Manage permission</li></ol>

---

### DELETE /security/principal/roles/{referenceId}/catalogueItemReference

**Summary:** Deletes a catalogue item for a role.

**Description:** This API deletes a catalogue reference ID for a role

Requires the caller be granted the 'Manage Console Security' or 'Lookup Users and Group Membership' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id for a role.

**Responses:**
- **204**: Successfully deleted catalogue reference id.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6511: Insufficient Edit Permission</li></ol>

---
### GET /security/principal/roles/{referenceId}/{scope}/rights

**Summary:** Returns the permissions of a role.

**Description:** Returns the permissions allocated to a role.

Requires the caller be granted the "Manage Console Security" or "Lookup Users and Group Membership" permission.

**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference identifier.
- `scope` (Required): Type: string. Description: The scope.

**Responses:**
- **200**: Successfully returns permission for a role.
- **400**: Contract validation failed.
- **403**: Forbidden.

---

### PUT /security/principal/roles/{referenceId}/{scope}/rights

**Summary:** Updates the general permissions for a role.

**Description:** This API updates the general permissions for a selected role specified by its Reference Id.

Requires the caller be granted the 'Manage Console Security' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id for a role.
- `scope` (Required): Type: string. Description: Authorization scope.
- `rights` (Required): Type: object. Description: Schema for permission and its boolean value.

**Responses:**
- **200**: Successfully returns a list of Right Summary.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6507: Invalid permission name.</li><li>6508: Duplicate permission name.</li><li>6509: Invalid parent child state.</li><li>6511: Insufficient Edit Permission.</li><li>6514: Insufficient Manage permission.</li><li>6515: Security right not found.</li></ol>

---
### GET /security/principal/roles/{referenceId}/deviceGroups/{deviceGroupReferenceId}/rights

**Summary:** Returns device group permissions for a role.

**Description:** This API retrieves all device group permission for a role specified by its Reference Id.

Requires the caller be granted the 'Manage Console Security' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id for a role.
- `deviceGroupReferenceId` (Required): Type: string. Description: Reference Id of a device group.

**Responses:**
- **200**: Successfully returns a list of Right Summary.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6512: Insufficient View Permission</li></ol>

---

### PUT /security/principal/roles/{referenceId}/deviceGroups/{deviceGroupReferenceId}/rights

**Summary:** Updates the device group permission for a role.

**Description:** This API updates all device group permission rights belonging to a single role specified by its Reference Id.

Requires the caller be granted the 'Manage Console Security' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id for a role.
- `deviceGroupReferenceId` (Required): Type: string. Description: Reference Id for a device group.
- `rights` (Required): Type: object. Description: Schema for permission and its boolean value.

**Responses:**
- **200**: Successfully returns a list of Right Summary.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6507: Invalid permission name</li><li>6508: Duplicate permission name</li><li>6509: Security right has invalid parent/child state</li><li>6511: Insufficient Edit Permission</li><li>6514: Insufficient Manage permission</li><li>6515: Security right not found</li></ol>

---
### GET /security/principal/roles/{referenceId}/{scope}/bulkActionLimits

**Summary:** Returns the Bulk Action Limits allocated to a role.

**Description:** Returns the Bulk Action Limit allocated to a role.

Requires the caller be granted the "Manage Console Security" permission or the "LookupUsersAndGroups" permission.

**(Available Since MobiControl v2024.1.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference identifier.
- `scope` (Required): Type: string. Description: The scope.

**Responses:**
- **200**: Successfully returns Bulk Action Limits for a role.
- **400**: Contract validation failed.
- **403**: Forbidden.

---
### GET /security/principal/roles/{referenceId}/logs

**Summary:** Retrieves logs for a role.

**Description:** Retrieves the log activity for a particular role.

Requires the caller be granted the 'Manage Console Security' or 'Lookup Users and Group Membership' permissions.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id of a Role.
- `startDate` (Required): Type: string. Description: Date to retrieve logs from. Please specify the time if start and end dates are the same.
- `endDate` (Required): Type: string. Description: Date to retrieve logs to. Please specify the time if start and end dates are the same.
- `logSeverities`: Type: array. Description: One or more categories of log severities.
- `orderByDesc`: Type: boolean. Description: Order logs by timestamp, true for descending, false for ascending.
- `skip`: Type: integer. Description: Input the first X (count) entries that should not be returned.
- `take`: Type: integer. Description: Input the number of entries to be returned, after skipping over the 'skip' count.

**Responses:**
- **200**: Successfully returns a list of Security Role Log Entry.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.

---
### GET /security/principal/roles/{referenceId}/logs/actions/download

**Summary:** Returns the CSV file of logs for a role.

**Description:** This API exports a CSV file of logs for a role specified by its Reference Id.

Requires the caller be granted the 'Manage Console Security' or ' Lookup Users and Group Membership' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The unique Identifier for the role.
- `reportHeaderFields` (Required): Type: string. Description: Comma separated field names to be included in the csv file.
- `logSeverities`: Type: array. Description: List of log severities to include into result such as Information, Warning or Error.
- `startDate` (Required): Type: string. Description: The date starting which the logs will be fetched (UTC format).
- `endDate` (Required): Type: string. Description: The date till which the logs will be fetched (UTC format).
- `format`: Type: string. Description: File format [Currently only csv is supported.].
- `timeZoneOffset`: Type: integer. Description: Time zone offset from UTC (in Minutes).
- `orderByDesc`: Type: boolean. Description: Defines the sorting order by timestamp. Pass the value as true for descending, false for ascending.
- `Skip`: Type: integer.
- `Take`: Type: integer.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.

---
## Schedules

### GET /schedules/{referenceId}

**Summary:** Returns a specified Schedules.

**Description:** This API returns a specified Schedule.


         Requires the caller be granted the "View File Sync Policies", "View Telecom Expense Management Policies", or "View Profile Schedules" permission.

**(Available since MobiControl v2024.1.0).**


**Parameters:**
- `referenceId` (Required): Type: string. Description: reference identifier of schedule.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.

---

### PUT /schedules/{referenceId}

**Summary:** Updates the specified schedule.

**Description:** This API updates a specified Schedule.


         Requires the caller be granted the "Manage File Sync Policies", "Manage Telecom Expense Management Policies", or "Manage Profile Schedules" permission.

**(Available since MobiControl v2024.1.0).**


**Parameters:**
- `referenceId` (Required): Type: string. Description: reference identifier of schedule.
- `schedule` (Required): Type: object. Description: The schedule.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.

---

### DELETE /schedules/{referenceId}

**Summary:** Deletes the specified schedule.

**Description:** This API deletes a specified Schedule.


         Requires the caller be granted the "Manage File Sync Policies" or "Manage Telecom Expense Management Policies" permission.

**(Available since MobiControl v2024.1.0).**


**Parameters:**
- `referenceId` (Required): Type: string. Description: reference identifier of schedule.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.

---
### POST /schedules

**Summary:** Creates schedule.

**Description:** This API creates a schedule.


         Requires the caller be granted the "Manage File Sync Policies", "Manage Telecom Expense Management Policies", or "Manage Profile Schedules" permission.

**(Available since MobiControl v2024.1.0).**


**Parameters:**
- `schedule` (Required): Type: object. Description: The schedule.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.

---
## Search

### GET /search/index

**Summary:** Get Search Synchronization Results

**Description:** Returns current and historical MobiControl Search index synchronization results that describes the integrity of the index at the time of completion, or the progress of an indexing process if currently running. Requires the caller be granted the "Access Web Console" permission.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `Skip`: Type: integer.
- `Take`: Type: integer.

**Responses:**
- **200**: Gets synchronization results

---

### POST /search/index

**Summary:** Starts Incremental Search Synchronization

**Description:** Initiates synchronization which will compare and update the MobiControl Search index using the MobiControl database as the source of true. During regular operation MobiControl will ensure the index is updated in real-time, and therefore this synchronization process is needed only as a failsafe. Only one synchronization process can be running at a time across all Management Services, and results can be requested periodically via the GET /search/index method. Requires the caller be granted the "Access Web Console" permission.
**(Available Since MobiControl v14.0.0)**

**Responses:**
- **202**: Indexing started successfully
- **406**: Indexing is currently running
- **409**: Indexing cannot be started because another server is currently starting it

---
### POST /search/executeRawRequest

**Summary:** Executes raw MobiControl search request

**Description:** Executes raw MobiControl Search request. For power users who are familiar with ElasticSearch REST API only.
Requires EnableRawElasticSearchRequests to be set to "1" in the Settings table
**(Available Since MobiControl v15.1.0)**

**Parameters:**
- `elasticSearchRequest` (Required): Type: object. Description: Raw MobiControl Search request

**Responses:**
- **200**: MobiControl Search raw response

---
### GET /search/health

**Summary:** Get Search Engine Health Status

**Description:** Returns current Search Engine health status. Requires the caller be granted the "Access Web Console" permission.
**(Available Since MobiControl v14.3.0)**

**Responses:**
- **200**: Gets Search Engine Health Status

---
### GET /search/configuration

**Summary:** Get Search Engine Configuration

**Description:** Returns current Search Engine configuration information. Requires the caller be granted the "Administration" permission.
**(Available Since MobiControl v14.2.1)**

**Responses:**
- **200**: A collection of SearchEngineConfiguration

---

### POST /search/configuration

**Summary:** Set Search Engine Configuration

**Description:** Updates the Search Engine configuration information using engineConfiguration as a mandatory parameter. Requires the caller be granted the "Administration" permission.
**(Available Since MobiControl v14.2.1)**

**Parameters:**
- `engineConfiguration` (Required): Type: object.

**Responses:**
- **204**:

---
### POST /search/index/all

**Summary:** Starts Full Search Synchronization

**Description:** Recreates ElasticSearch indexes and type mapping and synchronizes the data. Use with caution.

**Responses:**
- **204**:

---
### GET /search/status

**Summary:** Gets the Health Status of MobiControl Search Engine.

**Description:** Get the Health Status of MobiControl Search Engine. Requires the caller be granted "View System Health" permission.
**(Available Since MobiControl v15.3.0)**

**Responses:**
- **200**:
- **401**: Unauthorized access
- **403**: Forbidden
- **503**: Service unavailable

---
## Search Server

### GET /servers/searchServer

**Summary:** Returns the list of search servers.

**Description:** This API returns the list of search servers


Requires the caller be granted the "Manage SOTI Search" permission.

**(Available since MobiControl v2024.0.0)**


**Responses:**
- **200**: Success.
- **403**: Forbidden.

---
### DELETE /servers/searchServer/{referenceId}

**Summary:** Deletes obsolete search server.

**Description:** This API deletes obsolete search server.


Requires the caller be granted the "Manage SOTI Search" permission.

**(Available since MobiControl v2024.0.0)**


**Parameters:**
- `referenceId` (Required): Type: string.

**Responses:**
- **204**: No Content.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:.<br /><ol><li>9901 - Search server {FQDN} cannot be deleted when it is online.</li><li>9902 - Last remaining Search Server cannot be deleted.</li></ol>

---
## Security

### GET /security/permissions

**Summary:** Retrieve All System Permissions

**Description:** Returns the MobiControl permissions tree which includes all possible rights for administrators of the system. Role defines functional areas of the product and should be used to contextualize where the permission is applied. For example, "CheckIn" is an action (and permission) of both the administrative console ("SystemAdministrator" role), and the Self Service Portal ("DeviceOwner" role). Requires the caller be granted the "Access Web Console" permission.
**(Available Since MobiControl v14.0.0)**

**Responses:**
- **200**: The permission trees

---
### GET /security/currentUser/rights/{permission}/IsAllowed

**Summary:** Report on access permission for current user

**Description:** Retrieve information on whether the current user can access / execute a specific action in MobiControl. Actions typically are view profiles, manage rules etc.  This requires the caller to be granted the “Access Web Console” permission.
**(Available Since MobiControl v14.2.1)**

**Parameters:**
- `permission` (Required): Type: string. Description: Name of the Permission

**Responses:**
- **200**: boolean telling if user has permission or not

---
### GET /security/currentUser/rights/{permission}/{assetType}/{referenceId}/IsAllowed

**Summary:** Report on access permission for current user per asset

**Description:** Retrieve information on whether the current user can access / execute a specific action on a specific asset (Device / Device Group) in MobiControl. Actions typically are view profiles, manage rules etc.  The “referenceId” refers to the primary identifier of the asset. This requires the caller to be granted the “Access Web Console” permission.
**(Available Since MobiControl v14.2.1)**

**Parameters:**
- `permission` (Required): Type: string. Description: Name of the Permission
- `assetType` (Required): Type: string. Description: Type of the Asset
- `referenceId` (Required): Type: string. Description: Identifier of the Asset

**Responses:**
- **200**: boolean telling if user has permission or not

---
### GET /security/rights

**Summary:** Retrieve Permissions of Current User

**Description:** Returns the rights granted to the current user. Currently only Device Group, and Self Service Portal permissions are returned. Role defines functional areas of the product and should be used to contextualize where the permission is applied. For example, "CheckIn" is an action (and permission) of both the administrative console ("SystemAdministrator" role), and the Self Service Portal ("DeviceOwner" role). Requires the caller be granted the "Manage Console Security" permission if the request is for a user other than the caller.
**(Available Since MobiControl v14.0.0)**

**Responses:**
- **200**: The user right details

---
### GET /security/users/{userName}/{role}/rights

**Summary:** Retrieves Permissions for a User

**Description:** Returns the rights granted to the specified user. Currently only Device Group, and Self Service Portal permissions are returned. Role defines functional areas of the product and should be used to contextualize where the permission is applied. For example, "CheckIn" is an action (and permission) of both the administrative console ("SystemAdministrator" role), and the Self Service Portal ("DeviceOwner" role). Requires the caller be granted the "Manage Console Security" permission if the request is for a user other than the caller.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `userName` (Required): Type: string. Description: Name of the user. Must be double URL-encoded when using special characters (e.g. a/username - a%252fusername). When called from this page, it should be encoded only once (a%2fusername).
- `role` (Required): Type: string. Description: The security role
- `asset`: Type: string. Description: Type of the Asset

**Responses:**
- **200**: The user right details

---

### PUT /security/users/{userName}/{role}/rights

**Summary:** Sets Permissions for a User

**Description:** Replaces the permissions for a given user with those defined. Currently only Device Group, and Self Service Portal permissions are supported. Role defines functional areas of the product and should be used to contextualize where the permission is applied. For example, "CheckIn" is an action (and permission) of both the administrative console ("SystemAdministrator" role), and the Self Service Portal ("DeviceOwner" role). Requires the caller be granted the "Manage Console Security" permission.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `userName` (Required): Type: string. Description: Name of the user. Must be double URL-encoded when using special characters (e.g. a/username - a%252fusername). When called from this page, it should be encoded only once (a%2fusername).
- `role` (Required): Type: string. Description: The role
- `rights` (Required): Type: object. Description: Security rights

**Responses:**
- **204**:

---

### DELETE /security/users/{userName}/{role}/rights

**Summary:** Removes Role Permissions from a User

**Description:** Removes all rights granted in a given role for the specified user. Currently only Device Group, and Self Service Portal permissions are supported. Role defines functional areas of the product and should be used to contextualize where the permission is applied. For example, "CheckIn" is an action (and permission) of both the administrative console ("SystemAdministrator" role), and the Self Service Portal ("DeviceOwner" role). Requires the caller be granted the "Manage Console Security" permission if the request is for a user other than the caller.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `userName` (Required): Type: string. Description: Name of the user. Must be double URL-encoded when using special characters (e.g. a/username - a%252fusername). When called from this page, it should be encoded only once (a%2fusername).
- `role` (Required): Type: string. Description: The role

**Responses:**
- **204**:

---
### GET /security/users/{userName}/group/{path}/rights

**Summary:** Retrieves Device Group Permissions for a User

**Description:** Returns all rights granted on given device group for the specified user. Requires the caller be granted the "Manage Console Security" permission. Requires the caller be granted the "Manage Console Security" permission if the request is for a user other than the caller.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `userName` (Required): Type: string. Description: Name of the user. Must be double URL-encoded when using special characters (e.g. a/username - a%252fusername). When called from this page, it should be encoded only once (a%2fusername).
- `path` (Required): Type: string. Description: The reference ID or the path of the device group. When using reference ID, "referenceId:" must be prepended to the ID value. Path must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).

**Responses:**
- **200**: Device group security rights

---

### PUT /security/users/{userName}/group/{path}/rights

**Summary:** Sets Device Group Permissions for a User

**Description:** Replaces the device group permissions for a given user with those defined. Requires the caller be granted the "Manage Console Security" permission.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `userName` (Required): Type: string. Description: Name of the user. Must be double URL-encoded when using special characters (e.g. a/username - a%252fusername). When called from this page, it should be encoded only once (a%2fusername).
- `path` (Required): Type: string. Description: The reference ID or the path of the device group. When using reference ID, "referenceId:" must be prepended to the ID value. Path must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).
- `rights` (Required): Type: object. Description: Security rights

**Responses:**
- **204**:

---

### DELETE /security/users/{userName}/group/{path}/rights

**Summary:** Deletes Device Group Permissions from a User

**Description:** Removes all rights granted on given device group for the specified user. Requires the caller be granted the "Manage Console Security" permission.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `userName` (Required): Type: string. Description: Name of the user. Must be double URL-encoded when using special characters (e.g. a/username - a%252fusername). When called from this page, it should be encoded only once (a%2fusername).
- `path` (Required): Type: string. Description: The reference ID or the path of the device group. When using reference ID, "referenceId:" must be prepended to the ID value. Path must be double URL-encoded (e.g. %255C%255CMy%2520Company). When called from this page, it should be encoded only once (%5C%5CMy%20Company).

**Responses:**
- **204**:

---
### GET /security/users

**Summary:** Retrieve List of Users

**Description:** Returns all MobiControl console users or those that match the provided search criteria. Hidden users are users implicitly authorized to login to MobiControl through an LDAP group and have logged in at least once.
**(Since MobiControl 13.3.0)**

**Parameters:**
- `includeHiddenUsers`: Type: boolean. Description: Filter returned users by their visibility
- `searchString`: Type: string. Description: Filter returned user names by this value
- `memberOf`: Type: array. Description: Only return users that are members of one or more of the specified groups
- `kind`: Type: string. Description: Only returns users of this kind
- `order`: Type: string. Description: Defines the sorting order by property. Pass the value as -property for descending, and +property for ascending.
- `skip`: Type: integer. Description: Input the first X (count) entries that should not be returned.
- `take`: Type: integer. Description: Input the number of entries to be returned, after skipping over the 'skip' count.

**Responses:**
- **200**: A list of all users, or those that match the given criteria

---
### GET /security/users/{userName}

**Summary:** Retrieve a Single User

**Description:** Returns a named MobiControl console user including users that are implicitly authorized to login to MobiControl through an LDAP group and have logged in at least once ("hidden").
**(Since MobiControl 13.3.0)**

**Parameters:**
- `userName` (Required): Type: string. Description: Name of the user. Must be double URL-encoded when using special characters (e.g. a/username - a%252fusername). When called from this page, it should be encoded only once (a%2fusername).

**Responses:**
- **200**: The user

---
### GET /security/users/{userName}/groups

**Summary:** Retrieve User's Group

**Description:** Returns a list of groups that a given user is a member of including users that are implicitly authorized to login to MobiControl through an LDAP group and have logged in at least once ("hidden").
**(Since MobiControl 13.3.0)**

**Parameters:**
- `userName` (Required): Type: string. Description: Name of the user. Must be double URL-encoded when using special characters (e.g. a/username - a%252fusername). When called from this page, it should be encoded only once (a%2fusername).
- `showGroupInheritance`: Type: boolean. Description: Whether to show inherited groups

**Responses:**
- **200**: A list of all groups the user is a member of.

---
### GET /security/users/{userName}/logs

**Summary:** Retrieve Logs for a User/User Group

**Description:** Retrieve event logs for users identified by its username. Limit the results to matching criteria such as event severity and date range. Requires the caller be granted the "ManageUserSecurity" or "LookupUsersAndGroups" permissions.
**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `userName` (Required): Type: string. Description: Name of the user. Must be double URL-encoded when using special characters (e.g. a/username - a%252fusername). When called from this page, it should be encoded only once (a%2fusername).
- `startDate` (Required): Type: string. Description: The start date. Example: 2015-12-19T16:39:57-02:00
- `endDate` (Required): Type: string. Description: The end date. Example: 2015-12-19T16:39:57-02:00
- `logSeverities`: Type: array. Description: List of log severities to include into result set
- `Skip`: Type: integer.
- `Take`: Type: integer.

**Responses:**
- **200**: Returns logs for a user by its user

---
### POST /security/currentuser/changepassword

**Summary:** Change Current User's Password

**Description:** Changes the password for the authenticating user. Requires that Console Security allow for change of user's passwords, and that the account is local, not LDAP.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `passwordChange` (Required): Type: object. Description: Current user's old and new password

**Responses:**
- **204**:

---
### GET /security/passwordpolicy

**Summary:** Retrieve Administrative Password Policy

**Description:** Returns the administrative password policy configured in Console Security and applies to local administrators. Requires the caller be granted the "Access Web Console" permission.
**(Available Since MobiControl v14.0.0)**

**Responses:**
- **200**: Password policy

---

### PUT /security/passwordpolicy

**Summary:** Update Password Policy

**Description:** Updates the administrative password policy configured in Console Security and applies to local administrators.
**(Available Since MobiControl v15.2.0)**

**Parameters:**
- `passwordPolicy` (Required): Type: object.

**Responses:**
- **204**:

---
### GET /security/accessControlPolicy

**Summary:** Returns the access control configuration

**Description:** Returns the access control &amp; password policy configuration
**(Available Since MobiControl v15.3.0)**
Requires the caller be granted the "Web Console Access" permission

**Responses:**
- **401**: Unauthorized access

---

### PUT /security/accessControlPolicy

**Summary:** Updates the access policy configuration

**Description:** Updates the access control &amp; password policy configuration
**(Available Since MobiControl v15.3.0)**
Requires the caller be granted the "Manage Console Authentication" permission

**Parameters:**
- `request` (Required): Type: object. Description: contract to define the configuration

**Responses:**
- **204**: Successfully updated the access control config
- **400**: Contract validation failed
- **401**: Unauthorized access

---
### PUT /security/administrator/password

**Summary:** Set Default Administrator's Password

**Description:** Sets the initial password for the default "administrator" user. No authorization is required for this endpoint while the system has console security disabled. Once the administrator account has been configured console security is enabled calls to this endpoint will fail.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `password` (Required): Type: object. Description: The password

**Responses:**
- **204**: Administrator password was successfully set
- **400**: Bad request, i.e. missing or invalid password
- **403**: Forbidden, administrator user already exists

---
### PUT /security/currentUser/eulaStatus

**Summary:** Sets Acceptance of MobiControl EULA

**Description:** Sets acceptance of the MobiControl EULA for the authenticating user. At least one MobiControl administrator must have accepted the MobiControl EULA before other calls may be made to the system.
**(Available Since MobiControl v14.0.0)**

**Parameters:**
- `eulaStatus` (Required): Type: object. Description: EULA status

**Responses:**
- **204**:

---
### PUT /security/users/{username}/catalogueitem/{referenceId}/rights

**Summary:** Set the view/edit rights of the user for a specified catalogue item

**Description:** Sets the individual permissions of a user on a catalogue item.
**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `username` (Required): Type: string. Description: The name of the user
- `referenceId` (Required): Type: string. Description: The reference id of the catalogue item
- `userRight` (Required): Type: object. Description: The user's rights for the specified catalogue item

**Responses:**
- **204**:

---
### GET /security/catalogueItem/{referenceId}/rights

**Summary:** Get Catalogue Item Rights

**Description:** Returns a list of rights associated with a Catalogue Item. Requires the caller be granted the "WebConsole" global permission and the right to view the specified Catalogue Item.
**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference id of the catalogue item

**Responses:**
- **200**: Returns a list of rights based on a profile reference id
- **403**: Unauthorized access or profile reference does not exist

---
### GET /security/users/{userName}/catalogueItem/{referenceId}/rights

**Summary:** Get Catalogue Item Rights for a User

**Description:** Returns the user right associated with a Catalogue Item. Requires the caller be granted the "WebConsole" global permission and the right to view the specified Catalogue Item.
**(Available Since MobiControl v14.3.0)**

**Parameters:**
- `userName` (Required): Type: string. Description: Name of the user. Must be double URL-encoded when using special characters (e.g. a/username - a%252fusername). When called from this page, it should be encoded only once (a%2fusername).
- `referenceId` (Required): Type: string. Description: The reference id of the catalogue item

**Responses:**
- **200**: Returns the right based on a profile reference id and the username
- **403**: Unauthorized access or profile reference does not exist

---
### GET /security/groups

**Summary:** Retrieve List of Groups

**Description:** Returns all MobiControl console groups or those that match the provided search criteria.
**(Since MobiControl 14.3.0)**

**Parameters:**
- `searchString`: Type: string. Description: Filter returned group names by this value
- `memberOf`: Type: array. Description: Only return groups that are members of one or more of the specified groups
- `kind`: Type: string. Description: Only return groups of this kind
- `order`: Type: string. Description: Defines the sorting order by property. Pass the value as -property for descending, and +property for ascending.
- `skip`: Type: integer. Description: Input the first X (count) entries that should not be returned.
- `take`: Type: integer. Description: Input the number of entries to be returned, after skipping over the 'skip' count.

**Responses:**
- **200**: A list of all groups, or those that match the given criteria

---
### GET /security/assets/{assetType}/{referenceId}/rights

**Summary:** Gets rights of an asset with specified asset type and reference id

**Description:**

**(Available Since MobiControl v14.3.0)**

Please note: currently only CatalogueItem asset type is supported by this endpoint

**Parameters:**
- `assetType` (Required): Type: string. Description: Type of the asset.
- `referenceId` (Required): Type: string. Description: The asset reference identifier.

**Responses:**
- **200**: Returns a list of asset rights for a specified asset type and reference id
- **400**: Contract validation failed
- **403**: Unauthorized access
- **422**: Device Group asset type is not supported

---

### PUT /security/assets/{assetType}/{referenceId}/rights

**Summary:** Sets rights of an asset with specified asset type and reference id

**Description:**

**(Available Since MobiControl v14.3.0)**

Please note: currently only CatalogueItem asset type is supported by this endpoint

**Parameters:**
- `assetType` (Required): Type: string. Description: Type of the asset.
- `referenceId` (Required): Type: string. Description: The asset reference identifier.
- `assetRights` (Required): Type: object. Description: The asset rights.

**Responses:**
- **204**: Request to update asset rights was processed successfully
- **400**: Contract validation failed
- **403**: Unauthorized access
- **422**: Device Group asset type is not supported

---
### GET /security/assets/{assetType}/{referenceId}/users/{userName}/rights

**Summary:** Get rights of an user with specified asset type and reference id

**Description:**

**(Available Since MobiControl v14.3.0)**

Please note: currently only CatalogueItem asset type is supported by this endpoint

**Parameters:**
- `assetType` (Required): Type: string. Description: Type of the asset.
- `referenceId` (Required): Type: string. Description: The asset reference identifier.
- `userName` (Required): Type: string. Description: Name of the user. Must be double URL-encoded when using special characters (e.g. a/username - a%252fusername). When called from this page, it should be encoded only once (a%2fusername).

**Responses:**
- **200**: Returns a list of user asset rights for a specified asset type and reference id
- **400**: Contract validation failed
- **403**: Unauthorized access
- **422**: Device Group asset type is not supported

---
### GET /security/user/{name}/catalogueItemReferenceId

**Summary:** Retrieve the user referenceID from the Catalogue

**Description:** Get the Catalogue Item ReferenceId for a specific user. Requires the caller to be granted the "WebConsole" global permission and the right to view the specified Catalogue Item.
**(Available Since MobiControl v15.0.0)**

**Parameters:**
- `name` (Required): Type: string. Description: user name

**Responses:**
- **200**: Returns user's catalog referenceId

---

### POST /security/user/{name}/catalogueItemReferenceId

**Summary:** Assign rights to a user based on a catalogue reference

**Description:** Assign rights associated with a Catalogue Item to a user. Requires the caller to be granted the "WebConsole" global permission and the right to view the specified Catalogue Item.
**(Available Since MobiControl v15.0.0)**

**Parameters:**
- `name` (Required): Type: string. Description: user name

**Responses:**
- **204**:

---

### DELETE /security/user/{name}/catalogueItemReferenceId

**Summary:** Remove the user rights based on the catalogue reference

**Description:** Remove rights associated with a Catalogue Item to a specific user. Requires the caller to be granted the "WebConsole" global permission and the right to view the specified Catalogue Item.
**(Available Since MobiControl v15.0.0)**

**Parameters:**
- `name` (Required): Type: string. Description: user name

**Responses:**
- **204**:

---
### GET /security/userGroup/{name}/catalogueItemReferenceId

**Summary:** Retrieve the user group referenceID from the Catalogue

**Description:** Get the Catalogue Item ReferenceId for a specific user group. Requires the caller to be granted the "WebConsole" global permission and the right to view the specified Catalogue Item.
**(Available Since MobiControl v15.0.0)**

**Parameters:**
- `name` (Required): Type: string. Description: user group name

**Responses:**
- **200**: Returns user group's catalog referenceId

---

### POST /security/userGroup/{name}/catalogueItemReferenceId

**Summary:** Assign rights to a user group based on a catalogue reference

**Description:** Assign rights associated with a Catalogue Item to a user group. Requires the caller to be granted the "WebConsole" global permission and the right to view the specified Catalogue Item.
**(Available Since MobiControl v15.0.0)**

**Parameters:**
- `name` (Required): Type: string. Description: user group name

**Responses:**
- **204**:

---

### DELETE /security/userGroup/{name}/catalogueItemReferenceId

**Summary:** Remove the user group rights based on the catalogue reference

**Description:** Remove rights associated with a Catalogue Item to a specific user group. Requires the caller to be granted the "WebConsole" global permission and the right to view the specified Catalogue Item.
**(Available Since MobiControl v15.0.0)**

**Parameters:**
- `name` (Required): Type: string. Description: user group name

**Responses:**
- **204**:

---
### GET /security/{portalName}/externalAuthentication

**Summary:** Returns the authentication setting for specified portal

**Description:** Returns the authentication setting for specified portal hosted along with MobiControl
Requires the caller be granted the "Web Console Access" permission
**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `portalName` (Required): Type: string. Description: Security portal name e.g. SSP, IOSProfileCatalog, WebConsole

**Responses:**
- **200**: Returns external authentication security settings
- **401**: Unauthorized access
- **403**: Forbidden

---

### PUT /security/{portalName}/externalAuthentication

**Summary:** Updates the authentication setting for specified portal

**Description:** Updates the authentication setting for specified portal hosted along with MobiControl
Requires the caller be granted the "Manage Console Authentication" permission
**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `portalName` (Required): Type: string. Description: Security portal name e.g. SSP, IOSProfileCatalog and WebConsole
- `settings` (Required): Type: object. Description: Security settings object contains the authentication type and authentication service name.

**Responses:**
- **204**: Successfully updated the authentication settings
- **400**: Contract validation failed
- **401**: Unauthorized access
- **403**: Forbidden

---
### PUT /security/authentication

**Summary:** Updates the authentication setting for MC webconsole

**Description:** Updates the authentication setting to be used for MC Webconsole
**(Available Since MobiControl v15.3.0)**
Requires the caller be granted the "Manage Console Authentication" permission

**Parameters:**
- `authenticationSettings` (Required): Type: object.

**Responses:**
- **204**: Successfully updated the authentication config
- **400**: Contract validation failed
- **401**: Unauthorized access
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:<br /><ol><li>3103 - SOTI Identity is not configured.</li></ol>

---

### GET /security/authentication

**Summary:** Returns the authentication setting for MC Webconsole

**Description:** Returns the authentication setting to be used for MC Webconsole
**(Available Since MobiControl v15.3.0)**
Requires the caller be granted the "Web Console Access" permission

**Responses:**
- **401**: Unauthorized access

---
### POST /security/currentUser/deviceGroupRights

**Summary:** Report on access permission(s) for current user for a given list of Device Groups and list of Permission Names

**Description:** Retrieve information on the permission status for a list of Device Groups for the current user in MobiControl. The "referenceId" refers to the primary identifier of the Device Group. This requires the caller to be granted the “Access Web Console” permission.
**(Available Since MobiControl v2024.0.0)**

**Parameters:**
- `request` (Required): Type: object. Description: A list of Device Group reference IDs and permission names

**Responses:**
- **200**: Returns device group permissions
- **400**: Contract validation failed
- **401**: Unauthorized access
- **403**: Forbidden

---
### POST /security/currentUser/filterPermissions

**Summary:** Report on access permission for current user

**Description:** Retrieve information on whether the current user can access / execute a specific action in MobiControl. Actions typically are view profiles, manage rules etc.  This requires the caller to be granted the “Access Web Console” permission.
**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `permissions` (Required): Type: object. Description: The permissions Array that will be filtered if User does not has permission.

**Responses:**
- **200**: Array of User's permissions

---
### GET /security/passwordpolicy1

**Summary:** New Retrieve Administrative Password Policy

**Description:** Returns the administrative password policy configured in Console Security and applies to local administrators. Requires the caller be granted the "Access Web Console" permission.
**(Available Since MobiControl v14.0.0)**

**Responses:**
- **200**: Password policy

---
## Server Health

### GET /servers/database/status

**Summary:** Gets the Health Status of SQL Server and MobiControl databases.

**Description:** Get the health status of SQL Server and MobiControl databases. This API also returns information about your MobiControl archive database and the temporary database. Requires the caller be granted "View System Health" permission.

**(Available Since MobiControl v15.3.0)**

**Responses:**
- **200**:
- **401**: Unauthorized access
- **403**: Forbidden

---
### GET /servers/deploymentServer/status

**Summary:** Gets the status of the Deployment Servers.

**Description:** Returns status information about all Deployment Servers. This includes the name, number of connected devices, status and queue length for each Deployment Server, as stored in the MobiControl database. Requires the caller be granted "View System Health" permission.

**(Available Since MobiControl v15.3.0)**

**Responses:**
- **200**:
- **401**: Unauthorized access
- **403**: Forbidden

---
### GET /servers/deploymentServer/{dsName}/status

**Summary:** Gets the status of a specific Deployment Server.

**Description:** Returns status information as stored in the MobiControl Database about the Deployment Server specified by {dsName}. Requires the caller be granted "View System Health" permission.

**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `dsName` (Required): Type: string. Description: Host name of the Deployment Server

**Responses:**
- **200**:
- **401**: Unauthorized access
- **403**: Forbidden

---
### GET /servers/managementServer/status

**Summary:** Gets the status of the Management Servers.

**Description:** Get the status of all Management Servers powering the MobiControl environment. Requires the caller be granted "View System Health" permission.

**(Available Since MobiControl v15.3.0)**

**Responses:**
- **200**:
- **401**: Unauthorized access
- **403**: Forbidden

---
### GET /servers/managementServer/{msName}/status

**Summary:** Gets the status of a specific Management Server.

**Description:** Get the status detail of a specific Management Server powering the MobiControl environment. Requires the caller be granted "View System Health" permission.

**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `msName` (Required): Type: string. Description: Host name of the Management Server

**Responses:**
- **200**:
- **401**: Unauthorized access
- **403**: Forbidden

---
## Servers

### GET /servers

**Summary:** Get All Servers

**Description:** Returns a list of Management and Deployment Servers powering the MobiControl environment. Requires the caller be granted "Web Console Access" permission.

**(Available Since MobiControl v13.2.0)**

**Parameters:**
- `forceDsStatusRefresh`: Type: boolean. Description: When set to true, Deployment Server(s) are notified to update status prior to API response. When set to false, API response will return the last known values from the MobiControl Database
- `getAdditionalCertificates`: Type: boolean. Description: Get additional certificates including DSE, APNS, etc

**Responses:**
- **200**: List of DS, MS, and Assist server(s).

---
### GET /servers/logLevels

**Summary:** Returns a list of Log Levels

**Description:** Returns a list of Log Levels currently set for each of the MobiControl's functional areas


         Requires the caller be granted the "Web Console Access" permission

**(Available Since MobiControl v15.3.0)**

**Responses:**
- **200**:
- **401**: Unauthorized access

---

### PUT /servers/logLevels

**Summary:** Updates the specific Log Level

**Description:** Update the Log Levels for the specific MobiControl's functional area. Multiple functional areas can be updated in single attempt.


         Requires the caller be granted the "Manage Servers and Global Settings" permission

**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `systemLogLevel` (Required): Type: object. Description: Define the values in key value format for the desired MC functional area. Check Model for details.

**Responses:**
- **204**: Successfully set log levels
- **400**: Contract validation failed
- **401**: Unauthorized access

---
## Signal Health

### GET /signal/signalHealth/services

**Summary:** Returns list of the health of all Signal Services.

**Description:** Retrieves a list of the health status of all Signal Services.


         Requires the caller be granted the "View System Health" permission.

**(Available since MobiControl v2024.0.0)**


**Responses:**
- **200**: Operation Successful.
- **401**: Failed to authenticate the request.
- **403**: Forbidden.
- **500**: Internal Server Error.
- **503**: Service Unavailable.

---
## Signal Policies

### PUT /signal/signalPolicies/{referenceId}/enable/{enabled}

**Summary:** Enable/Disable the specific Signal Policy.

**Description:** Enables or disables the specified Signal Policy.


         Requires the caller be granted the "Manage Signal Policy" permission.

**(Available since MobiControl v2024.0.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id of Signal Policy.
- `enabled` (Required): Type: string. Description: True or False.

**Responses:**
- **200**: Success.
- **400**: Contract Validation Failed.
- **401**: Failed to authenticate the request.
- **403**: Forbidden.
- **500**: Internal Server Error.
- **503**: Service Unavailable.

---
### GET /signal/signalPolicies

**Summary:** Returns all Signal Policies.

**Description:** Retrieves all Signal Policies from the server.


         Requires the caller be granted the "View Signal Policy" permission.

**(Available since MobiControl v2024.0.0)**


**Responses:**
- **200**: Success.
- **401**: Failed to authenticate the request.
- **403**: Forbidden.
- **500**: Internal Server Error.
- **503**: Service Unavailable.

---
### GET /signal/signalPolicies/actionSearch

**Summary:** Returns all Signal Policies filtered by Action.

**Description:** Retrieves all Signal Policies from the server that are using the specified action with the specified parameter value.


         Requires the caller be granted the "View Signal Policy" permission.

**(Available since MobiControl v2024.0.0)**


**Parameters:**
- `actionName` (Required): Type: string. Description: Name of action to filter on.
- `parameterName`: Type: string. Description: Name of parameter used by action to check.
- `parameterValue`: Type: string. Description: Value of parameter used by action to check.

**Responses:**
- **200**: Success.
- **400**: Contract Validation Failed.
- **403**: Forbidden.
- **500**: Internal Server Error.
- **503**: Service Unavailable.

---
### GET /signal/signalPolicies/webhookSearch

**Summary:** Retrieves all Signal Policies that are using a specific webhook action.

**Description:** Retrieves all Signal Policies from the server that are using a specific webhook action.


         Requires the caller be granted the "View Signal Policy" permission.

**(Available since MobiControl v2024.0.0)**


**Parameters:**
- `webhookId` (Required): Type: string. Description: Reference Id of the Webhook.

**Responses:**
- **200**: Success.
- **400**: Contract Validation Failed.
- **401**: Failed to authenticate the request.
- **403**: Forbidden.
- **500**: Internal Server Error.
- **503**: Service Unavailable.

---
### GET /signal/signalPolicies/{referenceId}

**Summary:** Retrieves details about the specified Signal Policy.

**Description:** Retrieves details about the specified Signal Policy from the server.


         Requires the caller be granted the 'View Signal Policies' permission.

**(Available since MobiControl v2024.0.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id of the Signal Policy.

**Responses:**
- **200**: Success.
- **400**: Contract Validation Failed.
- **401**: Failed to authenticate the request.
- **403**: Forbidden.
- **500**: Internal Server Error.
- **503**: Service Unavailable.

---

### DELETE /signal/signalPolicies/{referenceId}

**Summary:** Deletes an existing Signal Policy.

**Description:** Deletes the specified Signal Policy.


         Requires the caller be granted the "Manage Signal Policy" permission.

**(Available since MobiControl v2024.0.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id of Signal Policy.

**Responses:**
- **204**: Success.
- **400**: Contract Validation Failed.
- **401**: Failed to authenticate the request.
- **403**: Forbidden.
- **500**: Internal Server Error.
- **503**: Service Unavailable.

---
### GET /signal/signalPolicies/{referenceId}/activityLog

**Summary:** Returns the Activity Log for a specific Signal Policy.

**Description:** Retrieves the activity log associated with the specified Signal Policy.


         Requires the caller be granted the "View Signal Policy" permission.

**(Available since MobiControl v2024.0.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id of Signal Policy.
- `skip`: Type: integer. Description: Where in the list to begin.
- `take`: Type: integer. Description: The size of the list to be returned.

**Responses:**
- **200**: Success.
- **400**: Contract Validation Failed.
- **401**: Failed to authenticate the request.
- **403**: Forbidden.
- **500**: Internal Server Error.
- **503**: Service Unavailable.

---
### GET /signal/signalPolicies/{referenceId}/changelog

**Summary:** Returns the Change Log for a specific Signal Policy.

**Description:** Retrieves the change log associated with the specified Signal Policy.


         Requires the caller be granted the "View Signal Policy" permission.

**(Available since MobiControl v2024.0.0)**


**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id of Signal Policy.

**Responses:**
- **200**: Success.
- **400**: Contract Validation Failed.
- **401**: Failed to authenticate the request.
- **403**: Forbidden.
- **500**: Internal Server Error.
- **503**: Service Unavailable.

---
## Signal Schema

### GET /signal/domainschemas

**Summary:** Returns the Signal Domain Schemas.

**Description:** Retrieves Signal Policy domain schemas from the server.


         Requires the caller be granted the "View Signal Policy" permission.

**(Available since MobiControl v2024.0.0)**


**Parameters:**
- `locale` (Required): Type: string. Description: Locale used when returning language-specific strings.

**Responses:**
- **200**: Success.
- **400**: Contract Validation Failed.
- **401**: Failed to authenticate the request.
- **403**: Forbidden.
- **500**: Internal Server Error.
- **503**: Service Unavailable.

---
## Smtp

### POST /smtp/connections

**Parameters:**
- `connection` (Required): Type: object.

**Responses:**
- **200**:

---

### GET /smtp/connections

**Responses:**
- **200**:

---
### DELETE /smtp/connections/{referenceId}

**Parameters:**
- `referenceId` (Required): Type: string.

**Responses:**
- **204**:

---

### GET /smtp/connections/{referenceId}

**Parameters:**
- `referenceId` (Required): Type: string.

**Responses:**
- **200**:

---

### PUT /smtp/connections/{referenceId}

**Parameters:**
- `referenceId` (Required): Type: string.
- `connection` (Required): Type: object.

**Responses:**
- **200**:

---
### POST /smtp/connections/actions

**Parameters:**
- `action` (Required): Type: object.

**Responses:**
- **204**:

---
## Soti Assist Configuration

### GET /sotiOne/assist

**Summary:** Returns the SOTI Assist URL configuration

**Description:** Returns the configuration of SOTI Assist server
Requires the caller be granted the "Web Console Access" permission
**(Available Since MobiControl v15.3.0)**

**Responses:**
- **200**: URL configuration returned successfully
- **401**: Unauthorized access
- **403**: Forbidden

---

### PUT /sotiOne/assist

**Summary:** Updates the SOTI Assist URL configuration

**Description:** Updates the configuration of SOTI Assist server
Requires the caller be granted the "Manage Servers and Global Settings" permission
**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `sotiAssistConfiguration` (Required): Type: object. Description: Define the values in key value format for the SOTI Assist URI. Only http/https URIs are allowed.Check Model for details

**Responses:**
- **204**: Successfully add SOTI Assist Configuration
- **400**: Contract validation failed
- **401**: Unauthorized access
- **403**: Forbidden

---
## Soti Connect Configuration

### GET /sotiOne/connect

**Summary:** Returns the SOTI Connect URL configuration

**Description:** Returns the configuration of SOTI Connect server
Requires the caller be granted the "Web Console Access" permission
**(Available Since MobiControl v15.3.0)**

**Responses:**
- **200**: URL configuration returned successfully
- **401**: Unauthorized access
- **403**: Forbidden

---

### PUT /sotiOne/connect

**Summary:** Updates the SOTI Connect URL configuration

**Description:** Updates the configuration of SOTI Connect server
Requires the caller be granted the "Manage Servers and Global Settings" permission
**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `sotiConnectConfiguration` (Required): Type: object. Description: Define the values in key value format for the SOTI Connect URI. Only http/https URIs are allowed.Check Model for details

**Responses:**
- **204**: Successfully add SOTI Connect Configuration
- **400**: Contract validation failed
- **401**: Unauthorized access
- **403**: Forbidden

---
## Soti Snap Configuration

### GET /sotiOne/snap

**Summary:** Returns the SOTI Snap URL configuration

**Description:** Returns the configuration of SOTI Snap server
Requires the caller be granted the "Web Console Access" permission
**(Available Since MobiControl v15.3.0)**

**Responses:**
- **200**: URL configuration returned successfully
- **401**: Unauthorized access
- **403**: Forbidden

---

### PUT /sotiOne/snap

**Summary:** Updates the SOTI Snap URL configuration

**Description:** Updates the configuration of SOTI Snap server
Requires the caller be granted the "Manage Servers and Global Settings" permission
**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `sotiSnapConfiguration` (Required): Type: object. Description: Define the values in key value format for the SOTI Snap URI. Only http/https URIs are allowed.Check Model for details

**Responses:**
- **204**: Successfully add SOTI Snap Configuration
- **400**: Contract validation failed
- **401**: Unauthorized access
- **403**: Forbidden

---
## System Configuration

### GET /systemconfiguration/syslog

**Summary:** Retrieve Syslog Configuration

**Description:** Returns the current Syslog configuration.
**(Available Since MobiControl v14.2.0)**

**Responses:**
- **200**:

---

### PUT /systemconfiguration/syslog

**Summary:** Update Syslog Configuration

**Description:** Update Syslog configuration to the global setting.
Requires the caller be granted the "Manage Servers and Global Settings.
**(Available Since MobiControl v14.2.0)**

**Parameters:**
- `configuration` (Required): Type: object.

**Responses:**
- **200**:

---

### DELETE /systemconfiguration/syslog

**Summary:** Delete Syslog Configuration

**Description:** Delete Syslog configuration from the global setting.
Requires the caller be granted the "Manage Servers and Global Settings.
**(Available Since MobiControl v14.2.0)**

**Responses:**
- **204**:

---
### POST /systemconfiguration/syslog/tests

**Summary:** Test Syslog Connectivity

**Description:** Test Syslog connectivity
Requires the caller be granted the "Manage Servers and Global Setting" permission."
**(Available Since MobiControl v14.2.0)**

**Parameters:**
- `syslogConfigurationTest` (Required): Type: object.

**Responses:**
- **200**:

---
### GET /systemconfiguration/globalproxy

**Summary:** Retrieve Global Proxy Configuration

**Description:** Returns the current global proxy configuration.
Requires the caller be granted "Web Console Access" permission.
**(Available Since MobiControl v14.3.1)**

**Responses:**
- **200**:

---

### PUT /systemconfiguration/globalproxy

**Summary:** Replace Global Proxy Configuration

**Description:** Adds or updates global proxy configuration. If configuration already exists then this action will update it, otherwise configuration will be added.
Requires the caller be granted the "Manage Servers and Global Settings.
**(Available Since MobiControl v14.3.1)**

**Parameters:**
- `proxySetting` (Required): Type: object.

**Responses:**
- **200**:

---

### DELETE /systemconfiguration/globalproxy

**Summary:** Delete Global Proxy Configuration

**Description:** Deletes global proxy configuration.
Requires the caller be granted the "Manage Servers and Global Settings.
**(Available Since MobiControl v14.3.1)**

**Responses:**
- **204**:

---
### PUT /systemconfiguration/globalproxy/isenabled

**Summary:** Enable/Disable Global Proxy

**Description:** Enables/Disables global proxy.
Requires the caller be granted the "Manage Servers and Global Settings.
**(Available Since MobiControl v14.3.1)**

**Parameters:**
- `enable` (Required): Type: boolean.

**Responses:**
- **200**:

---
### POST /systemconfiguration/globalproxy/validate

**Summary:** Validate Global Proxy Configuration

**Description:** Validate global proxy configuration.
**(Available Since MobiControl v14.3.1)**
Requires the caller be granted the "Manage Servers and Global Settings.

**Parameters:**
- `proxySetting` (Required): Type: object.

**Responses:**
- **200**:

---
### GET /systemconfiguration/cloudlinkagent

**Summary:** Retrieve CloudLink settings

**Description:** Retrieve CloudLink settings, such as compatible CloudLink version and URI for CloudLink installer
**(Available Since MobiControl v15.0.0)**

**Responses:**
- **200**: CloudLink settings

---
## System Health

### GET /systemHealth/settings

**Summary:** Gets the System Health Advanced Analytics Settings.

**Description:** Get the status of System Health advanced analytics charts and if data is being collected by MobiControl to display the charts. This API also gets the rate at which the data is being collected from MobiControl to be displayed in charts. This API is only available with SOTI Premium Plus and Enterprise Plus Service. Requires the caller be granted "Manage System Health" permission.

**(Available Since MobiControl v15.3.0)**

**Responses:**
- **200**:
- **401**: Unauthorized access
- **403**: Forbidden
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:<br /><ol><li>6600 - Failed to retrieve System Health settings because the MobiControl server does not have the required support contract. System Health settings are only available with SOTI Premium Plus and Enterprise Plus Service.</li></ol>

---

### PUT /systemHealth/settings

**Summary:** Update the System Health Advanced Analytics Settings.

**Description:** This API is only available with SOTI Premium Plus and Enterprise Plus Service. When collect system data setting is disabled, the advanced analytics charts will not be shown and MobiControl system metrics data will not be collected. This API also allows to configure the rate at which the metrics data is collected from MobiControl to be displayed in charts. Requires the caller be granted "Manage System Health" permission.

**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `systemHealthSettings` (Required): Type: object. Description: System Health Settings

**Responses:**
- **204**: System Health Settings have been updated
- **401**: Unauthorized access
- **403**: Forbidden
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:<br /><ol><li>6601 - Failed to update System Health settings because the MobiControl server does not have the required support contract. System Health settings are only available with SOTI Premium Plus and Enterprise Plus Service.</li></ol>

---
### GET /systemHealth/metrics

**Summary:** Gets System Health metrics data for specified servers

**Description:** Gets the metrics data for specified servers. You can specify start and end date time to see metrics data for the specified time period given the data is available. System Health metrics is only available with SOTI Premium Plus and Enterprise Plus Service. Requires the caller be granted "View System Health" permission.

**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `startTime` (Required): Type: string. Description: Start Date Time. Format Year-Month-DayTHour:Minutes:SecondsZ (e.g. 2020-12-14T19:00:00Z)
- `endTime` (Required): Type: string. Description: End Date Time. Format Year-Month-DayTHour:Minutes:SecondsZ (e.g. 2020-12-14T20:00:00Z)
- `ds`: Type: array. Description: Host name of the Deployment Server (e.g. ds1 ds2)
- `ms`: Type: array. Description: Host name of the Management Server (e.g. ms1 ms2)
- `m`: Type: array. Description: Metric name (e.g. CPU Usage Available RAM Check-Ins)
- `timeDensity`: Type: string. Description: Time Density Frequency to define the time interval between each data point. Format [[h]ours | [m]inutes | [s]econds]:value (e.g. m:5)
- `includeSummary`: Type: boolean. Description: Should the summary be included in output
- `includeStatistics`: Type: boolean. Description: Should the statistics be included in output
- `includeHeader`: Type: boolean. Description: Should the header be included in output
- `initialLoad`: Type: boolean. Description: This is the initial or first load of data required, use internal mechanisms to retrieve necessary data

**Responses:**
- **200**: Returns System Health metrics
- **401**: Unauthorized access
- **403**: Forbidden
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:<br /><ol><li>6602 - Failed to retrieve System Health metrics because the MobiControl server does not have the required support contract. System Health metrics are only available with SOTI Premium Plus and Enterprise Plus Service.</li></ol>

---
## System Maintenance

### GET /system/maintenance/configuration

**Summary:** Returns the configuration for log truncation &amp; maintenance

**Description:** Returns the configuration for log  truncation &amp; maintenance schedule and other related settings
Requires the caller be granted the "Web Console Access" permission
**(Available Since MobiControl v15.4.0)**

**Responses:**
- **401**: Unauthorized access
- **403**: Forbidden

---

### PUT /system/maintenance/configuration

**Summary:** Updates the configuration for log maintenance

**Description:** Updates the configuration for log  truncation &amp; maintenance schedule and other related settings
Requires the caller be granted the "Configure Database Maintenance" permission
**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `configuration` (Required): Type: object. Description: contract for log  truncation &amp; maintenance schedule

**Responses:**
- **204**: Successfully saved
- **400**: Contract validation failed
- **401**: Unauthorized access
- **403**: Forbidden

---
### POST /system/maintenance/actions/truncateLogs

**Summary:** Creates a new log truncation request

**Description:** Creates a new log truncation request for logs, alerts, app logs
Requires the caller be granted the "Configure Database Maintenance" permission
**(Available Since MobiControl v15.4.0)**

**Parameters:**
- `truncateLogsConfiguration` (Required): Type: object. Description: contract to request truncation of logs

**Responses:**
- **204**: Successfully requested the log truncation
- **400**: Contract validation failed
- **401**: Unauthorized access
- **403**: Forbidden
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:<br /><ol><li>6200 - Invalid Folder Path</li><li>6201 - No write permission</li></ol>

---
## Terms And Conditions

### GET /termsAndConditions

**Responses:**
- **200**:

---

### POST /termsAndConditions

**Responses:**
- **200**:

---
### GET /termsAndConditions/{referenceId}/versions

**Parameters:**
- `referenceId` (Required): Type: string.

**Responses:**
- **200**:

---
### GET /termsAndConditions/{referenceId}/versions/{versionNumber}

**Parameters:**
- `referenceId` (Required): Type: string.
- `versionNumber` (Required): Type: integer.

**Responses:**
- **200**:

---
### PUT /termsAndConditions/{referenceId}

**Parameters:**
- `referenceId` (Required): Type: string.

**Responses:**
- **200**:

---

### DELETE /termsAndConditions/{referenceId}

**Parameters:**
- `referenceId` (Required): Type: string.

**Responses:**
- **204**:

---
## User Group Management

### GET /security/principal/userGroups

**Summary:** Returns a list of directories.

**Description:** This API retrieves all directories

Requires the caller be granted the 'Manage Console Security' or ' Lookup Users and Group Membership' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `searchString`: Type: string. Description: The keyword to be searched in the directory name.
- `memberOf`: Type: array. Description: Input a list of the reference id's of roles, mapped to the directory.
- `kind`: Type: string. Description: Select the type of directory.
- `order`: Type: string. Description: Defines the sorting order by property. Pass the value as -property for descending, and +property for ascending.
- `skip`: Type: integer. Description: Input the first X (count) entries that should not be returned.
- `take`: Type: integer. Description: Input the number of entries to be returned, after skipping over the 'skip' count.

**Responses:**
- **200**: Successfully returns a list of Directories.
- **400**: Contract validation failed.
- **403**: Forbidden.

---
### DELETE /security/principal/userGroups/{referenceId}

**Summary:** Deletes the specified directory.

**Description:** This API deletes a selected directory mapping from MobiControl

Requires the caller be granted the 'Manage Console Security' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id for a directory.

**Responses:**
- **204**: Successfully deleted specified Directory.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6510: Deletion not allowed</li><li>6511: Insufficient edit permission</li><li>6518: Directory deletion restricted through MobiControl</li><li>6519: Directory deletion not allowed</li></ol>

---

### GET /security/principal/userGroups/{referenceId}

**Summary:** Returns the details of a directory.

**Description:** This API retrieves the details of a directory specified by its Reference Id.

Requires the caller be granted the 'Manage Console Security' or ' Lookup Users and Group Membership' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id for a directory.

**Responses:**
- **200**: Successfully returns the specified directory.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6512: Insufficient View Permission</li></ol>

---
### GET /security/principal/userGroups/{referenceId}/roles

**Summary:** Returns a list of roles for a directory.

**Description:** This API retrieves all roles that are mapped to a directory specified by its Reference Id.

Requires the caller be granted the 'Manage Console Security' or 'Lookup Users and Group Membership' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id for a directory.

**Responses:**
- **200**: Successfully returns a list of roles.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6512: Insufficient View Permission</li></ol>

---

### PUT /security/principal/userGroups/{referenceId}/roles

**Summary:** Updates the roles associated to a user group.

**Description:** Updates the roles associated to a user group. Here, the roles refer to the MobiControl default roles - MobiControl Administrators, MobiControl Technicians, MobiControl Viewers and BYOD.

Requires the caller be granted the 'Manage Console Security' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id for a directory.
- `roleReferenceIds` (Required): Type: object. Description: Reference Id's for roles.

**Responses:**
- **200**: Successfully returns a list of roles.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6511: Insufficient Edit Permission</li><li>6520: Partially Updated</li></ol>

---
### GET /security/principal/userGroups/{referenceId}/users

**Summary:** Returns a list of users for a directory.

**Description:** This API retrieves all users that are mapped to a directory specified by its Reference Id.

Requires the caller be granted the 'Manage Console Security' or ' Lookup Users and Group Membership' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id for a directory.
- `includeHiddenUsers`: Type: boolean. Description: Indicates whether to include hidden users.
- `searchString`: Type: string. Description: User name search string.

**Responses:**
- **200**: Successfully returns a list of users.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6512: Insufficient View Permission</li></ol>

---
### GET /security/principal/userGroups/{referenceId}/catalogueItemReference

**Summary:** Returns the catalogue reference for a directory.

**Description:** This API retrieves the catalogue reference ID for a directory

Requires the caller be granted the 'Manage Console Security' or 'Lookup Users and Group Membership' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id for a directory.

**Responses:**
- **200**: Successfully returns the specified catalogue reference id.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6512: Insufficient View Permission</li></ol>

---

### POST /security/principal/userGroups/{referenceId}/catalogueItemReference

**Summary:** Creates a catalogue item for a directory.

**Description:** This API creates a new catalogue item for a directory

Requires the caller be granted the 'Manage Console Security' or 'Lookup Users and Group Membership' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id for a directory.

**Responses:**
- **200**: Successfully returns the specified catalogue reference id.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6511: Insufficient Edit Permission</li></ol>

---

### DELETE /security/principal/userGroups/{referenceId}/catalogueItemReference

**Summary:** Deletes a catalogue item for a directory.

**Description:** This API deletes a catalogue reference ID for a directory

Requires the caller be granted the 'Manage Console Security' or 'Lookup Users and Group Membership' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id for a directory.

**Responses:**
- **204**: Successfully deleted specified catalogue reference id.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6511: Insufficient Edit Permission</li></ol>

---
### GET /security/principal/userGroups/{referenceId}/{scope}/rights

**Summary:** Returns the permissions allocated to a UserGroup.

**Description:** Returns the permissions allocated to a UserGroup. These UserGroups can be LDAP or IdP UserGroups.

Requires the caller be granted the "Manage Console Security" permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference identifier.
- `scope` (Required): Type: string. Description: The scope.

**Responses:**
- **400**: Contract validation failed.
- **403**: Forbidden.

---

### PUT /security/principal/userGroups/{referenceId}/{scope}/rights

**Summary:** Updates the general permissions for a directory.

**Description:** This API updates the general permissions for a selected directory specified by its Reference Id.

Requires the caller be granted the 'Manage Console Security' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id for a directory.
- `scope` (Required): Type: string. Description: Authorization scope.
- `rights` (Required): Type: object. Description: Schema for permission and its boolean value.

**Responses:**
- **200**: Successfully returns a list of right summary.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6507: Invalid permission name.</li><li>6508: Duplicate permission name.</li><li>6509: Invalid parent child state.</li><li>6511: Insufficient Edit Permission.</li><li>6515: Security right not found.</li></ol>

---
### GET /security/principal/userGroups/{referenceId}/deviceGroups/{deviceGroupReferenceId}/rights

**Summary:** Returns device group permission for a directory.

**Description:** This API retrieves all device group permission for a directory

Requires the caller be granted the 'Manage Console Security' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id for a directory.
- `deviceGroupReferenceId` (Required): Type: string. Description: Reference Id of a device group.

**Responses:**
- **200**: Successfully returns a list of right summary.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6512: Insufficient View Permission</li></ol>

---

### PUT /security/principal/userGroups/{referenceId}/deviceGroups/{deviceGroupReferenceId}/rights

**Summary:** Updates the device group permission for a directory.

**Description:** This API updates all device group permission Rights belonging to a single directory

Requires the caller be granted the 'Manage Console Security' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id for a directory.
- `deviceGroupReferenceId` (Required): Type: string. Description: Reference Id for a device group.
- `rights` (Required): Type: object. Description: Schema for permission and its boolean value.

**Responses:**
- **200**: Successfully returns a list of right summary.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6507: Invalid permission name</li><li>6508: Duplicate permission name</li><li>6509: Security right has invalid parent/child state</li><li>6511: Insufficient Edit Permission</li><li>6515: Security right not found</li></ol>

---
### POST /security/principal/userGroups/ldapUserGroup

**Summary:** Creates a new LDAP directory.

**Description:** This API adds a new LDAP directory into MobiControl

Requires the caller be granted the 'Manage Console Security' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `ldapUserGroup` (Required): Type: object. Description: Schema for adding a directory.

**Responses:**
- **200**: Successfully created a new ldap directory.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6503: Duplicate LDAP directory name</li><li>6504: Duplicate SID</li></ol>

---
### POST /security/principal/userGroups/ssoUserGroup

**Summary:** Creates a new SSO directory.

**Description:** Add a new Identity Provider directory into MobiControl, it can be either from SOTI Identity or External Identity

Requires the caller be granted the 'Manage Console Security' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `ssoUserGroup` (Required): Type: object. Description: Schema for adding a directory.

**Responses:**
- **200**: Successfully created a new sso directory.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6505: Duplicate SSO directory name</li><li>6517: Directory creation not allowed</li></ol>

---
### GET /security/principal/userGroups/{referenceId}/logs

**Summary:** Returns the logs for a directory.

**Description:** This API retrieves logs for a directory specified by its Reference Id.

Requires the caller be granted the 'Manage Console Security' or ' Lookup Users and Group Membership' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference id of a directory.
- `startDate` (Required): Type: string. Description: The date starting which the logs will be fetched.
- `endDate` (Required): Type: string. Description: The date till which the logs will be fetched.
- `logSeverities`: Type: array. Description: Select the type of log.
- `orderByDesc`: Type: boolean. Description: Defines the sorting order by timestamp. Pass the value as true for descending, false for ascending.
- `skip`: Type: integer. Description: Input the first X (count) entries that should not be returned.
- `take`: Type: integer. Description: Input the number of entries to be returned, after skipping over the 'skip' count.

**Responses:**
- **200**: Successfully returns a list of user log entry.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><li>6512: Insufficient view permission</li>

---
### GET /security/principal/userGroups/{referenceId}/logs/actions/download

**Summary:** Returns the CSV file of logs for a directory.

**Description:** This API exports a CSV file of logs for a directory specified by its Reference Id.

Requires the caller be granted the 'Manage Console Security' or 'Lookup Users and Group Membership' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The unique Identifier for the directory.
- `reportHeaderFields` (Required): Type: string. Description: Comma separated field names to be included in the csv file.
- `logSeverities`: Type: array. Description: List of log severities to include into result such as Information, Warning or Error.
- `startDate` (Required): Type: string. Description: The date starting which the logs will be fetched (UTC format).
- `endDate` (Required): Type: string. Description: The date till which the logs will be fetched (UTC format).
- `format`: Type: string. Description: File format [Currently only csv is supported.].
- `timeZoneOffset`: Type: integer. Description: Time zone offset from UTC (in Minutes).
- `orderByDesc`: Type: boolean. Description: Defines the sorting order by timestamp. Pass the value as true for descending, false for ascending.
- `Skip`: Type: integer.
- `Take`: Type: integer.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.

---
## User Management

### PUT /security/principal/users/mobiControlUser/{referenceId}/lockAccount

**Summary:** Locks the specified user account.

**Description:** Locks the user account referred to by referenceId.

Requires the caller be granted the 'Manage Console Security' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference id of mobi control user.
- `lockAccount` (Required): Type: object. Description: The lock account info.

**Responses:**
- **204**: Successfully updated a user.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6511: Insufficient Edit Permission</li></ol>

---
### GET /security/principal/users

**Summary:** Returns all users in MobiControl.

**Description:** Returns all users in MobiControl.

Requires the caller be granted the 'Lookup Users and Groups Membership' or the 'Manage Console Security' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `includeHiddenUsers`: Type: boolean. Description: Indicates whether to include hidden users.
- `searchString`: Type: string. Description: User name search string.
- `memberOf`: Type: array. Description: Only return users that are members of one or more of the specified groups.
- `kind`: Type: string. Description: Only returns users of this kind.
- `order`: Type: string. Description: Defines the sorting order by property. Pass the value as -property for descending, and +property for ascending.
- `skip`: Type: integer. Description: Input the first X (count) entries that should not be returned.
- `take`: Type: integer. Description: Input the number of entries to be returned, after skipping over the 'skip' count.

**Responses:**
- **200**: Successfully returns the user.
- **400**: Contract validation failed.
- **403**: Forbidden.

---
### POST /security/principal/users/mobiControlUser

**Summary:** Creates a new local user.

**Description:** Creates a new local user.

Requires the caller be granted the 'Manage Console Security' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `user` (Required): Type: object. Description: MobiControl user.

**Responses:**
- **200**: Successfully created a user.
- **400**: Contract validation failed.
- **403**: Forbidden.

---
### POST /security/principal/users/ldapUser

**Summary:** Creates a new LDAP user.

**Description:** Creates a new LDAP user.

Requires the caller be granted the 'Manage Console Security' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `user` (Required): Type: object. Description: LDAP user.

**Responses:**
- **200**: Successfully created a user.
- **400**: Contract validation failed.
- **403**: Forbidden.

---
### PUT /security/principal/users/mobiControlUser/{referenceId}

**Summary:** Updates the user referred to by the referenceId.

**Description:** Updates the user referred to by the referenceId.

Requires the caller be granted the 'Manage Console Security' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: User reference id.
- `user` (Required): Type: object. Description: MobiControl user.

**Responses:**
- **200**: Successfully updates the user.
- **400**: Contract validation failed.
- **403**: Forbidden.

---
### GET /security/principal/users/{referenceId}

**Summary:** Returns the user details for a specified user.

**Description:** Returns the user details for a specified user.

Requires the caller be granted the 'Lookup Users and Groups Membership' or the 'Manage Console Security' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: User reference id.

**Responses:**
- **200**: Successfully returns the user.
- **400**: Contract validation failed.
- **403**: Forbidden.

---

### DELETE /security/principal/users/{referenceId}

**Summary:** Deletes the user referred to by the referenceId.

**Description:** Deletes the user referred to by the referenceId.

Requires the caller be granted the 'Manage Console Security' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: User reference id.

**Responses:**
- **400**: Contract validation failed.
- **403**: Forbidden.
- **204**: No content.

---
### GET /security/principal/users/{referenceId}/roles

**Summary:** Returns a list of roles for a user.

**Description:** This API retrieves all roles that are mapped to a user specified by its Reference Id.

Requires the caller be granted the 'Manage Console Security' or 'Lookup Users and Group Membership' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference id of a user.

**Responses:**
- **200**: Successfully returns a list of roles.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6512: Insufficient View Permission</li></ol>

---

### PUT /security/principal/users/{referenceId}/roles

**Summary:** Updates the specified roles for a user.

**Description:** This API updates the roles that map to a user

Requires the caller be granted the 'Manage Console Security' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id for a user.
- `roleReferenceIds` (Required): Type: object. Description: Reference Id's for roles.

**Responses:**
- **200**: Returns a list of roles.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6511: Insufficient Edit Permission</li><li>6520: Partially Updated</li></ol>

---
### GET /security/principal/users/{referenceId}/userGroups

**Summary:** Returns the role associated with the specified user.

**Description:** Returns the role associated with the specified user.

Requires the caller be granted the 'Lookup Users and Groups Membership' or the 'Manage Console Security' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: User reference id.

**Responses:**
- **200**: Successfully returns the role associated with the specified user.
- **400**: Contract validation failed.
- **403**: Forbidden.

---
### GET /security/principal/users/{referenceId}/catalogueItemReference

**Summary:** Returns the catalogue reference for a user.

**Description:** This API retrieves the catalogue reference ID for a user specified by its Reference Id.

Requires the caller be granted the 'Manage Console Security' or ' Lookup Users and Group Membership' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id for a user.

**Responses:**
- **200**: Successfully returns the specified catalogue reference id.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6512: Insufficient View Permission</li></ol>

---

### POST /security/principal/users/{referenceId}/catalogueItemReference

**Summary:** Creates a catalogue item for a user.

**Description:** This API creates a new catalogue item for a user

Requires the caller be granted the 'Manage Console Security' or 'Lookup Users and Group Membership' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id for a user.

**Responses:**
- **200**: Successfully returns the specified catalogue reference id.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6511: Insufficient Edit Permission</li></ol>

---

### DELETE /security/principal/users/{referenceId}/catalogueItemReference

**Summary:** Deletes a catalogue item for a user.

**Description:** This API deletes a catalogue reference ID for a user

Requires the caller be granted the 'Manage Console Security' or 'Lookup Users and Group Membership' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id for a user.

**Responses:**
- **204**: Successfully deleted specified catalogue reference id.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6511: Insufficient Edit Permission</li></ol>

---
### GET /security/principal/users/{referenceId}/{scope}/rights

**Summary:** Returns the permissions allocated to the specified  given user.

**Description:** Returns the permissions allocated to the specified  given user.

Requires the caller be granted the 'Manage Console Security' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The reference identifier.
- `scope` (Required): Type: string. Description: The scope.

**Responses:**
- **200**: Successfully returns the specified user.
- **400**: Contract validation failed.
- **403**: Forbidden.

---

### PUT /security/principal/users/{referenceId}/{scope}/rights

**Summary:** Updates the general permissions for a user.

**Description:** This API updates the general permissions for a selected user specified by its Reference Id.

Requires the caller be granted the 'Manage Console Security' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id for a user.
- `scope` (Required): Type: string. Description: Authorization scope.
- `rights` (Required): Type: object. Description: Schema for permission and its boolean value.

**Responses:**
- **200**: Successfully returns a list of right summary.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6507: Invalid permission name.</li><li>6508: Duplicate permission name.</li><li>6509: Invalid parent child state.</li><li>6511: Insufficient Edit Permission.</li><li>6515: Security right not found.</li></ol>

---
### GET /security/principal/users/{referenceId}/deviceGroups/{deviceGroupReferenceId}/rights

**Summary:** Returns device group permissions for a user.

**Description:** This API retrieves all device group permission for a user

Requires the caller be granted the 'Manage Console Security' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id for a user.
- `deviceGroupReferenceId` (Required): Type: string. Description: Reference Id of a device group.

**Responses:**
- **200**: Successfully returns a list of right summary.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6512: Insufficient View Permission</li></ol>

---

### PUT /security/principal/users/{referenceId}/deviceGroups/{deviceGroupReferenceId}/rights

**Summary:** Updates the device group permission for a user.

**Description:** This API updates all device group permission rights belonging to a single user

Requires the caller be granted the 'Manage Console Security' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id for a user.
- `deviceGroupReferenceId` (Required): Type: string. Description: Reference Id for a device group.
- `rights` (Required): Type: object. Description: Schema for permission and its boolean value.

**Responses:**
- **200**: Successfully returns a list of right summary.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>6507: Invalid permission name</li><li>6508: Duplicate permission name</li><li>6509: Security right has invalid parent/child state</li><li>6511: Insufficient Edit Permission</li><li>6515: Security right not found</li></ol>

---
### GET /security/principal/users/{referenceId}/logs

**Summary:** Retrieves logs for a user.

**Description:** Retrieves the log activity for a particular user.

Requires the caller be granted the 'Manage Console Security' or 'Lookup Users and Group Membership' permissions.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Reference Id of a User.
- `startDate` (Required): Type: string. Description: Date to retrieve logs from. Please specify the time if start and end dates are the same.
- `endDate` (Required): Type: string. Description: Date to retrieve logs to. Please specify the time if start and end dates are the same.
- `logSeverities`: Type: array. Description: One or more categories of log severities.
- `orderByDesc`: Type: boolean. Description: Order logs by timestamp, true for descending, false for ascending.
- `skip`: Type: integer. Description: Input the first X (count) entries that should not be returned.
- `take`: Type: integer. Description: Input the number of entries to be returned, after skipping over the 'skip' count.

**Responses:**
- **200**: Successfully returns a list of user log entry.
- **400**: Contract validation failed.
- **403**: Forbidden.
- **422**: Violated logical condition.

---
### GET /security/principal/users/logs

**Summary:** Returns the logs for MC users.

**Description:** This API retrieves logs for users of MC, based on the request parameters.

Requires the caller be granted the 'Manage Console Security' or ' Lookup Users and Group Membership' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `startDate` (Required): Type: string. Description: The date starting which the logs will be fetched.
- `endDate` (Required): Type: string. Description: The date till which the logs will be fetched.
- `logSeverities`: Type: array. Description: Select the type of log.
- `userLogFilter`: Type: string. Description: Define the log filter for all or deleted users.  If left blank data is returned for all users.
- `orderByDesc`: Type: boolean. Description: Defines the sorting order. Pass the value as true for descending, false for ascending.
- `skip`: Type: integer. Description: Input the first X (count) entries that should not be returned.
- `take`: Type: integer. Description: Input the number of entries to be returned, after skipping over the 'skip' count.

**Responses:**
- **200**: Successfully returns a list of user log entry.
- **400**: Contract validation failed.
- **403**: Forbidden.

---
### GET /security/principal/users/{referenceId}/logs/actions/download

**Summary:** Returns the CSV file of logs for a user.

**Description:** This API exports a CSV file of logs for a user specified by its Reference Id.

Requires the caller be granted the 'Manage Console Security' or 'Lookup Users and Group Membership' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: The unique Identifier for the user.
- `reportHeaderFields` (Required): Type: string. Description: Comma separated field names to be included in the csv file.
- `logSeverities`: Type: array. Description: List of log severities to include into result such as Information, Warning or Error.
- `startDate` (Required): Type: string. Description: The date starting which the logs will be fetched (UTC format).
- `endDate` (Required): Type: string. Description: The date till which the logs will be fetched (UTC format).
- `format`: Type: string. Description: File format [Currently only csv is supported.].
- `timeZoneOffset`: Type: integer. Description: Time zone offset from UTC (in Minutes).
- `orderByDesc`: Type: boolean. Description: Defines the sorting order by timestamp. Pass the value as true for descending, false for ascending.
- `Skip`: Type: integer.
- `Take`: Type: integer.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.

---
### GET /security/principal/users/logs/actions/download

**Summary:** Returns the CSV file of logs for all user.

**Description:** This API exports a CSV file of logs for all active and deleted users of MobiControl.

Requires the caller be granted the 'Manage Console Security' or 'Lookup Users and Group Membership' permission.

**(Available since MobiControl v15.4.0)**

**Parameters:**
- `reportHeaderFields` (Required): Type: string. Description: Comma separated field names to be included in the csv file.
- `logSeverities`: Type: array. Description: List of log severities to include into result such as Information, Warning or Error.
- `startDate` (Required): Type: string. Description: The date starting which the logs will be fetched (UTC format).
- `endDate` (Required): Type: string. Description: The date till which the logs will be fetched (UTC format).
- `userLogFilter`: Type: string. Description: Define the log filter for all or deleted users. If left blank data is returned for all users.
- `format`: Type: string. Description: File format [Currently only csv is supported.].
- `timeZoneOffset`: Type: integer. Description: Time zone offset from UTC (in Minutes).
- `orderByDesc`: Type: boolean. Description: Defines the sorting order by timestamp. Pass the value as true for descending, false for ascending.
- `Skip`: Type: integer.
- `Take`: Type: integer.

**Responses:**
- **200**: Success.
- **400**: Contract validation failed.
- **403**: Forbidden.

---
### GET /security/principal/users/currentUser

**Summary:** Returns the details of the current user.

**Description:** This API retrieves the details of the user currently logged-in

Requires the caller be granted the "Web Console Access" permission.

**(Available since MobiControl v15.4.0)**

**Responses:**
- **200**: Successfully returns the details of the current user.
- **403**: Forbidden.

---
## Webhook Credentials

### POST /webhookCredentials/basic

**Summary:** Creates a new Basic Webhook Credential in MobiControl.

**Description:** Returns Webhook Credential Details with Reference Id.

Requires the caller be granted the "Manage Webhooks" permission.

**(Available since MobiControl v2024.0.0)**

**Parameters:**
- `basicCredential` (Required): Type: object. Description: Webhook Credential Details.

**Responses:**
- **200**: {Soti.MobiControl.Webhooks.Web.Contracts.Authentication.BasicCredentialSummary}Successfully returns newly created Webhook Credential details.
- **400**: Bad Request.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>10001: Webhook Credential name already exists.</li></ol>
- **500**: Internal Server Error.

---
### POST /webhookCredentials/apiKey

**Summary:** Creates a new ApiKey Webhook Credential in MobiControl.

**Description:** Returns Webhook Credential Details with Reference Id.

Requires the caller be granted the "Manage Webhooks" permission.

**(Available since MobiControl v2024.0.0)**

**Parameters:**
- `apiKeyCredential` (Required): Type: object. Description: Webhook Credential Details.

**Responses:**
- **200**: {Soti.MobiControl.Webhooks.Web.Contracts.Authentication.ApiKeyCredentialSummary}Successfully returns newly created Webhook Credential details.
- **400**: Bad Request.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>10001: Webhook Credential name already exists.</li></ol>
- **500**: Internal Server Error.

---
### POST /webhookCredentials/none

**Summary:** Creates a new None Webhook Credential in MobiControl.

**Description:** Returns Webhook Credential Details with Reference Id.

Requires the caller be granted the "Manage Webhooks" permission.

**(Available since MobiControl v2024.0.0)**

**Parameters:**
- `noneCredential` (Required): Type: object. Description: Webhook Credential Details.

**Responses:**
- **200**: {Soti.MobiControl.Webhooks.Web.Contracts.Authentication.NoneCredentialSummary}Successfully returns newly created Webhook Credential details.
- **400**: Bad Request.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>10001: Webhook Credential name already exists.</li></ol>
- **500**: Internal Server Error.

---
### GET /webhookCredentials/{referenceId}

**Summary:** Gets Webhook Credential Details in MobiControl based on the Reference Id.

**Description:** Webhook Credential Details based on Reference Id parameter.

Requires the caller be granted the "Manage Webhooks" permission.

**(Available since MobiControl v2024.0.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Webhook Credential Reference Id.

**Responses:**
- **200**: {Soti.MobiControl.Webhooks.Web.Contracts.Authentication.WebhookCredentialSummary}Successfully returns a Webhook Credential Details.
- **400**: Bad Request.
- **403**: Forbidden or no data found.
- **500**: Internal Server Error.

---

### DELETE /webhookCredentials/{referenceId}

**Summary:** Deletes Webhook Credential in MobiControl based on the Reference Id.

**Description:**
Requires the caller be granted the "Manage Webhooks" permission.

**(Available since MobiControl v2024.0.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Webhook Credential Reference Id.

**Responses:**
- **204**: Successfully deleted Webhook Credential.
- **400**: Bad Request.
- **403**: Forbidden or no data found.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>10004: Cannot delete Webhook Credential since it is being used by active Webhooks.</li></ol>
- **500**: Internal Server Error.

---
### PUT /webhookCredentials/basic/{referenceId}

**Summary:** Update Webhook Credential Details in MobiControl based on the Reference Id.

**Description:** Returns Webhook Credential Details with Reference Id.

Requires the caller be granted the "Manage Webhooks" permission.

**(Available since MobiControl v2024.0.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: External ReferenceId to identify the WebhookCredential.
- `basicCredential` (Required): Type: object. Description: Webhook Credential Details.

**Responses:**
- **200**: {Soti.MobiControl.Webhooks.Web.Contracts.Authentication.BasicCredentialSummary}Successfully returns newly created Webhook Credential details.
- **400**: Bad Request.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>10001: Webhook Credential name already exists.</li><li>10003: Webhook Credential not found.</li></ol>
- **500**: Internal Server Error.

---
### PUT /webhookCredentials/apiKey/{referenceId}

**Summary:** Update Webhook Credential Details in MobiControl based on the Reference Id.

**Description:** Returns Webhook Credential Details with Reference Id.

Requires the caller be granted the "Manage Webhooks" permission.

**(Available since MobiControl v2024.0.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: External ReferenceId to identify the WebhookCredential.
- `apiKeyCredential` (Required): Type: object. Description: Webhook Credential Details.

**Responses:**
- **200**: {Soti.MobiControl.Webhooks.Web.Contracts.Authentication.ApiKeyCredentialSummary}Successfully returns newly created Webhook Credential details.
- **400**: Bad Request.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>10001: Webhook Credential name already exists.</li><li>10003: Webhook Credential not found.</li></ol>
- **500**: Internal Server Error.

---
### PUT /webhookCredentials/none/{referenceId}

**Summary:** Update Webhook Credential Details in MobiControl based on the Reference Id.

**Description:** Returns Webhook Credential Details with Reference Id.

Requires the caller be granted the "Manage Webhooks" permission.

**(Available since MobiControl v2024.0.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: External ReferenceId to identify the WebhookCredential.
- `noneCredential` (Required): Type: object. Description: Webhook Credential Details.

**Responses:**
- **200**: {Soti.MobiControl.Webhooks.Web.Contracts.Authentication.NoneCredentialSummary}Successfully returns newly created Webhook Credential details.
- **400**: Bad Request.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>10001: Webhook Credential name already exists.</li><li>10003: Webhook Credential not found.</li></ol>
- **500**: Internal Server Error.

---
## Webhooks

### POST /webhooks

**Summary:** Creates a new Webhook in MobiControl.

**Description:** Returns Webhook Details with Reference Id.

Requires the caller be granted the "Manage Webhooks" permission.

**(Available since MobiControl v2024.0.0)**

**Parameters:**
- `webhook` (Required): Type: object. Description: Webhook Details.

**Responses:**
- **200**: {Soti.MobiControl.Webhooks.Web.Contracts.WebhookSummary}Successfully returns newly created Webhook details.
- **400**: Bad Request.
- **403**: Forbidden.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>10000: Webhook name already exists.</li></ol>
- **500**: Internal Server Error.

---

### GET /webhooks

**Summary:** Gets all the Webhooks in MobiControl.

**Description:** Returns all Webhooks Details in the MobiControl.

Requires the caller be granted the "Manage Webhooks" permission.

**(Available since MobiControl v2024.0.0)**

**Responses:**
- **200**: {System.Collections.Generic.List`1}where T is {Soti.MobiControl.Webhooks.Web.Contracts.WebhookSummary}Successfully returns a list of all Webhooks.
- **403**: Forbidden.
- **500**: Internal Server Error.

---
### GET /webhooks/{referenceId}

**Summary:** Gets Webhook Details in MobiControl based on the Reference Id.

**Description:** Webhook Details based on Reference Id parameter.

Requires the caller be granted the "Manage Webhooks" permission.

**(Available since MobiControl v2024.0.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Webhook Reference Id.

**Responses:**
- **200**: {Soti.MobiControl.Webhooks.Web.Contracts.WebhookSummary}Successfully returns a Webhook Details.
- **400**: Bad Request.
- **403**: Forbidden or no data found.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>10005: Cannot process request on deleted webhook.</li></ol>
- **500**: Internal Server Error.

---

### DELETE /webhooks/{referenceId}

**Summary:** Deletes Webhook in MobiControl based on the Reference Id.

**Description:**
Requires the caller be granted the "Manage Webhooks" permission.

**(Available since MobiControl v2024.0.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Webhook Reference Id.

**Responses:**
- **204**: Successfully deleted the Webhook.
- **400**: Bad Request.
- **403**: Forbidden or no data found.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>10005: Cannot process request on deleted webhook.</li></ol>
- **500**: Internal Server Error.

---

### PUT /webhooks/{referenceId}

**Summary:** Update Webhook Details in MobiControl based on the Reference Id.

**Description:** Updated Webhook Details based on Reference Id parameter.

Requires the caller be granted the "Manage Webhooks" permission.

**(Available since MobiControl v2024.0.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Webhook Reference Id.
- `updatedWebhook` (Required): Type: object. Description: Updated webhook info.

**Responses:**
- **200**: {Soti.MobiControl.Webhooks.Web.Contracts.WebhookSummary}Successfully returns a Webhook Details.
- **400**: Bad Request.
- **403**: Forbidden or no data found.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>10000: Webhook name already exists.</li><li>10002: Webhook not found.</li><li>10005: Cannot process request on deleted webhook.</li></ol>
- **500**: Internal Server Error.

---
### PUT /webhooks/status/{referenceId}

**Summary:** Update Webhook Status in MobiControl based on the Reference Id.

**Description:**
Requires the caller be granted the "Manage Webhooks" permission.

**(Available since MobiControl v2024.0.0)**

**Parameters:**
- `referenceId` (Required): Type: string. Description: Webhook Reference Id.
- `status` (Required): Type: object. Description: Updated webhook info.

**Responses:**
- **200**: Status update success or failure.
- **400**: Bad Request.
- **403**: Forbidden or no data found.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned.<br /><ol><li>10007: Cannot process request on deleted webhook.</li></ol>
- **500**: Internal Server Error.

---
### POST /webhooks/test

**Summary:** Test a Webhook in MobiControl.

**Description:** True if successful, else False.

Requires the caller be granted the "Manage Webhooks" permission.

**(Available since MobiControl v2024.0.0)**

**Parameters:**
- `webhook` (Required): Type: object. Description: Webhook Details.

**Responses:**
- **200**: True if successful else False.
- **400**: Bad Request.
- **403**: Forbidden.
- **500**: Internal Server Error.

---
## Windows Bit Locker Keys

### POST /windows/devices/{deviceId}/actions/fetchBitLockerKeys

**Summary:** Returns the BitLocker keys information for a device.

**Description:** This API returns the BitLocker keys information for a device.



         Requires the caller be granted the "View Decrypted Personal Recovery Key" permission.

**(Available Since MobiControl v2024.0.0)**


**Parameters:**
- `deviceId` (Required): Type: string. Description: The device identifier.

**Responses:**
- **200**: Success.
- **400**: Contract Validation Failed.
- **401**: Unauthorized.
- **403**: Forbidden.

---
## Windows Modern Enrollment Policies

### GET /enrollmentPolicies/windowsModern/{referenceId}

**Parameters:**
- `referenceId` (Required): Type: string.

**Responses:**
- **200**:

---

### DELETE /enrollmentPolicies/windowsModern/{referenceId}

**Parameters:**
- `referenceId` (Required): Type: string.

**Responses:**
- **204**:

---

### PUT /enrollmentPolicies/windowsModern/{referenceId}

**Parameters:**
- `referenceId` (Required): Type: string.
- `request` (Required): Type: object.

**Responses:**
- **200**:

---
### POST /enrollmentPolicies/windowsModern

**Parameters:**
- `request` (Required): Type: object.

**Responses:**
- **200**:

---
### GET /enrollmentPolicies/windowsModern/{referenceId}/actions/downloadPackage

**Parameters:**
- `referenceId` (Required): Type: string.
- `includeCertificateChain` (Required): Type: boolean.

**Responses:**
- **200**:

---
## Windows Updates

### GET /windowsUpdates/device/{deviceId}

**Summary:** Returns a summary list of Windows Updates for the specified device

**Description:** Return a summary list of Windows Updates and their status for the specified device. Requires the caller be granted "View Windows Updates" permission.

**(Available Since MobiControl v15.5.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: Device Id

**Responses:**
- **200**: Successfully retrieved all Windows Updates and their statuses from a given device
- **400**: Bad request to approve:<br /><ol><li>Device id must be specified</li></ol>
- **403**: User is not authorized or reference does not exist

---
### GET /windowsUpdates/classifications

**Summary:** Gets Windows Updates Classifications

**Description:** Retrieves the list of Windows Updates classifications from MobiControl which is refreshed at a configurable interval. In case the classifications have not been synced during the configured interval, then Microsoft server is reached.

**(Available Since MobiControl v15.5.0)**

**Responses:**
- **200**: Successfully retrieved the list of Windows Updates classifications

---
### POST /windowsUpdates/device/{deviceId}/approve

**Summary:** Approve Windows Updates for the specified device

**Description:** Send request to the specified device to approve the specified Windows Updates.Requires the caller be granted "Manage Windows Updates" permission.

**(Available Since MobiControl v15.5.0)**

**Parameters:**
- `deviceId` (Required): Type: string. Description: Device Id
- `approveUpdateRequest` (Required): Type: object. Description: A list of Windows Update ids to approve

**Responses:**
- **204**: Successfully requested to approve a list of Windows Updates
- **400**: Bad request to approve:<br /><ol><li>Device id must be specified</li><li>Updates must be specified</li><li>Invalid approver</li></ol>
- **403**: User is not authorized or reference does not exist
- **422**: Violated logical condition. The following ErrorCode values can be returned:<br /><ol><li>7200 - Windows Update is invalid</li><li>7201 - There are no available Windows Updates on the device</li><li>7202 - Windows Update is not found</li><li>7203 - Windows Update is not installable</li></ol>

---
## Wns Configuration

### PUT /windows/wns

**Summary:** Saves the Windows Notification Service (WNS) configuration

**Description:** Configures Windows Notification Services (WNS), which enables MobiControl to send push notifications to Windows devices on demand.

**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `wnsConfiguration` (Required): Type: object.

**Responses:**
- **401**: Unauthorized attempt to execute the method
- **403**: User is not authorized to perform the operation.
- **422**: Violated logical condition.<br />The following ErrorCode values can be returned:<br /><ol><li>5700 - Failed to update the Windows Notification Service configuration due to an unknown error.</li><li>5701 - Failed to update the Windows Notification Service configuration because the service failed to obtain a token.</li><li>5704 - Failed to update the Windows Notification Service configuration because the Client secret for WNS configuration is invalid.</li></ol>

---

### GET /windows/wns

**Summary:** Gets the Windows Notification Service (WNS) configuration.

**Description:** Retrieves the configured Windows Notification Services (WNS) details.

**(Available Since MobiControl v15.3.0)**

**Responses:**
- **200**: Success.
- **401**: Unauthorized attempt to execute the method.
- **403**: User is not authorized to perform the operation.

---
## Zebra Android Firmware Upgrade Client Summary

### GET /androidFirmwareUpgrade/clients/{clientType}/summary

**Summary:** Retrieve Android firmware upgrade client summary.

**Description:** Retrieve the count of target devices, enrolled devices and FOTA Ready devices.

Requires the caller to be granted Web Console Access permission.

**(Available Since MobiControl v15.3.0)**

**Parameters:**
- `clientType` (Required): Type: string. Description: Android Firmware Upgrade ClientType.

**Responses:**
- **200**: Returns Zebra Android firmware upgrade client summary.
- **401**: Unauthorized access.

---
````
