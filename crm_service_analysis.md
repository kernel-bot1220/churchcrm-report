# ChurchCRM Service Layer Analysis
## Static Analysis of Service Classes

---

## PersonService.php

**Public Methods** (8):

- `search()`
- `getPeopleEmailsAndGroups()`
- `addVolunteerOpportunity()`
- `removeVolunteerOpportunity()`
- `getFamilyList()`
- `getMissingGenderDataCount()`
- `getMissingRoleDataCount()`
- `getMissingClassificationDataCount()`

**Table Operations**:

- READ from: `a`

**Uses Models**:

- Family
- Person
- List
- Group

---

## FamilyService.php

**Public Methods** (3):

- `__construct()`
- `getMissingCoordinatesCount()`
- `autoGeocodeFamily()`

**Table Operations**:

- UPDATE: `family`

**Calls Other Services**:

- `logger`

**Uses Models**:

- Family

---

## GroupService.php

**Public Methods** (11):

- `removeUserFromGroup()`
- `addUserToGroup()`
- `addUserToGroupInternal()`
- `getGroupRoles()`
- `setGroupRoleOrder()`
- `getGroupRoleOrder()`
- `deleteGroupRole()`
- `addGroupRole()`
- `enableGroupSpecificProperties()`
- `disableGroupSpecificProperties()`
- `getGroupMembers()`

**Table Operations**:

- READ from: `person_custom_master, group_grp, the, Group, list_lst, which, groupprop_master, person2group2role_p2g2r, groupprop_`
- INSERT to: `the, groupprop_`
- UPDATE: `person_custom, group_grp, the, list_lst, person2group2role_p2g2r, groupprop_`

**Uses Models**:

- Group
- Person
- List
- User

---

## FinancialService.php

**Public Methods** (30):

- `deletePayment()`
- `getPayments()`
- `getMemberByScanString()`
- `setDeposit()`
- `getDepositTotal()`
- `getPaymentViewURI()`
- `getViewURI()`
- `locateFamilyCheck()`
- `validateChecks()`
- `processCurrencyDenominations()`
- `insertPledgeorPayment()`
- `submitPledgeOrPayment()`
- `getPledgeorPayment()`
- `getDepositPDF()`
- `getDepositCSV()`
- `getCurrencyTypeOnDeposit()`
- `getCurrency()`
- `getAdvancedDepositReportData()`
- `getTaxReportData()`
- `getZeroGiversReportData()`
- `getFiscalYearDates()`
- `getDepositStatistics()`
- `getRecentDeposits()`
- `getYtdPaymentTotal()`
- `getYtdPledgeTotal()`
- `getYtdPaymentCount()`
- `getYtdDonorFamilyCount()`
- `getCurrentDeposit()`
- `getCurrentDepositId()`
- `getDashboardData()`

**Table Operations**:

- READ from: `family_fam, currency_denominations_cdem, current, pledge_denominations_pdem, session, pledge_plg`
- INSERT to: `pledge_denominations_pdem`

**Uses Models**:

- Family
- Person
- Pledge
- Group
- Deposit
- User

---

## DepositService.php

**Public Methods** (8):

- `getPayments()`
- `setDeposit()`
- `getDepositTotal()`
- `getDepositPDF()`
- `getDepositCSV()`
- `getViewURI()`
- `getDepositItemsByType()`
- `createDeposit()`

**Table Operations**:

- READ from: `pledge_plg, a`

**Uses Models**:

- Family
- Pledge
- Group
- Deposit
- User

---

