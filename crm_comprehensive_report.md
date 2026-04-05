# ChurchCRM 综合数据架构报告
## Comprehensive Data Architecture Report

---

## 执行摘要 (Executive Summary)

ChurchCRM 是一个基于 PHP/MySQL 的教堂管理信息系统。本报告基于代码库深度分析，涵盖：

- **数据库表总数**: 43 张
- **业务域**: 11 个
- **核心实体**: Person, Family, Group, Event, Financial (Pledge/Deposit)
- **API端点**: Private API + Public API (RESTful)
- **服务层**: 5 个核心 Service 类

### 数据库业务域分布

| 业务域 | 表数量 | 描述 |
|--------|--------|------|
| Person & Family | 8 | |
| System | 6 | |
| Events | 6 | |
| Groups & Volunteers | 5 | |
| Financial | 5 | |
| Queries | 3 | |
| Properties | 3 | |
| Location & Calendar | 3 | |
| Kiosk | 2 | |
| Menu | 1 | |
| Tokens | 1 | |


---

## 第一部分：完整数据字典 (43张表)

# ChurchCRM 数据字典
## 完整 Schema 分析报告

**Database**: ChurchCRM (MySQL)  
**Total Tables**: 43

---

## Person & Family

### family_custom
**PHP Class**: `FamilyCustom` | **Domain**: Person & Family

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| fam_ID | FamId | SMALLINT(9) | 0 | Yes | Yes |  |

**Foreign Keys**

- -> `family_fam` (fam_ID -> fam_ID)

---

### family_custom_master
**PHP Class**: `FamilyCustomMaster` | **Domain**: Person & Family

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| fam_custom_Order | Order | SMALLINT | 0 | Yes | No |  |
| fam_custom_Field | Field | VARCHAR(5) |  | Yes | Yes |  |
| fam_custom_Name | Name | VARCHAR(40) |  | Yes | No |  |
| fam_custom_Special | CustomSpecial | mediumint(8) unsigned(8) |  | No | No |  |
| fam_custom_FieldSec | FieldSecurity | TINYINT | 1 | Yes | No |  |
| type_ID | TypeId | TINYINT | 0 | Yes | No |  |

---

### family_fam
**PHP Class**: `Family` | **Domain**: Person & Family

**Description**: This contains the main family data, including family name, family addresses, and family phone numbers

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| fam_ID | Id | mediumint(9) unsigned(9) |  | Yes | Yes |  |
| fam_Name | Name | VARCHAR(50) |  | No | No |  |
| fam_Address1 | Address1 | VARCHAR(255) |  | No | No |  |
| fam_Address2 | Address2 | VARCHAR(255) |  | No | No |  |
| fam_City | City | VARCHAR(50) |  | No | No |  |
| fam_State | State | VARCHAR(50) |  | No | No |  |
| fam_Zip | Zip | VARCHAR(50) |  | No | No |  |
| fam_Country | Country | VARCHAR(50) |  | No | No |  |
| fam_HomePhone | HomePhone | VARCHAR(30) |  | No | No |  |
| fam_Email | Email | VARCHAR(100) |  | No | No |  |
| fam_WeddingDate | Weddingdate | DATE |  | No | No |  |
| fam_DateEntered | DateEntered | TIMESTAMP |  | Yes | No |  |
| fam_DateLastEdited | DateLastEdited | TIMESTAMP |  | No | No |  |
| fam_EnteredBy | EnteredBy | smallint(5)(5) | 0 | Yes | No |  |
| fam_EditedBy | EditedBy | smallint(5) unsigned(5) | 0 | No | No |  |
| fam_scanCheck | ScanCheck | LONGVARCHAR |  | No | No |  |
| fam_scanCredit | ScanCredit | LONGVARCHAR |  | No | No |  |
| fam_SendNewsLetter | SendNewsletter | enum('FALSE','TRUE') | FALSE | Yes | No |  |
| fam_DateDeactivated | DateDeactivated | DATE |  | No | No |  |
| fam_Latitude | Latitude | DOUBLE |  | No | No |  |
| fam_Longitude | Longitude | DOUBLE |  | No | No |  |
| fam_Envelope | Envelope | SMALLINT(9) | 0 | Yes | No |  |

**Indexes**

- **fam_ID**: `fam_ID`

---

### note_nte
**PHP Class**: `Note` | **Domain**: Person & Family

**Description**: Contains all person and family notes, including the date, time, and person who entered the note

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| nte_ID | Id | mediumint(8) unsigned(8) |  | Yes | Yes |  |
| nte_per_ID | PerId | mediumint(8) unsigned(8) | 0 | Yes | No |  |
| nte_fam_ID | FamId | mediumint(8) unsigned(8) | 0 | Yes | No |  |
| nte_Private | Private | mediumint(8) unsigned(8) | 0 | Yes | No |  |
| nte_Text | Text | LONGVARCHAR |  | No | No |  |
| nte_DateEntered | DateEntered | TIMESTAMP |  | Yes | No |  |
| nte_DateLastEdited | DateLastEdited | TIMESTAMP |  | No | No |  |
| nte_EnteredBy | EnteredBy | mediumint(8)(8) | 0 | Yes | No |  |
| nte_EditedBy | EditedBy | mediumint(8) unsigned(8) | 0 | Yes | No |  |
| nte_Type | Type | VARCHAR(50) |  | No | No |  |

**Foreign Keys**

- -> `person_per` (nte_per_ID -> per_ID)
- -> `family_fam` (nte_fam_ID -> fam_ID)

---

### person_custom
**PHP Class**: `PersonCustom` | **Domain**: Person & Family

**Description**: Person custom fields

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| per_ID | PerId | SMALLINT(9) | 0 | Yes | Yes |  |

**Foreign Keys**

- -> `person_per` (per_ID -> per_ID)

---

### person_custom_master
**PHP Class**: `PersonCustomMaster` | **Domain**: Person & Family

**Description**: This contains definitions for the custom person fields

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| custom_Order | Order | SMALLINT | 0 | Yes | No |  |
| custom_Field | Id | VARCHAR(5) |  | Yes | Yes |  |
| custom_Name | Name | VARCHAR(40) |  | Yes | No |  |
| custom_Special | Special | mediumint(8) unsigned(8) |  | No | No |  |
| custom_FieldSec | FieldSecurity | TINYINT |  | Yes | No |  |
| type_ID | TypeId | TINYINT | 0 | Yes | No |  |

