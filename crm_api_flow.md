# ChurchCRM OpenAPI Data Flow Analysis
## API Endpoints and Data Models

---

## Private API Endpoints

**Total**: 184

| Method | Path | Summary | Tags | Request Body | Response |
|--------|------|---------|------|--------------|----------|

| GET | /api/database/people/export/chmeetings | Export all people as a ChMeetings-compatible CSV file (Admin role required) | Admin | - | 200 |
| DELETE | /api/database/reset | Drop all database tables and views, clear uploaded images, and destroy the session (Admin role required) | Admin | - | 200, 403, 500 |
| POST | /api/demo/load | Import demo data into the application (Admin role required) | Admin | object | 200, 403, 500 |
| GET | /admin/api/import/csv/families | Download a CSV import template for families (Admin role required) | Import | - | 200, 401, 403 |
| POST | /admin/api/import/csv/upload | Upload a CSV file and return headers with auto-detected field mappings | Import | object | 200, 400, 401, 403 |
| POST | /admin/api/import/csv/execute | Execute a CSV import using a previously uploaded file and column mapping | Import | - | 200, 400, 401, 403 |
| GET | /api/orphaned-files | List orphaned files | Admin | - | 200, 401, 403 |
| POST | /api/orphaned-files/delete-all | Delete all orphaned files | Admin | - | 200, 401, 403, 500 |
| GET | /api/upgrade/download-latest-release | Download the latest release from GitHub | Admin | - | 200, 400, 401, 403 |
| POST | /api/upgrade/do-upgrade | Apply the system upgrade | Admin | object | 200, 401, 403, 500 |
| POST | /api/upgrade/refresh-upgrade-info | Refresh upgrade information from GitHub | Admin | - | 200, 401, 403, 500 |
| POST | /api/user/{userId}/password/reset | Reset a user's password to a random value and email it to them (Admin role required) | Admin | - | 200, 403 |
| POST | /api/user/{userId}/disableTwoFactor | Disable two-factor authentication for a user (Admin role required) | Admin | - | 200, 403 |
| POST | /api/user/{userId}/login/reset | Reset failed login counter and send unlock email (Admin role required) | Admin | - | 200, 403 |
| DELETE | /api/user/{userId}/ | Delete a user account (Admin role required) | Admin | - | 200, 403 |
| GET | /api/user/{userId}/permissions | Get permission flags for a user (Admin role required) | Admin | - | 200, 403 |
| POST | /background/timerjobs | Trigger background timer jobs (scheduled task runner) | System | - | 200 |
| GET | /systemcalendars | List all system calendars | Calendar | - | 200, 401 |
| GET | /systemcalendars/{id}/events | Get events from a system calendar | Calendar | - | 200, 401, 404 |
| GET | /systemcalendars/{id}/events/{eventid} | Get a single event from a system calendar | Calendar | - | 200, 401, 404 |
| GET | /systemcalendars/{id}/fullcalendar | Get system calendar events in FullCalendar format | Calendar | - | 200, 401, 404 |
| GET | /calendars | List user-created calendars | Calendar | - | 200, 401, 404 |
| POST | /calendars | Create a new calendar | Calendar | object | 200, 401, 403 |
| GET | /calendars/{id} | Get a specific user calendar | Calendar | - | 200, 401, 404 |
| DELETE | /calendars/{id} | Delete a user calendar | Calendar | - | 200, 400, 401 |
| GET | /calendars/{id}/fullcalendar | Get user calendar events in FullCalendar format | Calendar | - | 200, 401, 404 |
| GET | /calendars/{id}/events | Get events for a user calendar | Calendar | - | 200, 401, 404 |
| POST | /calendars/{id}/NewAccessToken | Generate a new public access token for a calendar | Calendar | - | 200, 400, 401, 403 |
| DELETE | /calendars/{id}/AccessToken | Remove the public access token from a calendar | Calendar | - | 200, 400, 401, 403 |
| GET | /calendar/events-counters | Get today's event counters for the dashboard menu badges | Calendar | - | 200, 401 |
| GET | /events | List all events | Calendar | - | 200, 401, 404 |
| POST | /events | Create a new event | Calendar | object | 200, 400, 401, 403 |
| GET | /events/types | List all event types | Calendar | - | 200, 401, 404 |
| GET | /events/{id} | Get an event by ID | Calendar | - | 200, 401, 404 |
| POST | /events/{id} | Update an existing event | Calendar | object | 200, 401, 403, 404 |
| DELETE | /events/{id} | Delete an event | Calendar | - | 200, 401, 403, 404 |
| GET | /events/{id}/primarycontact | Get an event's primary contact person | Calendar | - | 200, 401, 404 |
| GET | /events/{id}/secondarycontact | Get an event's secondary contact person | Calendar | - | 200, 401, 404 |
| GET | /events/{id}/location | Get an event's location | Calendar | - | 200, 401, 404 |
| GET | /events/{id}/audience | Get an event's audience (linked groups) | Calendar | - | 200, 401, 404 |
| POST | /events/{id}/time | Update an event's start and end times | Calendar | object | 200, 401, 403, 404 |
| GET | /cart/ | Get the current session people cart contents | Cart | - | 200 |
| POST | /cart/ | Add persons, a family, or a group to the session cart | Cart | object | 200, 400 |
| DELETE | /cart/ | Remove persons or a family from the cart, or empty the entire cart | Cart | object | 200, 400 |
| POST | /cart/emptyToGroup | Move all persons in the cart into a group with a specified role | Cart | object | 200, 400 |
| POST | /cart/removeGroup | Remove all members of a group from the session cart | Cart | object | 200, 400 |
| GET | /deposits | Get all deposits (Finance role required) | Finance | - | 200, 401, 403 |
| POST | /deposits | Create a new deposit (Finance role required) | Finance | object | 200, 400, 401, 403 |
| GET | /deposits/dashboard | Get deposits from the last 90 days (Finance role required) | Finance | - | 200, 401, 403 |
| GET | /deposits/{id} | Get a single deposit by ID (Finance role required) | Finance | - | 200, 401, 403 |
| POST | /deposits/{id} | Update an existing deposit (Finance role required) | Finance | object | 200, 401, 403 |
| DELETE | /deposits/{id} | Delete a deposit (Finance role required) | Finance | - | 200, 401, 403 |
| GET | /deposits/{id}/ofx | Get OFX export data for a deposit (Finance role required) | Finance | - | 200, 404, 401, 403 |
| GET | /deposits/{id}/pdf | Generate and stream a PDF report for a deposit (Finance role required) | Finance | - | 200, 404, 401, 403 |
| GET | /deposits/{id}/csv | Download a CSV export of payments for a deposit (Finance role required) | Finance | - | 200, 401, 403 |
| GET | /deposits/{id}/pledges | Get pledge items for a deposit (Finance role required) | Finance | - | 200, 401, 403 |
| GET | /deposits/{id}/payments | Get payment items for a deposit (Finance role required) | Finance | - | 200, 401, 403 |
| GET | /payments/ | Get all payments (Finance role required) | Finance | - | 200, 401, 403 |
| POST | /payments/ | Submit a new pledge or payment (Finance role required) | Finance | object | 200, 401, 403 |
| GET | /payments/family/{familyId}/list | Get pledge and payment history for a family (Finance role required) | Finance | - | 200, 401, 403 |
| DELETE | /payments/{groupKey} | Delete a payment by group key (Finance role required) | Finance | - | 200, 401, 403 |
| POST | /geocoder/address | Geocode an address — returns latitude and longitude | Map | object | 200, 400 |
| GET | /map/families | Get geocoded map items — families, group members, or cart persons | Map | - | 200 |
| GET | /map/neighbors/{familyId} | Get nearest neighbor families for a given familyId | Map | - | 200 |
| GET | /groups/properties | Get all available group property definitions | Groups, Properties | - | 200, 403 |
| GET | /groups/{groupID}/properties | Get properties assigned to a specific group | Groups, Properties | - | 200, 403, 404 |
| POST | /groups/{groupID}/properties/{propertyId} | Assign or update a property on a group (ManageGroup role required) | Groups, Properties | object | 200, 403, 404 |
| DELETE | /groups/{groupID}/properties/{propertyId} | Remove a property from a group (ManageGroup role required) | Groups, Properties | - | 200, 404, 403 |
| GET | /person/{personId}/notes | List user-type notes for a person | People | - | 200, 401, 403, 404 |
| POST | /person/{personId}/note | Create a note for a person | People | object | 201, 400, 401, 403, 404 |
| GET | /family/{familyId}/notes | List user-type notes for a family | Families | - | 200, 401, 403, 404 |
| POST | /family/{familyId}/note | Create a note for a family | Families | object | 201, 400, 401, 403, 404 |
| GET | /note/{noteId} | Get a single note by ID | People | - | 200, 401, 403, 404 |
| PUT | /note/{noteId} | Update a note's text and/or privacy | People | object | 200, 400, 401, 403, 404 |
| DELETE | /note/{noteId} | Delete a note | People | - | 200, 401, 403, 404 |
| GET | /families/familiesInCart | Get families whose all members are in the session cart | Families | - | 200 |
| GET | /families/email/without | Get families with no email address on record | Families | - | 200 |
| GET | /families/search/{query} | Search families by name (max 15 results) | Families | - | 200 |
| GET | /families/self-register | Get the last 100 self-registered families | Families | - | 200 |
| GET | /families/self-verify | Get the last 100 families with self-verification notes | Families | - | 200 |
| GET | /families/pending-self-verify | Get families with pending (unused, non-expired) self-verify tokens | Families | - | 200 |
| GET | /families/byCheckNumber/{scanString} | Find a family by check scan string | Families | - | 200 |
| GET | /families/anniversaries | Get families with wedding anniversaries within 7 days of today | Families | - | 200 |
| GET | /families/latest | Get the 10 most recently added families | Families | - | 200 |
| GET | /families/updated | Get the 10 most recently updated families | Families | - | 200 |
| GET | /family/{familyId}/photo | Get uploaded photo for a family (binary image) | Families | - | 200, 404 |
| POST | /family/{familyId}/photo | Upload a family photo from base64 data (EditRecords role required) | Families | object | 200, 400, 403 |
| DELETE | /family/{familyId}/photo | Delete a family's uploaded photo (EditRecords role required) | Families | - | 200, 403 |
| GET | /family/{familyId}/avatar | Get avatar info JSON for a family (for client-side rendering) | Families | - | 200 |
| GET | /family/{familyId} | Get a family object by ID | Families | - | 200, 404 |
| GET | /family/{familyId}/geolocation | Get geolocation and driving distance from church for a family | Families | - | 200 |
| GET | /family/{familyId}/nav | Get previous and next family IDs for navigation | Families | - | 200 |
| POST | /family/{familyId}/verify | Send a verification email to the family | Families | - | 200, 500 |
| GET | /family/{familyId}/verify/url | Generate a new family self-verify URL token | Families | - | 200 |
| POST | /family/{familyId}/verify/now | Mark a family as verified immediately | Families | - | 200 |
| POST | /family/{familyId}/activate/{status} | Activate or deactivate a family | Families | - | 200, 400 |
| POST | /family/{familyId}/geocode | Refresh geocoding (latitude/longitude) for a family's address | Families | - | 200, 400 |
| GET | /groups/ | List all groups | Groups | - | 200 |
| POST | /groups/ | Create a new group (ManageGroupRole role required) | Groups | object | 200, 403 |
| GET | /groups/calendars | Get groups formatted for calendar display | Groups | - | 200 |
| GET | /groups/groupsInCart | Get IDs of groups whose all members are in the session cart | Groups | - | 200 |
| GET | /groups/{groupID} | Get a single group by ID | Groups | - | 200, 404 |
| POST | /groups/{groupID} | Update group name, type, and description (ManageGroupRole role required) | Groups | object | 200, 403 |
| DELETE | /groups/{groupID} | Delete a group (ManageGroupRole role required) | Groups | - | 200, 403 |
| GET | /groups/{groupID}/cartStatus | Check whether all members of a group are in the session cart | Groups | - | 200 |
| GET | /groups/{groupID}/members | Get members of a group with family address info | Groups | - | 200 |
| GET | /groups/{groupID}/events | Get group member-role memberships (events/roles per member) | Groups | - | 200 |
| GET | /groups/{groupID}/roles | Get the role options for a group | Groups | - | 200 |
| POST | /groups/{groupID}/roles | Add a new role to a group (ManageGroupRole role required) | Groups | object | 200, 403, 500 |
| GET | /groups/{groupID}/phones | Get cell phone numbers for group members (respects Do Not SMS) | Groups | - | 200 |
| GET | /groups/{groupID}/sundayschool/phones | Get cell phone numbers for a Sunday School class, segmented by role | Groups | - | 200 |
| GET | /groups/{groupID}/emails | Get email addresses for group members (respects Do Not Email) | Groups | - | 200 |
| GET | /groups/{groupID}/sundayschool/emails | Get email addresses for a Sunday School class, segmented by role | Groups | - | 200 |
| GET | /groups/sundayschool/export/email | Export people emails with group memberships as CSV | Groups | - | 200, 403 |
| GET | /groups/sundayschool/export/classlist | Export Sunday School class roster as CSV | Groups | - | 200, 403 |
| DELETE | /groups/{groupID}/removeperson/{userID} | Remove a person from a group (ManageGroupRole role required) | Groups | - | 200, 403 |
| POST | /groups/{groupID}/addperson/{userID} | Add a person to a group (ManageGroupRole role required) | Groups | object | 200, 403 |
| POST | /groups/{groupID}/userRole/{userID} | Update a group member's role (ManageGroupRole role required) | Groups | object | 200, 403 |
| POST | /groups/{groupID}/roles/{roleID} | Update a group role name or sort order (ManageGroupRole role required) | Groups | object | 200, 403, 500 |
| DELETE | /groups/{groupID}/roles/{roleID} | Delete a group role (ManageGroupRole role required) | Groups | - | 200, 403, 500 |
| POST | /groups/{groupID}/defaultRole | Set the default role for a group (ManageGroupRole role required) | Groups | object | 200, 403 |
| POST | /groups/{groupID}/setGroupSpecificPropertyStatus | Enable or disable group-specific properties (ManageGroupRole role required) | Groups | object | 200, 403, 500 |
| POST | /groups/{groupID}/settings/active/{value} | Set a group's active status (ManageGroupRole role required) | Groups | - | 200, 403 |
| POST | /groups/{groupID}/settings/email/export/{value} | Set the email export flag for a group (ManageGroupRole role required) | Groups | - | 200, 403 |
| GET | /person/{personId}/photo | Get a person's uploaded photo | People | - | 200, 401, 404 |
| POST | /person/{personId}/photo | Upload a person's photo (base64 encoded) | People | object | 200, 400, 401, 403, 404 |
| DELETE | /person/{personId}/photo | Delete a person's uploaded photo | People | - | 200, 401, 403 |
| GET | /person/{personId}/avatar | Get a person's avatar info (initials, gravatar) | People | - | 200, 401 |
| GET | /person/{personId} | Get a person's full record by ID | People | - | 200, 401, 404 |
| DELETE | /person/{personId} | Delete a person record | People | - | 200, 401, 403, 404 |
| POST | /person/{personId}/addToCart | Add a person to the cart | People | - | 200, 401, 404 |
| POST | /person/{personId}/role/{roleId} | Set a person's family role | People | - | 200, 401, 403, 404, 500 |
| GET | /persons/email/without | Get people with no personal or work email on record | People | - | 200 |
| GET | /persons/search/{query} | Search persons by name or email | People | - | 200, 401 |
| GET | /persons/self-register | List recently self-registered persons | People | - | 200, 401 |
| GET | /persons/roles | List all family roles | People | - | 200, 401 |
| GET | /persons/duplicate/emails | Find duplicate email addresses across persons and families | People | - | 200, 401 |
| GET | /persons/latest | List the 10 most recently added persons | People | - | 200, 401 |
| GET | /persons/updated | List the 10 most recently edited persons | People | - | 200, 401 |
| GET | /persons/birthday | List persons with birthdays in a ±7-day window around today | People | - | 200, 401 |
| GET | /people/properties/person | Get all available person property definitions | Properties | - | 200, 403 |
| POST | /people/properties/person/{personId}/{propertyId} | Add or update a property on a person (MenuOptions role required) | Properties | object | 200, 403 |
| DELETE | /people/properties/person/{personId}/{propertyId} | Remove a property from a person (MenuOptions role required) | Properties | - | 200, 404, 403 |
| GET | /people/properties/family | Get all available family property definitions | Properties | - | 200, 403 |
| GET | /people/properties/person/{personId} | Get properties assigned to a specific person | Properties | - | 200, 403 |
| GET | /people/properties/family/{familyId} | Get properties assigned to a specific family | Properties | - | 200, 403 |
| POST | /people/properties/family/{familyId}/{propertyId} | Add or update a property on a family (MenuOptions role required) | Properties | object | 200, 403 |
| DELETE | /people/properties/family/{familyId}/{propertyId} | Remove a property from a family (MenuOptions role required) | Properties | - | 200, 404, 403 |
| DELETE | /people/properties/definition/{propertyId} | Delete a property definition and all its assignments (MenuOptions role required) | Properties | - | 200, 404, 403 |
| GET | /search/{query} | Search persons, families, groups, deposits, payments, and calendar events | Search | - | 200 |
| GET | /system/custom-fields/person | Get custom person fields filtered by type ID (Admin role required) | System | - | 200, 403 |
| GET | /system/properties/person | Get person property definitions as id/value pairs for settings dropdowns (Admin role required) | System | - | 200, 403 |
| POST | /database/backup | Create a local database backup (Admin role required) | System | object | 200, 400, 403 |
| POST | /database/backupRemote | Trigger a remote (WebDAV) backup via the External Backup plugin (Admin role required) | System | object | 200, 400, 403, 500 |
| POST | /database/restore | Restore the database from a backup file (Admin role required) | System | - | 200, 500, 403 |
| GET | /database/download/{filename} | Download a backup file by name (Admin role required) | System | - | 200, 400, 403 |
| GET | /system/debug/urls | Get internal system URL paths for debugging (Admin role required) | System | - | 200, 401, 403 |
| POST | /issues | Generate a GitHub issue body pre-filled with system diagnostics | System | object | 200 |
| GET | /locale/database/terms | Get all translatable terms stored in the database (Admin role required) | System | - | 200, 401, 403 |
| GET | /system/notification | Get current UI notifications (update alerts, system messages) | System | - | 200 |
| POST | /user/current/refresh2fasecret | Begin 2FA enrollment — provision a new TOTP secret and return a QR code data URI | 2FA | - | 200 |
| POST | /user/current/refresh2farecoverycodes | Generate new 2FA recovery codes for the current user | 2FA | - | 200 |
| POST | /user/current/remove2fasecret | Remove the 2FA secret from the current user (disables 2FA) | 2FA | - | 200 |
| GET | /user/current/get2faqrcode | Get the current user's 2FA QR code as a PNG image | 2FA | - | 200 |
| POST | /user/current/test2FAEnrollmentCode | Validate a TOTP enrollment code to complete 2FA setup | 2FA | object | 200 |
| GET | /user/current/2fa-status | Get the 2FA enabled status for the current user | 2FA | - | 200 |
| GET | /user/{userId}/setting/{settingName} | Get a named setting value for a user | Users | - | 200 |
| POST | /user/{userId}/setting/{settingName} | Set a named setting value for a user | Users | object | 200 |
| POST | /user/{userId}/apikey/regen | Regenerate the API key for a user | Users | - | 200 |
| POST | /user/{userId}/config/{key} | Update a named config string for a user | Users | object | 200 |
| GET | /kiosk/api/devices | List all kiosk devices | Kiosk | - | 200, 401, 403 |
| POST | /kiosk/api/allowRegistration | Open a 30-second kiosk registration window | Kiosk | - | 200, 401, 403 |
| POST | /kiosk/api/devices/{kioskId}/reload | Reload a kiosk device | Kiosk | - | 200, 401, 403, 404 |
| POST | /kiosk/api/devices/{kioskId}/identify | Trigger identification signal on a kiosk device | Kiosk | - | 200, 401, 403, 404 |
| POST | /kiosk/api/devices/{kioskId}/accept | Accept a pending kiosk device | Kiosk | - | 200, 401, 403, 404 |
| POST | /kiosk/api/devices/{kioskId}/assignment | Set kiosk event assignment | Kiosk | object | 200, 400, 401, 403, 404 |
| DELETE | /kiosk/api/devices/{kioskId} | Delete a kiosk device | Kiosk | - | 200, 401, 403, 404, 500 |
| GET | /plugins/api/plugins | List all available plugins | Plugins | - | 200, 401, 403, 500 |
| GET | /plugins/api/plugins/{pluginId} | Get plugin details | Plugins | - | 200, 401, 403, 404 |
| POST | /plugins/api/plugins/{pluginId}/enable | Enable a plugin | Plugins | - | 200, 400, 401, 403, 500 |
| POST | /plugins/api/plugins/{pluginId}/disable | Disable a plugin | Plugins | - | 200, 400, 401, 403, 500 |
| POST | /plugins/api/plugins/{pluginId}/settings | Update plugin settings | Plugins | object | 200, 400, 401, 403, 404 |
| POST | /plugins/api/plugins/{pluginId}/test | Test plugin connection with provided settings | Plugins | object | 200, 400, 401, 403, 404 |
| POST | /plugins/api/plugins/{pluginId}/reset | Reset all settings for a plugin | Plugins | - | 200, 401, 403, 404 |