---

### person_per
**PHP Class**: `Person` | **Domain**: Person & Family

**Description**: This contains the main person data, including person names, person addresses, person phone numbers, and foreign keys to the family table

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| per_ID | Id | mediumint(9) unsigned(9) |  | Yes | Yes |  |
| per_Title | Title | VARCHAR(50) |  | No | No |  |
| per_FirstName | FirstName | VARCHAR(50) |  | No | No |  |
| per_MiddleName | MiddleName | VARCHAR(50) |  | No | No |  |
| per_LastName | LastName | VARCHAR(50) |  | No | No |  |
| per_Suffix | Suffix | VARCHAR(50) |  | No | No |  |
| per_Address1 | Address1 | VARCHAR(50) |  | No | No |  |
| per_Address2 | Address2 | VARCHAR(50) |  | No | No |  |
| per_City | City | VARCHAR(50) |  | No | No |  |
| per_State | State | VARCHAR(50) |  | No | No |  |
| per_Zip | Zip | VARCHAR(50) |  | No | No |  |
| per_Country | Country | VARCHAR(50) |  | No | No |  |
| per_HomePhone | HomePhone | VARCHAR(30) |  | No | No |  |
| per_WorkPhone | WorkPhone | VARCHAR(30) |  | No | No |  |
| per_CellPhone | CellPhone | VARCHAR(30) |  | No | No |  |
| per_Email | Email | VARCHAR(50) |  | No | No |  |
| per_WorkEmail | WorkEmail | VARCHAR(50) |  | No | No |  |
| per_BirthMonth | BirthMonth | tinyint(3) unsigned(3) | 0 | Yes | No |  |
| per_BirthDay | BirthDay | tinyint(3) unsigned(3) | 0 | Yes | No |  |
| per_BirthYear | BirthYear | smallint(4)(4) |  | No | No |  |
| per_MembershipDate | MembershipDate | DATE |  | No | No |  |
| per_Gender | Gender | tinyint(1) unsigned(1) | false | Yes | No |  |
| per_fmr_ID | FmrId | tinyint(3) unsigned(3) | 0 | Yes | No |  |
| per_cls_ID | ClsId | tinyint(3) unsigned(3) | 0 | Yes | No |  |
| per_fam_ID | FamId | smallint(5) unsigned(5) | 0 | Yes | No |  |
| per_Envelope | Envelope | smallint(5) unsigned(5) |  | No | No |  |
| per_DateLastEdited | DateLastEdited | TIMESTAMP |  | No | No |  |
| per_DateEntered | DateEntered | TIMESTAMP |  | Yes | No |  |
| per_EnteredBy | EnteredBy | smallint(5)(5) | 0 | Yes | No |  |
| per_EditedBy | EditedBy | smallint(5) unsigned(5) | 0 | No | No |  |
| per_FriendDate | FriendDate | DATE |  | No | No |  |
| per_Flags | Flags | SMALLINT(9) | 0 | Yes | No |  |
| per_Facebook | Facebook | VARCHAR(50) |  | No | No | Facebook username |
| per_Twitter | Twitter | VARCHAR(50) |  | No | No | Twitter username |
| per_LinkedIn | LinkedIn | VARCHAR(50) |  | No | No | LinkedIn name |

**Indexes**

- **per_ID**: `per_ID`

**Foreign Keys**

- -> `family_fam` (per_fam_ID -> fam_ID)

---

### whycame_why
**PHP Class**: `WhyCame` | **Domain**: Person & Family

**Description**: This contains the comments related to why people came

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| why_ID | Id | SMALLINT(9) |  | Yes | Yes |  |
| why_per_ID | PerId | SMALLINT(9) | 0 | Yes | No |  |
| why_join | Join | LONGVARCHAR |  | Yes | No |  |
| why_come | Come | LONGVARCHAR |  | Yes | No |  |
| why_suggest | Suggest | LONGVARCHAR |  | Yes | No |  |
| why_hearOfUs | HearOfUs | LONGVARCHAR |  | Yes | No |  |

**Foreign Keys**

- -> `person_per` (why_per_ID -> per_ID)

---

## Groups & Volunteers

### group_grp
**PHP Class**: `Group` | **Domain**: Groups & Volunteers

**Description**: This contains the name and description for each group, as well as foreign keys to the list of group roles

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| grp_ID | Id | mediumint(8) unsigned(8) |  | Yes | Yes |  |
| grp_Type | Type | TINYINT | 0 | Yes | No | The group type.  This is defined in list_lst.OptionId where lst_ID=3 |
| grp_RoleListID | RoleListId | mediumint(8) unsigned(8) | 0 | Yes | No | The lst_ID containing the names of the roles for this group |
| grp_DefaultRole | DefaultRole | SMALLINT(9) | 0 | Yes | No | The ID of the default role in this group's RoleList |
| grp_Name | Name | VARCHAR(50) |  | Yes | No |  |
| grp_Description | Description | LONGVARCHAR |  | No | No |  |
| grp_hasSpecialProps | HasSpecialProps | BOOLEAN | 0 | No | No |  |
| grp_active | Active | BOOLEAN(1) |  | Yes | No |  |
| grp_include_email_export | IncludeInEmailExport | BOOLEAN(1) |  | Yes | No | Should members of this group be included in MailChimp Export |

**Indexes**

- **grp_ID_2**: `grp_ID`

**Unique Constraints**

- **grp_ID**: `grp_ID`

**Foreign Keys**

- -> `list_lst` (grp_RoleListID -> lst_ID, grp_Type -> lst_OptionID)

---

### groupprop_master
**PHP Class**: `GroupPropMaster` | **Domain**: Groups & Volunteers

**Description**: This contains definitions for the group-specific fields

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| grp_ID | GrpId | mediumint(9) unsigned(9) | 0 | Yes | No |  |
| prop_ID | PropId | tinyint(3) unsigned(3) | 0 | Yes | No |  |
| prop_Field | Field | VARCHAR(5) | 0 | Yes | No |  |
| prop_Name | Name | VARCHAR(40) |  | No | No |  |
| prop_Description | Description | VARCHAR(60) |  | No | No |  |
| type_ID | TypeId | smallint(5) unsigned(5) | 0 | Yes | No |  |
| prop_Special | Special | mediumint(9) unsigned(9) |  | No | No |  |
| prop_PersonDisplay | PersonDisplay | enum('false','true') | false | Yes | No |  |

---

### person2group2role_p2g2r
**PHP Class**: `None` | **Domain**: Groups & Volunteers

**Description**: This table stores the information of which people are in which groups, and what group role each person holds in that group

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| p2g2r_per_ID | PersonId | mediumint(8) unsigned(8) | 0 | Yes | Yes |  |
| p2g2r_grp_ID | GroupId | mediumint(8) unsigned(8) | 0 | Yes | Yes |  |
| p2g2r_rle_ID | RoleId | mediumint(8) unsigned(8) | 0 | Yes | No |  |

**Indexes**

- **p2g2r_per_ID**: `p2g2r_per_ID, p2g2r_grp_ID, p2g2r_rle_ID`

**Foreign Keys**

- -> `person_per` (p2g2r_per_ID -> per_ID)
- -> `group_grp` (p2g2r_grp_ID -> grp_ID)

---

### person2volunteeropp_p2vo
**PHP Class**: `PersonVolunteerOpportunity` | **Domain**: Groups & Volunteers

**Description**: This table indicates which people are tied to which volunteer opportunities

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| p2vo_ID | Id | SMALLINT(9) |  | Yes | Yes |  |
| p2vo_per_ID | PersonId | SMALLINT(9) |  | No | No |  |
| p2vo_vol_ID | VolunteerOpportunityId | SMALLINT(9) |  | No | No |  |

**Unique Constraints**

- **p2vo_ID**: `p2vo_ID`

---

### volunteeropportunity_vol
**PHP Class**: `VolunteerOpportunity` | **Domain**: Groups & Volunteers

**Description**: This contains the names and descriptions of volunteer opportunities

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| vol_ID | Id | INTEGER(3) |  | Yes | Yes |  |
| vol_Order | Order | INTEGER(3) | 0 | Yes | No |  |
| vol_Active | Active | enum('true','false') | true | Yes | No |  |
| vol_Name | Name | VARCHAR(30) |  | No | No |  |
| vol_Description | Description | VARCHAR(100) |  | No | No |  |

**Unique Constraints**

- **vol_ID**: `vol_ID`

---

## Financial

### deposit_dep
**PHP Class**: `Deposit` | **Domain**: Financial

**Description**: This records deposits / payments

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| dep_ID | Id | mediumint(9) unsigned(9) |  | Yes | Yes |  |
| dep_Date | Date | DATE |  | No | No |  |
| dep_Comment | Comment | LONGVARCHAR |  | No | No |  |
| dep_EnteredBy | Enteredby | mediumint(9) unsigned(9) |  | No | No |  |
| dep_Closed | Closed | BOOLEAN(1) | false | Yes | No |  |
| dep_Type | Type | enum('Bank','CreditCard','BankDraft') | Bank | Yes | No |  |

---

### donateditem_di
**PHP Class**: `DonatedItem` | **Domain**: Financial

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| di_ID | Id | mediumint(9) unsigned(9) |  | Yes | Yes |  |
| di_item | Item | VARCHAR(32) |  | Yes | No |  |
| di_FR_ID | FrId | mediumint(9) unsigned(9) |  | Yes | No |  |
| di_donor_ID | DonorId | SMALLINT(9) | 0 | Yes | No |  |
| di_buyer_ID | BuyerId | SMALLINT(9) | 0 | Yes | No |  |
| di_multibuy | Multibuy | SMALLINT(1) | 0 | Yes | No |  |
| di_title | Title | VARCHAR(128) |  | Yes | No |  |
| di_description | Description | LONGVARCHAR |  | No | No |  |
| di_sellprice | Sellprice | DECIMAL(8) |  | No | No |  |
| di_estprice | Estprice | DECIMAL(8) |  | No | No |  |
| di_minimum | Minimum | DECIMAL(8) |  | No | No |  |
| di_materialvalue | MaterialValue | DECIMAL(8) |  | No | No |  |
| di_EnteredBy | Enteredby | smallint(5) unsigned(5) | 0 | Yes | No |  |
| di_EnteredDate | Entereddate | DATE |  | Yes | No |  |
| di_picture | Picture | LONGVARCHAR |  | No | No |  |

**Unique Constraints**

- **di_ID**: `di_ID`

---

### donationfund_fun
**PHP Class**: `DonationFund` | **Domain**: Financial

**Description**: This contains the defined donation funds

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| fun_ID | Id | TINYINT(3) |  | Yes | Yes |  |
| fun_Active | Active | enum('true','false') | true | Yes | No |  |
| fun_Name | Name | VARCHAR(30) |  | No | No |  |
| fun_Description | Description | VARCHAR(100) |  | No | No |  |
| fun_Order | Order | INTEGER | 0 | Yes | No |  |

**Unique Constraints**

- **fun_ID**: `fun_ID`

---

### fundraiser_fr
**PHP Class**: `FundRaiser` | **Domain**: Financial

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| fr_ID | Id | mediumint(9) unsigned(9) |  | Yes | Yes |  |
| fr_date | Date | DATE |  | No | No |  |
| fr_title | Title | VARCHAR(128) |  | Yes | No |  |
| fr_description | Description | LONGVARCHAR |  | No | No |  |
| fr_EnteredBy | EnteredBy | smallint(5) unsigned(5) | 0 | Yes | No |  |
| fr_EnteredDate | EnteredDate | DATE |  | Yes | No |  |

**Unique Constraints**

- **fr_ID**: `fr_ID`

---

### pledge_plg
**PHP Class**: `Pledge` | **Domain**: Financial