---

## Public API Endpoints

**Total**: 11

| Method | Path | Summary | Tags | Request Body | Response |
|--------|------|---------|------|--------------|----------|

| GET | /public/calendar/{CalendarAccessToken}/events | Get public calendar events as JSON | Calendar | - | 200, 404 |
| GET | /public/calendar/{CalendarAccessToken}/ics | Download public calendar as ICS file | Calendar | - | 200, 404 |
| GET | /public/calendar/{CalendarAccessToken}/fullcalendar | Get public calendar events in FullCalendar format | Calendar | - | 200, 404 |
| GET | /public/data/countries | List all countries | Lookups | - | 200 |
| GET | /public/data/countries/{countryCode}/states | List states/provinces for a country | Lookups | - | 200 |
| POST | /public/register/family | Register a new family | Registration | object | 200, 400, 401 |
| POST | /public/register/person | Register a new individual person | Registration | object | 200, 400 |
| POST | /public/user/login | Log in and retrieve an API key | Auth | object | 200, 401, 404 |
| POST | /public/user/password-reset | Request a password reset email | Auth | object | 200, 400 |
| GET | /public/echo | Health check / echo | Utility | - | 200 |
| POST | /public/csp-report | Log a Content Security Policy violation report | Utility | object | 204 |

---

## Schema Definitions

### Private API Schemas


### Public API Schemas


---

## Service Mapping

| API Tag | Related Service |
|---------|-----------------|
| Person | PersonService |
| Family | FamilyService |
| Group | GroupService |
| Financial | FinancialService, DepositService |
| Event | EventService |
| User | UserService |
| System | SystemService, AdminService |