**Description**: This contains all payment/pledge information

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| plg_plgID | Id | mediumint(9)(9) |  | Yes | Yes |  |
| plg_FamID | FamId | mediumint(9)(9) |  | No | No |  |
| plg_FYID | FyId | mediumint(9)(9) |  | No | No |  |
| plg_date | Date | DATE |  | No | No |  |
| plg_amount | Amount | DECIMAL(8) |  | No | No |  |
| plg_schedule | Schedule | enum('Weekly','Monthly','Quarterly','Once','Other') |  | No | No |  |
| plg_method | Method | enum('CREDITCARD','CHECK','CASH','BANKDRAFT') |  | No | No |  |
| plg_comment | Comment | LONGVARCHAR |  | No | No |  |
| plg_DateLastEdited | DateLastEdited | DATE | 2016-01-01 | Yes | No |  |
| plg_EditedBy | EditedBy | mediumint(9)(9) | 0 | Yes | No |  |
| plg_PledgeOrPayment | PledgeOrPayment | enum('Pledge','Payment') | Pledge | Yes | No |  |
| plg_fundID | FundId | tinyint(3) unsigned(3) |  | No | No |  |
| plg_depID | DepId | mediumint(9) unsigned(9) |  | No | No |  |
| plg_CheckNo | CheckNo | bigint(16) unsigned(16) |  | No | No |  |
| plg_Problem | Problem | BOOLEAN(1) |  | No | No |  |
| plg_scanString | ScanString | LONGVARCHAR |  | No | No |  |
| plg_aut_ID | AutId | mediumint(9)(9) | 0 | Yes | No |  |
| plg_aut_Cleared | AutCleared | BOOLEAN(1) | false | Yes | No |  |
| plg_aut_ResultID | AutResultId | mediumint(9)(9) | 0 | Yes | No |  |
| plg_NonDeductible | Nondeductible | DECIMAL(8) |  | Yes | No |  |
| plg_GroupKey | GroupKey | VARCHAR(64) |  | Yes | No |  |

**Foreign Keys**

- -> `deposit_dep` (plg_depID -> dep_ID)
- -> `donationfund_fun` (plg_fundID -> fun_ID)
- -> `family_fam` (plg_FamID -> fam_ID)
- -> `person_per` (plg_EditedBy -> per_ID)

---

## Events

### event_attend
**PHP Class**: `EventAttend` | **Domain**: Events

**Description**: this indicates which people attended which events

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| attend_id | AttendId | INTEGER |  | Yes | Yes |  |
| event_id | EventId | INTEGER | 0 | Yes | No |  |
| person_id | PersonId | INTEGER | 0 | Yes | No |  |
| checkin_date | CheckinDate | TIMESTAMP |  | No | No |  |
| checkin_id | CheckinId | INTEGER |  | No | No |  |
| checkout_date | CheckoutDate | TIMESTAMP |  | No | No |  |
| checkout_id | CheckoutId | INTEGER |  | No | No |  |

**Unique Constraints**

- **event_id**: `event_id, person_id`

**Foreign Keys**

- -> `events_event` (event_id -> event_id)
- -> `person_per` (person_id -> per_ID)

---

### event_audience
**PHP Class**: `EventAudience` | **Domain**: Events

**Description**: This is a join-table to link an event with a prospective audience for the purpose of advertising / outreach

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| event_id | EventId | mediumint(8) unsigned(8) |  | Yes | Yes |  |
| group_id | GroupId | mediumint(8) unsigned(8) |  | Yes | Yes |  |

**Foreign Keys**

- -> `events_event` (event_id -> event_id)
- -> `group_grp` (group_id -> grp_ID)

---

### event_types
**PHP Class**: `EventType` | **Domain**: Events

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| type_id | Id | INTEGER |  | Yes | Yes |  |
| type_name | Name | VARCHAR(255) |  | Yes | No |  |
| type_defstarttime | DefStartTime | TIME | 00:00:00 | Yes | No |  |
| type_defrecurtype | DefRecurType | enum('none','weekly','monthly','yearly') | none | Yes | No |  |
| type_defrecurDOW | DefRecurDOW | enum('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday') | Sunday | Yes | No |  |
| type_defrecurDOM | DefRecurDOM | CHAR(2) | 0 | Yes | No |  |
| type_defrecurDOY | DefRecurDOY | DATE | 2016-01-01 | Yes | No |  |
| type_active | Active | INTEGER(1) | 1 | Yes | No |  |
| type_grpid | GroupId | INTEGER | 0 | No | No |  |

**Foreign Keys**

- -> `group_grp` (type_grpid -> grp_ID)

---

### eventcountnames_evctnm
**PHP Class**: `EventCountName` | **Domain**: Events

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| evctnm_countid | Id | INTEGER(5) |  | Yes | Yes |  |
| evctnm_eventtypeid | TypeId | SMALLINT(5) | 0 | Yes | No |  |
| evctnm_countname | Name | VARCHAR(20) |  | Yes | No |  |

**Unique Constraints**

- **evctnm_eventtypeid**: `evctnm_eventtypeid, evctnm_countname`

---

### eventcounts_evtcnt
**PHP Class**: `EventCounts` | **Domain**: Events

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| evtcnt_eventid | EvtcntEventid | INTEGER(5) | 0 | Yes | Yes |  |
| evtcnt_countid | EvtcntCountid | INTEGER(5) | 0 | Yes | Yes |  |
| evtcnt_countname | EvtcntCountname | VARCHAR(20) |  | No | No |  |
| evtcnt_countcount | EvtcntCountcount | INTEGER(6) |  | No | No |  |
| evtcnt_notes | EvtcntNotes | VARCHAR(20) |  | No | No |  |

---

### events_event
**PHP Class**: `Event` | **Domain**: Events

**Description**: This contains events

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| event_id | Id | INTEGER |  | Yes | Yes |  |
| event_type | Type | INTEGER | 0 | Yes | No |  |
| event_title | Title | VARCHAR(255) |  | Yes | No |  |
| event_desc | Desc | VARCHAR(255) |  | No | No |  |
| event_text | Text | LONGVARCHAR |  | No | No |  |
| event_start | Start | TIMESTAMP |  | Yes | No |  |
| event_end | End | TIMESTAMP |  | Yes | No |  |
| inactive | InActive | INTEGER(1) | 0 | Yes | No |  |
| location_id | LocationId | INTEGER | 0 | Yes | No |  |
| primary_contact_person_id | PrimaryContactPersonId | INTEGER | 0 | Yes | No |  |
| secondary_contact_person_id | SecondaryContactPersonId | INTEGER | 0 | Yes | No |  |
| event_url | URL | LONGVARCHAR |  | No | No |  |

**Indexes**

- **event_txt**: `event_text`

**Foreign Keys**

- -> `event_types` (event_type -> type_id)
- -> `person_per` (event_type -> per_ID)
- -> `person_per` (secondary_contact_person_id -> per_ID)
- -> `locations` (location_id -> location_id)

---

## System

### config_cfg
**PHP Class**: `Config` | **Domain**: System

**Description**: This table contains all non-default configuration parameter names and values

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| cfg_id | Id | INTEGER | 0 | Yes | Yes |  |
| cfg_name | Name | VARCHAR(50) |  | Yes | No |  |
| cfg_value | Value | LONGVARCHAR |  | No | No |  |

**Indexes**

- **cfg_id**: `cfg_id`

**Unique Constraints**

- **cfg_name**: `cfg_name`

---

### list_lst
**PHP Class**: `ListOption` | **Domain**: System

**Description**: This table stores the options for most of the drop down lists in churchCRM, including person classifications, family roles, group types, group roles, group-specific property types, and custom field value lists.

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| lst_ID | Id | mediumint(8) unsigned(8) | 0 | Yes | Yes | The ID of the list.  Since this is a composite primary key, there may be multiple List IDs |
| lst_OptionID | OptionId | mediumint(8) unsigned(8) | 0 | Yes | Yes | The ID of the option in this list.  ***List ID + List Option ID must be unique*** |
| lst_OptionSequence | OptionSequence | tinyint(3) unsigned(3) | 0 | Yes | No | The order in which to display items in this list |
| lst_OptionName | OptionName | VARCHAR(50) |  | Yes | No | The actual value for this list option |

---

### user_settings
**PHP Class**: `UserSetting` | **Domain**: System

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| user_id | UserId | mediumint(9) unsigned(9) |  | Yes | Yes |  |
| setting_name | Name | VARCHAR(50) |  | Yes | Yes |  |
| setting_value | Value | VARCHAR(50) |  | No | No |  |

**Foreign Keys**

- -> `user_usr` (user_id -> usr_per_ID)

---

### user_usr
**PHP Class**: `User` | **Domain**: System

**Description**: This contains the login information and specific settings for each ChurchCRM user

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| usr_per_ID | PersonId | mediumint(9) unsigned(9) | 0 | Yes | Yes |  |
| usr_Password | Password | VARCHAR(500) |  | Yes | No |  |
| usr_NeedPasswordChange | NeedPasswordChange | tinyint(3) unsigned(1) | 1 | Yes | No |  |
| usr_LastLogin | LastLogin | TIMESTAMP | 2016-01-01 00:00:00 | Yes | No |  |
| usr_LoginCount | LoginCount | smallint(5) unsigned(5) | 0 | Yes | No |  |
| usr_FailedLogins | FailedLogins | tinyint(3) unsigned(3) | 0 | Yes | No |  |
| usr_AddRecords | AddRecords | tinyint(1) unsigned(1) | 0 | Yes | No |  |
| usr_EditRecords | EditRecords | tinyint(1) unsigned(1) | 0 | Yes | No |  |
| usr_DeleteRecords | DeleteRecords | tinyint(1) unsigned(1) | 0 | Yes | No |  |
| usr_MenuOptions | MenuOptions | tinyint(1) unsigned(1) | 0 | Yes | No |  |
| usr_ManageGroups | ManageGroups | tinyint(1) unsigned(1) | 0 | Yes | No |  |
| usr_Finance | Finance | tinyint(1) unsigned(1) | 0 | Yes | No |  |
| usr_Notes | Notes | tinyint(1) unsigned(1) | 0 | Yes | No |  |
| usr_Admin | Admin | tinyint(1) unsigned(1) | 0 | Yes | No |  |
| usr_defaultFY | DefaultFY | SMALLINT(9) | 10 | Yes | No |  |
| usr_currentDeposit | CurrentDeposit | SMALLINT(9) | 0 | Yes | No |  |
| usr_UserName | UserName | VARCHAR(32) |  | Yes | No |  |
| usr_Style | UserStyle | VARCHAR(50) |  | No | No |  |
| usr_ApiKey | ApiKey | VARCHAR(255) |  | No | No |  |
| usr_TwoFactorAuthSecret | TwoFactorAuthSecret | VARCHAR(255) |  | No | No |  |
| usr_TwoFactorAuthLastKeyTimestamp | TwoFactorAuthLastKeyTimestamp | SMALLINT(9) |  | No | No |  |
| usr_TwoFactorAuthRecoveryCodes | TwoFactorAuthRecoveryCodes | LONGVARCHAR |  | No | No |  |
| usr_EditSelf | EditSelf | tinyint(1) unsigned(1) | 0 | Yes | No |  |
| usr_CalStart | CalStart | DATE |  | No | No |  |
| usr_CalEnd | CalEnd | DATE |  | No | No |  |
| usr_CalNoSchool1 | CalNoSchool1 | DATE |  | No | No |  |
| usr_CalNoSchool2 | CalNoSchool2 | DATE |  | No | No |  |
| usr_CalNoSchool3 | CalNoSchool3 | DATE |  | No | No |  |
| usr_CalNoSchool4 | CalNoSchool4 | DATE |  | No | No |  |
| usr_CalNoSchool5 | CalNoSchool5 | DATE |  | No | No |  |
| usr_CalNoSchool6 | CalNoSchool6 | DATE |  | No | No |  |
| usr_CalNoSchool7 | CalNoSchool7 | DATE |  | No | No |  |
| usr_CalNoSchool8 | CalNoSchool8 | DATE |  | No | No |  |
| usr_SearchFamily | Searchfamily | TINYINT(3) |  | No | No |  |

**Indexes**

- **usr_per_ID**: `usr_per_ID`

**Unique Constraints**

- **usr_UserName**: `usr_UserName`
- **usr_ApiKey**: `usr_ApiKey`

**Foreign Keys**

- -> `person_per` (usr_per_ID -> per_ID)

---

### userconfig_ucfg
**PHP Class**: `UserConfig` | **Domain**: System

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| ucfg_per_id | PeronId | mediumint(9) unsigned(9) |  | Yes | Yes |  |
| ucfg_id | Id | INTEGER | 0 | Yes | Yes |  |
| ucfg_name | Name | VARCHAR(50) |  | Yes | No |  |
| ucfg_value | Value | LONGVARCHAR |  | No | No |  |
| ucfg_type | Type | enum('text','number','date','boolean','textarea') | text | Yes | No |  |
| ucfg_tooltip | Tooltip | LONGVARCHAR |  | Yes | No |  |
| ucfg_permission | Permission | enum('FALSE','TRUE') | FALSE | Yes | No |  |
| ucfg_cat | Cat | VARCHAR(20) |  | Yes | No |  |

**Foreign Keys**

- -> `user_usr` (ucfg_per_id -> usr_per_ID)

---

### version_ver
**PHP Class**: `Version` | **Domain**: System

**Description**: History of all version upgrades applied to this database

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| ver_ID | Id | mediumint(9) unsigned(9) |  | Yes | Yes |  |
| ver_version | Version | VARCHAR(50) |  | Yes | No |  |
| ver_update_start | UpdateStart | TIMESTAMP |  | No | No |  |
| ver_update_end | UpdateEnd | TIMESTAMP |  | No | No |  |

**Unique Constraints**

- **ver_version**: `ver_version`

---

## Properties

### property_pro
**PHP Class**: `Property` | **Domain**: Properties

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| pro_ID | ProId | mediumint(8) unsigned(8) |  | Yes | Yes |  |
| pro_Class | ProClass | VARCHAR(10) |  | Yes | No |  |
| pro_prt_ID | ProPrtId | mediumint(8) unsigned(8) | 0 | Yes | No |  |
| pro_Name | ProName | VARCHAR(200) | 0 | Yes | No |  |
| pro_Description | ProDescription | LONGVARCHAR |  | Yes | No |  |
| pro_Prompt | ProPrompt | VARCHAR(255) |  | No | No |  |

**Indexes**

- **pro_ID_2**: `pro_ID`

**Unique Constraints**

- **pro_ID**: `pro_ID`

**Foreign Keys**

- -> `propertytype_prt` (pro_prt_ID -> prt_ID)

---

### propertytype_prt
**PHP Class**: `PropertyType` | **Domain**: Properties

**Description**: This contains all the defined property types

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| prt_ID | PrtId | SMALLINT(9) |  | Yes | Yes |  |
| prt_Class | PrtClass | VARCHAR(10) |  | Yes | No |  |
| prt_Name | PrtName | VARCHAR(50) |  | Yes | No |  |
| prt_Description | PrtDescription | LONGVARCHAR |  | Yes | No |  |

**Indexes**

- **prt_ID_2**: `prt_ID`

**Unique Constraints**

- **prt_ID**: `prt_ID`

---

### record2property_r2p
**PHP Class**: `RecordProperty` | **Domain**: Properties

**Description**: This table indicates which persons, families, or groups are assigned specific properties and what the values of those properties are.

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| r2p_pro_ID | PropertyId | mediumint(8) unsigned(8) |  | Yes | Yes |  |
| r2p_record_ID | RecordId | mediumint(8) unsigned(8) |  | Yes | Yes |  |
| r2p_Value | PropertyValue | LONGVARCHAR |  | Yes | No |  |

**Foreign Keys**

- -> `property_pro` (r2p_pro_ID -> pro_ID)

---

## Kiosk

### kioskassginment_kasm
**PHP Class**: `KioskAssignment` | **Domain**: Kiosk

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| kasm_ID | Id | mediumint(9) unsigned(9) |  | Yes | Yes |  |
| kasm_kdevId | KioskId | INTEGER(9) |  | No | No |  |
| kasm_AssignmentType | AssignmentType | INTEGER(9) |  | No | No | The kiosk's current role. |
| kasm_EventId | EventId | INTEGER(9) |  | No | No | Optional.  If the current role is for event check-in, populate this value |

**Indexes**

- **kasm_ID**: `kasm_ID`

**Foreign Keys**

- -> `kioskdevice_kdev` (kasm_kdevId -> kdev_ID)
- -> `events_event` (kasm_EventId -> event_id)

---

### kioskdevice_kdev
**PHP Class**: `KioskDevice` | **Domain**: Kiosk

**Description**: This contains a list of all (un)registered kiosk devices

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| kdev_ID | Id | mediumint(9) unsigned(9) |  | Yes | Yes |  |
| kdev_GUIDHash | GUIDHash | VARCHAR(36) |  | No | No | SHA256 Hash of the GUID stored in the kiosk's cookie |
| kdev_Name | Name | VARCHAR(50) |  | No | No | Name of the kiosk |
| kdev_deviceType | DeviceType | LONGVARCHAR |  | No | No | Kiosk device type |
| kdev_lastHeartbeat | LastHeartbeat | LONGVARCHAR |  | No | No | Last time the kiosk sent a heartbeat |
| kdev_Accepted | Accepted | BOOLEAN |  | No | No | Has the admin accepted the kiosk after initial registration? |
| kdev_PendingCommands | PendingCommands | LONGVARCHAR |  | No | No | Commands waiting to be sent to the kiosk |

**Indexes**

- **kdev_ID**: `kdev_ID`

---

## Location & Calendar

### calendar_events
**PHP Class**: `CalendarEvent` | **Domain**: Location & Calendar

**Description**: This is a join-table to link an event with a calendar

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| calendar_id | CalendarId | mediumint(8) unsigned(8) |  | Yes | Yes |  |
| event_id | EventId | mediumint(8) unsigned(8) |  | Yes | Yes |  |

**Foreign Keys**

- -> `calendars` (calendar_id -> calendar_id)
- -> `events_event` (event_id -> event_id)

---

### calendars
**PHP Class**: `Calendar` | **Domain**: Location & Calendar

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| calendar_id | Id | mediumint(8) unsigned(8) |  | Yes | Yes |  |
| name | Name | VARCHAR(99) |  | Yes | No |  |
| accesstoken | AccessToken | VARCHAR(255) |  | No | No |  |
| backgroundColor | BackgroundColor | VARCHAR(6) |  | No | No |  |
| foregroundColor | ForegroundColor | VARCHAR(6) |  | No | No |  |

**Unique Constraints**

- **accesstoken**: `accesstoken`

---

### locations
**PHP Class**: `Location` | **Domain**: Location & Calendar

**Description**: This is a table for storing all physical locations (Church Offices, Events, etc) 

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| location_id | LocationId | mediumint(8) unsigned(8) |  | Yes | Yes |  |
| location_typeID | LocationType | mediumint(8) unsigned(8) |  | Yes | No |  |
| location_name | None | VARCHAR(256) |  | Yes | No | Location Name (e.g 'Main Campus') |
| location_address | None | VARCHAR(45) |  | Yes | No |  |
| location_city | None | VARCHAR(45) |  | Yes | No |  |
| location_state | None | VARCHAR(45) |  | Yes | No |  |
| location_zip | None | VARCHAR(45) |  | Yes | No |  |
| location_country | None | VARCHAR(45) |  | Yes | No |  |
| location_phone | None | VARCHAR(45) |  | Yes | No |  |
| location_email | None | VARCHAR(45) |  | Yes | No |  |
| location_timzezone | None | VARCHAR(45) |  | Yes | No |  |

---

## Queries

### query_qry
**PHP Class**: `PredefinedReports` | **Domain**: Queries

**Description**: This contains all the predefined queries that appear in the queries page

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| qry_ID | QryId | mediumint(8) unsigned(8) |  | Yes | Yes |  |
| qry_SQL | QrySql | LONGVARCHAR |  | Yes | No |  |
| qry_Name | QryName | VARCHAR(255) |  | Yes | No |  |
| qry_Description | QryDescription | LONGVARCHAR |  | Yes | No |  |
| qry_Count | QryCount | tinyint(1) unsigned(1) | false | Yes | No |  |

**Indexes**

- **qry_ID_2**: `qry_ID`

**Unique Constraints**

- **qry_ID**: `qry_ID`

---

### queryparameteroptions_qpo
**PHP Class**: `QueryParameterOptions` | **Domain**: Queries

**Description**: Defines the values for the parameters for each query

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| qpo_ID | QpoId | smallint(5) unsigned(5) |  | Yes | Yes |  |
| qpo_qrp_ID | QpoQrpId | mediumint(8) unsigned(8) | 0 | Yes | No |  |
| qpo_Display | QpoDisplay | VARCHAR(50) |  | Yes | No |  |
| qpo_Value | QpoValue | VARCHAR(50) |  | Yes | No |  |

**Unique Constraints**

- **qpo_ID**: `qpo_ID`

---

### queryparameters_qrp
**PHP Class**: `QueryParameters` | **Domain**: Queries

**Description**: defines the parameters for each query

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| qrp_ID | Id | mediumint(8) unsigned(8) |  | Yes | Yes |  |
| qrp_qry_ID | QryId | mediumint(8) unsigned(8) | 0 | Yes | No |  |
| qrp_Type | Type | tinyint(3) unsigned(3) | 0 | Yes | No |  |
| qrp_OptionSQL | OptionSQL | LONGVARCHAR |  | No | No |  |
| qrp_Name | Name | VARCHAR(25) |  | No | No |  |
| qrp_Description | Description | LONGVARCHAR |  | No | No |  |
| qrp_Alias | Alias | VARCHAR(25) |  | No | No |  |
| qrp_Default | Default | VARCHAR(25) |  | No | No |  |
| qrp_Required | Required | tinyint(3) unsigned(3) | 0 | Yes | No |  |
| qrp_InputBoxSize | InputBoxSize | tinyint(3) unsigned(3) | 0 | Yes | No |  |
| qrp_Validation | Validation | VARCHAR(5) |  | Yes | No |  |
| qrp_NumericMax | NumericMax | INTEGER |  | No | No |  |
| qrp_NumericMin | NumericMin | INTEGER |  | No | No |  |
| qrp_AlphaMinLength | AlphaMinLength | INTEGER |  | No | No |  |
| qrp_AlphaMaxLength | AlphaMaxLength | INTEGER |  | No | No |  |

**Indexes**

- **qrp_ID_2**: `qrp_ID`
- **qrp_qry_ID**: `qrp_qry_ID`

**Unique Constraints**

- **qrp_ID**: `qrp_ID`

---

## Tokens

### tokens
**PHP Class**: `Token` | **Domain**: Tokens

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| token | Token | VARCHAR |  | Yes | Yes |  |
| type | Type | VARCHAR |  | Yes | No |  |
| valid_until_date | ValidUntilDate | DATE |  | No | No |  |
| reference_id | ReferenceId | INTEGER |  | No | No |  |
| remainingUses | RemainingUses | INTEGER | 0 | No | No |  |

---

## Menu

### menu_links
**PHP Class**: `MenuLink` | **Domain**: Menu

| Field | PHP Type | SQL Type | Default | Required | PK | Description |
|-------|----------|----------|---------|----------|----|-------------|
| linkId | Id | mediumint(9) unsigned(9) |  | Yes | Yes |  |
| linkName | Name | VARCHAR(50) |  | No | No |  |
| linkUri | Uri | VARCHAR(500) |  | No | No |  |
| linkOrder | Order | SMALLINT |  | No | No |  |

**Indexes**

- **linkId**: `linkId`

---


---

## 第二部分：核心实体关系矩阵

### Person - Family - Group 关系

| Source Entity | Relationship | Target Entity | Cardinality |
|---------------|--------------|---------------|-------------|
| person_per | belongs to | family_fam | N:1 (per_fam_ID) |
| person_per | classified by | list_lst | N:1 (per_cls_ID) |
| person_per | member of | group_grp | N:M (p2g2r) |
| person_per | has note | note_nte | 1:N (nte_per_ID) |
| family_fam | has member | person_per | 1:N (per_fam_ID) |
| group_grp | has member | person_per | N:M (p2g2r) |

### Financial 关系

| Source Entity | Relationship | Target Entity | Cardinality |
|---------------|--------------|---------------|-------------|
| pledge_plg | belongs to | family_fam | N:1 (plg_FamID) |
| pledge_plg | assigned to | deposit_dep | N:1 (plg_depID) |
| pledge_plg | assigned to | donationfund_fun | N:1 (plg_fundID) |
| deposit_dep | contains | pledge_plg | 1:N (plg_depID) |

### Event 关系

| Source Entity | Relationship | Target Entity | Cardinality |
|---------------|--------------|---------------|-------------|
| events_event | typed by | event_types | N:1 (event_type) |
| events_event | located at | locations | N:1 (location_id) |
| events_event | attended by | person_per | N:M (event_attend) |
| event_types | targets | group_grp | N:1 (type_grpid) |

---

## 第三部分：API 数据模型映射

### Private API 端点摘要

- **GET** `/api/database/people/export/chmeetings` - Export all people as a ChMeetings-compatible CSV file (Admin role required)
- **DELETE** `/api/database/reset` - Drop all database tables and views, clear uploaded images, and destroy the session (Admin role required)
- **POST** `/api/demo/load` - Import demo data into the application (Admin role required)
- **GET** `/admin/api/import/csv/families` - Download a CSV import template for families (Admin role required)
- **POST** `/admin/api/import/csv/upload` - Upload a CSV file and return headers with auto-detected field mappings
- **POST** `/admin/api/import/csv/execute` - Execute a CSV import using a previously uploaded file and column mapping
- **GET** `/api/orphaned-files` - List orphaned files
- **POST** `/api/orphaned-files/delete-all` - Delete all orphaned files
- **GET** `/api/upgrade/download-latest-release` - Download the latest release from GitHub
- **POST** `/api/upgrade/do-upgrade` - Apply the system upgrade
- **POST** `/api/upgrade/refresh-upgrade-info` - Refresh upgrade information from GitHub
- **POST** `/api/user/{userId}/password/reset` - Reset a user's password to a random value and email it to them (Admin role required)
- **POST** `/api/user/{userId}/disableTwoFactor` - Disable two-factor authentication for a user (Admin role required)
- **POST** `/api/user/{userId}/login/reset` - Reset failed login counter and send unlock email (Admin role required)
- **DELETE** `/api/user/{userId}/` - Delete a user account (Admin role required)
- **GET** `/api/user/{userId}/permissions` - Get permission flags for a user (Admin role required)
- **POST** `/background/timerjobs` - Trigger background timer jobs (scheduled task runner)
- **GET** `/systemcalendars` - List all system calendars
- **GET** `/systemcalendars/{id}/events` - Get events from a system calendar
- **GET** `/systemcalendars/{id}/events/{eventid}` - Get a single event from a system calendar

... 共 184 个端点

### Public API 端点摘要

- **GET** `/public/calendar/{CalendarAccessToken}/events` - Get public calendar events as JSON
- **GET** `/public/calendar/{CalendarAccessToken}/ics` - Download public calendar as ICS file
- **GET** `/public/calendar/{CalendarAccessToken}/fullcalendar` - Get public calendar events in FullCalendar format
- **GET** `/public/data/countries` - List all countries
- **GET** `/public/data/countries/{countryCode}/states` - List states/provinces for a country
- **POST** `/public/register/family` - Register a new family
- **POST** `/public/register/person` - Register a new individual person
- **POST** `/public/user/login` - Log in and retrieve an API key
- **POST** `/public/user/password-reset` - Request a password reset email
- **GET** `/public/echo` - Health check / echo
- **POST** `/public/csp-report` - Log a Content Security Policy violation report

---

## 第四部分：服务层数据操作摘要

### PersonService
- 管理 person_per 表的 CRUD 操作
- 处理人员分类 (per_cls_ID -> list_lst)
- 关联家庭 (per_fam_ID -> family_fam)
- 社交媒体链接管理

### FamilyService
- 管理 family_fam 表的 CRUD 操作
- 处理家庭地址和联系方式
- 家庭成员管理

### GroupService
- 管理 group_grp 表
- 处理 person2group2role_p2g2r 关联表
- 组成员增删改查

### FinancialService
- 管理 pledge_plg 表
- 处理奉献承诺和付款
- 关联 donationfund_fun 和 deposit_dep

### DepositService
- 管理 deposit_dep 表
- 处理存款批次
- 关联 pledge_plg 付款记录

---

## 第五部分：完整 Mermaid ER 图代码

请参考文件: `/home/linuxuser/crm_complete_er.mmd`

---

## 第六部分：完整数据流图代码

请参考文件: `/home/linuxuser/crm_complete_flow.mmd`

---

## 附录：表名与PHP类名对照表

| 物理表名 | PHP类名 | 业务域 |
|----------|---------|--------|
| calendar_events | CalendarEvent | Location & Calendar |
| calendars | Calendar | Location & Calendar |
| config_cfg | Config | System |
| deposit_dep | Deposit | Financial |
| donateditem_di | DonatedItem | Financial |
| donationfund_fun | DonationFund | Financial |
| event_attend | EventAttend | Events |
| event_audience | EventAudience | Events |
| event_types | EventType | Events |
| eventcountnames_evctnm | EventCountName | Events |
| eventcounts_evtcnt | EventCounts | Events |
| events_event | Event | Events |
| family_custom | FamilyCustom | Person & Family |
| family_custom_master | FamilyCustomMaster | Person & Family |
| family_fam | Family | Person & Family |
| fundraiser_fr | FundRaiser | Financial |
| group_grp | Group | Groups & Volunteers |
| groupprop_master | GroupPropMaster | Groups & Volunteers |
| kioskassginment_kasm | KioskAssignment | Kiosk |
| kioskdevice_kdev | KioskDevice | Kiosk |
| list_lst | ListOption | System |
| locations | Location | Location & Calendar |
| menu_links | MenuLink | Menu |
| note_nte | Note | Person & Family |
| person2group2role_p2g2r | None | Groups & Volunteers |
| person2volunteeropp_p2vo | PersonVolunteerOpportunity | Groups & Volunteers |
| person_custom | PersonCustom | Person & Family |
| person_custom_master | PersonCustomMaster | Person & Family |
| person_per | Person | Person & Family |
| pledge_plg | Pledge | Financial |
| property_pro | Property | Properties |
| propertytype_prt | PropertyType | Properties |
| query_qry | PredefinedReports | Queries |
| queryparameteroptions_qpo | QueryParameterOptions | Queries |
| queryparameters_qrp | QueryParameters | Queries |
| record2property_r2p | RecordProperty | Properties |
| tokens | Token | Tokens |
| user_settings | UserSetting | System |
| user_usr | User | System |
| userconfig_ucfg | UserConfig | System |
| version_ver | Version | System |
| volunteeropportunity_vol | VolunteerOpportunity | Groups & Volunteers |
| whycame_why | WhyCame | Person & Family |


---

**报告生成完成**
