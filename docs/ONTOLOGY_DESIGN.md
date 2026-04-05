# ChurchCRM 本体设计文档 (ONTOLOGY_DESIGN.md)

## 1. 概述

本文档描述 ChurchCRM 系统的 RDF/OWL 本体（Ontology）设计。该本体从 ChurchCRM 数据库的 43 张表中推导而来，为教会管理系统提供统一的语义数据层，支持知识图谱构建、语义查询和数据互操作性。

| 属性 | 值 |
|------|-----|
| 版本 | 1.0.0 |
| 生成日期 | 2026-04-05 |
| 基础命名空间 | `http://churchcrm.org/ontology/` |
| 资源命名空间 | `http://churchcrm.org/resource/` |

---

## 2. 设计原则

1. **表→类映射**: 每张数据库表映射为一个 OWL Class（如 `crm:Person`, `crm:Family`）。
2. **外键→对象属性**: 每个外键关系映射为一个 OWL ObjectProperty，含 Domain/Range 约束。
3. **字段→数据类型属性**: 每个非外键字段映射为一个 OWL DatatypeProperty，XSD 类型约束。
4. **桥接表**: 关联表（如 `PersonGroupRole`, `EventAttend`）生成双向 ObjectProperty，体现多对多关系。
5. **命名规范**: Class = PascalCase（如 `crm:Person`），Property = lowerCamelCase（如 `crm:firstName`）。

---

## 3. 本体统计

| 指标 | 数量 |
|------|------|
| OWL Classes | 43 |
| Object Properties | 33 |
| Datatype Properties | 329 |
| 数据库表（来源） | 43 |

---

## 4. 类清单

| # | 数据库表 | OWL Class | PK | 外键数 | 数据字段数 |
|---|----------|-----------|----|--------|----------|
| 1 | `Calendar` | `crm:Calendar` | `calendar_id` | 0 | 4 |
| 2 | `CalendarEvent` | `crm:CalendarEvent` | `event_id` | 0 | 0 |
| 3 | `Config` | `crm:Config` | `cfg_id` | 0 | 2 |
| 4 | `Deposit` | `crm:Deposit` | `dep_ID` | 0 | 5 |
| 5 | `DonatedItem` | `crm:DonatedItem` | `di_ID` | 0 | 14 |
| 6 | `DonationFund` | `crm:DonationFund` | `fun_ID` | 0 | 4 |
| 7 | `Event` | `crm:Event` | `event_id` | 0 | 11 |
| 8 | `EventAttend` | `crm:EventAttend` | `attend_id` | 0 | 6 |
| 9 | `EventAudience` | `crm:EventAudience` | `group_id` | 0 | 0 |
| 10 | `EventCountName` | `crm:EventCountName` | `evctnm_countid` | 0 | 2 |
| 11 | `EventCounts` | `crm:EventCounts` | `evtcnt_countid` | 0 | 3 |
| 12 | `EventType` | `crm:EventType` | `type_id` | 0 | 8 |
| 13 | `Family` | `crm:Family` | `fam_ID` | 0 | 21 |
| 14 | `FamilyCustom` | `crm:FamilyCustom` | `fam_ID` | 0 | 0 |
| 15 | `FamilyCustomMaster` | `crm:FamilyCustomMaster` | `fam_custom_Field` | 0 | 5 |
| 16 | `FundRaiser` | `crm:FundRaiser` | `fr_ID` | 0 | 5 |
| 17 | `Group` | `crm:Group` | `grp_ID` | 0 | 8 |
| 18 | `GroupPropMaster` | `crm:GroupPropMaster` | `—` | 0 | 8 |
| 19 | `KioskAssignment` | `crm:KioskAssignment` | `kasm_ID` | 0 | 3 |
| 20 | `KioskDevice` | `crm:KioskDevice` | `kdev_ID` | 0 | 6 |
| 21 | `ListOption` | `crm:ListOption` | `lst_OptionID` | 0 | 2 |
| 22 | `Location` | `crm:Location` | `location_id` | 0 | 10 |
| 23 | `MenuLink` | `crm:MenuLink` | `linkId` | 0 | 3 |
| 24 | `Note` | `crm:Note` | `nte_ID` | 0 | 9 |
| 25 | `Person` | `crm:Person` | `per_ID` | 0 | 34 |
| 26 | `PersonCustom` | `crm:PersonCustom` | `per_ID` | 0 | 0 |
| 27 | `PersonCustomMaster` | `crm:PersonCustomMaster` | `custom_Field` | 0 | 5 |
| 28 | `PersonGroupRole` | `crm:PersonGroupRole` | `p2g2r_grp_ID` | 0 | 1 |
| 29 | `PersonVolunteerOpportunity` | `crm:PersonVolunteerOpportunity` | `p2vo_ID` | 0 | 2 |
| 30 | `Pledge` | `crm:Pledge` | `plg_plgID` | 0 | 20 |
| 31 | `PredefinedReports` | `crm:PredefinedReports` | `qry_ID` | 0 | 4 |
| 32 | `Property` | `crm:Property` | `pro_ID` | 0 | 5 |
| 33 | `PropertyType` | `crm:PropertyType` | `prt_ID` | 0 | 3 |
| 34 | `QueryParameterOptions` | `crm:QueryParameterOptions` | `qpo_ID` | 0 | 3 |
| 35 | `QueryParameters` | `crm:QueryParameters` | `qrp_ID` | 0 | 14 |
| 36 | `RecordProperty` | `crm:RecordProperty` | `r2p_record_ID` | 0 | 1 |
| 37 | `Token` | `crm:Token` | `token` | 0 | 4 |
| 38 | `User` | `crm:User` | `usr_per_ID` | 0 | 33 |
| 39 | `UserConfig` | `crm:UserConfig` | `ucfg_id` | 0 | 6 |
| 40 | `UserSetting` | `crm:UserSetting` | `setting_name` | 0 | 1 |
| 41 | `Version` | `crm:Version` | `ver_ID` | 0 | 3 |
| 42 | `VolunteerOpportunity` | `crm:VolunteerOpportunity` | `vol_ID` | 0 | 4 |
| 43 | `WhyCame` | `crm:WhyCame` | `why_ID` | 0 | 5 |

---

## 5. 对象属性（Object Properties）

从外键关系和业务语义推导的 33 个 ObjectProperty：

| # | 属性 URI | Domain | Range | 说明 |
|---|----------|--------|-------|------|
| 1 | `crm:assignedToEvent` | `crm:KioskAssignment` | `crm:Event` | FK:`kasm_EventId` from `KioskAssignment` |
| 2 | `crm:atLocation` | `crm:Event` | `crm:Location` | FK:`location_id` from `Event` |
| 3 | `crm:attendsEvent` | `crm:Person` | `crm:Event` | FK:`person_id` from `Person` |
| 4 | `crm:belongsToFamily` | `crm:Person` | `crm:Family` | FK:`per_fam_ID` from `Person` |
| 5 | `crm:buyerOfItem` | `crm:Person` | `crm:DonatedItem` | FK:`di_buyer_ID` from `Person` |
| 6 | `crm:calendarOfEvent` | `crm:Event` | `crm:Calendar` | FK:`event_id` from `Event` |
| 7 | `crm:depositOfFamily` | `crm:Deposit` | `crm:Family` | FK:`dep_FamID` from `Deposit` |
| 8 | `crm:donorOfItem` | `crm:Person` | `crm:DonatedItem` | FK:`di_donor_ID` from `Person` |
| 9 | `crm:eventInAudience` | `crm:Group` | `crm:Event` | FK:`group_id` from `Group` |
| 10 | `crm:eventOnCalendar` | `crm:Calendar` | `crm:Event` | FK:`calendar_id` from `Calendar` |
| 11 | `crm:familyHasNote` | `crm:Family` | `crm:Note` | FK:`nte_fam_ID` from `Family` |
| 12 | `crm:fundedByFund` | `crm:Pledge` | `crm:DonationFund` | FK:`plg_fundID` from `Pledge` |
| 13 | `crm:hasAudienceGroup` | `crm:Event` | `crm:Group` | FK:`event_id` from `Event` |
| 14 | `crm:hasDepositSlip` | `crm:Deposit` | `crm:Pledge` | FK:`plg_depID` from `Deposit` |
| 15 | `crm:hasDonatedItem` | `crm:FundRaiser` | `crm:DonatedItem` | FK:`di_FR_ID` from `FundRaiser` |
| 16 | `crm:hasEventAttendee` | `crm:Event` | `crm:Person` | FK:`event_id` from `Event` |
| 17 | `crm:hasFY` | `crm:Pledge` | `crm:Family` | FK:`plg_FamID` from `Pledge` |
| 18 | `crm:hasFamilyMember` | `crm:Family` | `crm:Person` | FK:`fam_ID` from `Family` |
| 19 | `crm:hasFamilyPledge` | `crm:Family` | `crm:Pledge` | FK:`plg_FamID` from `Family` |
| 20 | `crm:hasGroupMember` | `crm:Group` | `crm:Person` | FK:`p2g2r_grp_ID` from `Group` |
| 21 | `crm:hasKioskDevice` | `crm:KioskAssignment` | `crm:KioskDevice` | FK:`kasm_kdevId` from `KioskAssignment` |
| 22 | `crm:hasNote` | `crm:Person` | `crm:Note` | FK:`nte_per_ID` from `Person` |
| 23 | `crm:hasPledge` | `crm:Person` | `crm:Pledge` | FK:`plg_PerID` from `Person` |
| 24 | `crm:hasRecordProperty` | `crm:RecordProperty` | `crm:Property` | FK:`r2p_pro_ID` from `RecordProperty` |
| 25 | `crm:hasVolunteerOp` | `crm:Person` | `crm:VolunteerOpportunity` | FK:`p2vo_per_ID` from `Person` |
| 26 | `crm:linkedToPerson` | `crm:User` | `crm:Person` | FK:`usr_per_ID` from `User` |
| 27 | `crm:memberOfGroup` | `crm:Person` | `crm:Group` | FK:`p2g2r_per_ID` from `Person` |
| 28 | `crm:noteAboutFamily` | `crm:Note` | `crm:Family` | FK:`nte_fam_ID` from `Note` |
| 29 | `crm:noteAboutPerson` | `crm:Note` | `crm:Person` | FK:`nte_per_ID` from `Note` |
| 30 | `crm:primaryContact` | `crm:Event` | `crm:Person` | FK:`primary_contact_person_id` from `Event` |
| 31 | `crm:propertyForRecord` | `crm:Property` | `crm:RecordProperty` | FK:`pro_ID` from `Property` |
| 32 | `crm:secondaryContact` | `crm:Event` | `crm:Person` | FK:`secondary_contact_person_id` from `Event` |
| 33 | `crm:whyCameForPerson` | `crm:WhyCame` | `crm:Person` | FK:`why_per_ID` from `WhyCame` |

---

## 6. 数据类型属性（Datatype Properties）

按类分组的 DatatypeProperty 清单（329 个）：

### crm:Calendar  (5 properties)

| `accesstoken?` | `xsd:string` |
| `backgroundcolor?` | `xsd:string` |
| `foregroundcolor?` | `xsd:string` |
| `id` | `xsd:integer` |
| `name` | `xsd:string` |

### crm:CalendarEvent  (1 properties)

| `id` | `xsd:integer` |

### crm:Config  (3 properties)

| `cfgId` | `xsd:integer` |
| `cfgName` | `xsd:string` |
| `cfgValue?` | `xsd:string` |

### crm:Deposit  (6 properties)

| `closed` | `xsd:boolean` |
| `comment?` | `xsd:string` |
| `date?` | `xsd:date` |
| `enteredby?` | `xsd:integer` |
| `id` | `xsd:integer` |
| `type` | `xsd:string` |

### crm:DonatedItem  (15 properties)

| `buyerId` | `xsd:integer` |
| `description?` | `xsd:string` |
| `donorId` | `xsd:integer` |
| `enteredby` | `xsd:integer` |
| `entereddate` | `xsd:date` |
| `estprice?` | `xsd:decimal` |
| `frId` | `xsd:integer` |
| `id` | `xsd:integer` |
| `item` | `xsd:string` |
| `materialvalue?` | `xsd:decimal` |
| `minimum?` | `xsd:decimal` |
| `multibuy` | `xsd:integer` |
| `picture?` | `xsd:string` |
| `sellprice?` | `xsd:decimal` |
| `title` | `xsd:string` |

### crm:DonationFund  (5 properties)

| `active` | `xsd:string` |
| `description?` | `xsd:string` |
| `id` | `xsd:integer` |
| `name?` | `xsd:string` |
| `order` | `xsd:integer` |

### crm:Event  (12 properties)

| `desc?` | `xsd:string` |
| `end` | `xsd:dateTime` |
| `id` | `xsd:integer` |
| `inactive` | `xsd:integer` |
| `locationId` | `xsd:integer` |
| `primaryContactPersonId` | `xsd:integer` |
| `secondaryContactPersonId` | `xsd:integer` |
| `start` | `xsd:dateTime` |
| `text?` | `xsd:string` |
| `title` | `xsd:string` |
| `type` | `xsd:integer` |
| `url?` | `xsd:string` |

### crm:EventAttend  (7 properties)

| `attendId` | `xsd:integer` |
| `checkinDate?` | `xsd:dateTime` |
| `checkinId?` | `xsd:integer` |
| `checkoutDate?` | `xsd:dateTime` |
| `checkoutId?` | `xsd:integer` |
| `id` | `xsd:integer` |
| `personId` | `xsd:integer` |

### crm:EventAudience  (1 properties)

| `groupId` | `xsd:integer` |

### crm:EventCountName  (3 properties)

| `countid` | `xsd:integer` |
| `countname` | `xsd:string` |
| `eventtypeid` | `xsd:integer` |

### crm:EventCounts  (4 properties)

| `countcount?` | `xsd:integer` |
| `countid` | `xsd:integer` |
| `countname?` | `xsd:string` |
| `notes?` | `xsd:string` |

### crm:EventType  (9 properties)

| `typeActive` | `xsd:integer` |
| `typeDefrecurdom` | `xsd:string` |
| `typeDefrecurdow` | `xsd:string` |
| `typeDefrecurdoy` | `xsd:date` |
| `typeDefrecurtype` | `xsd:string` |
| `typeDefstarttime` | `xsd:dateTime` |
| `typeGrpid?` | `xsd:integer` |
| `typeId` | `xsd:integer` |
| `typeName` | `xsd:string` |

### crm:Family  (22 properties)

| `address1?` | `xsd:string` |
| `address2?` | `xsd:string` |
| `city?` | `xsd:string` |
| `country?` | `xsd:string` |
| `datedeactivated?` | `xsd:date` |
| `dateentered` | `xsd:dateTime` |
| `datelastedited?` | `xsd:dateTime` |
| `editedby?` | `xsd:integer` |
| `email?` | `xsd:string` |
| `enteredby` | `xsd:integer` |
| `envelope` | `xsd:integer` |
| `homephone?` | `xsd:string` |
| `id` | `xsd:integer` |
| `latitude?` | `xsd:decimal` |
| `longitude?` | `xsd:decimal` |
| `name?` | `xsd:string` |
| `scancheck?` | `xsd:string` |
| `scancredit?` | `xsd:string` |
| `sendnewsletter` | `xsd:string` |
| `state?` | `xsd:string` |
| `weddingdate?` | `xsd:date` |
| `zip?` | `xsd:string` |

### crm:FamilyCustom  (1 properties)

| `id` | `xsd:integer` |

### crm:FamilyCustomMaster  (6 properties)

| `customField` | `xsd:integer` |
| `customFieldsec` | `xsd:integer` |
| `customName` | `xsd:string` |
| `customOrder` | `xsd:integer` |
| `customSpecial?` | `xsd:integer` |
| `typeId` | `xsd:integer` |

### crm:FundRaiser  (6 properties)

| `date?` | `xsd:date` |
| `description?` | `xsd:string` |
| `enteredby` | `xsd:integer` |
| `entereddate` | `xsd:date` |
| `id` | `xsd:integer` |
| `title` | `xsd:string` |

### crm:Group  (9 properties)

| `active` | `xsd:boolean` |
| `defaultrole` | `xsd:integer` |
| `description?` | `xsd:string` |
| `hasspecialprops?` | `xsd:boolean` |
| `id` | `xsd:integer` |
| `includeEmailExport` | `xsd:boolean` |
| `name` | `xsd:string` |
| `rolelistid` | `xsd:integer` |
| `type` | `xsd:integer` |

### crm:GroupPropMaster  (8 properties)

| `id` | `xsd:integer` |
| `propDescription?` | `xsd:string` |
| `propField` | `xsd:string` |
| `propId` | `xsd:integer` |
| `propName?` | `xsd:string` |
| `propPersondisplay` | `xsd:string` |
| `propSpecial?` | `xsd:integer` |
| `typeId` | `xsd:integer` |

### crm:KioskAssignment  (4 properties)

| `assignmenttype?` | `xsd:integer` |
| `eventid?` | `xsd:integer` |
| `id` | `xsd:integer` |
| `kdevid?` | `xsd:integer` |

### crm:KioskDevice  (7 properties)

| `accepted?` | `xsd:boolean` |
| `devicetype?` | `xsd:string` |
| `guidhash?` | `xsd:string` |
| `id` | `xsd:integer` |
| `lastheartbeat?` | `xsd:string` |
| `name?` | `xsd:string` |
| `pendingcommands?` | `xsd:string` |

### crm:ListOption  (3 properties)

| `lstOptionid` | `xsd:integer` |
| `lstOptionname` | `xsd:string` |
| `lstOptionsequence` | `xsd:integer` |

### crm:Location  (11 properties)

| `locationAddress` | `xsd:string` |
| `locationCity` | `xsd:string` |
| `locationCountry` | `xsd:string` |
| `locationEmail` | `xsd:string` |
| `locationId` | `xsd:integer` |
| `locationName` | `xsd:string` |
| `locationPhone` | `xsd:string` |
| `locationState` | `xsd:string` |
| `locationTimzezone` | `xsd:string` |
| `locationTypeid` | `xsd:integer` |
| `locationZip` | `xsd:string` |

### crm:MenuLink  (4 properties)

| `linkid` | `xsd:integer` |
| `linkname?` | `xsd:string` |
| `linkorder?` | `xsd:integer` |
| `linkuri?` | `xsd:string` |

### crm:Note  (10 properties)

| `dateentered` | `xsd:dateTime` |
| `datelastedited?` | `xsd:dateTime` |
| `editedby` | `xsd:integer` |
| `enteredby` | `xsd:integer` |
| `famId` | `xsd:integer` |
| `id` | `xsd:integer` |
| `perId` | `xsd:integer` |
| `private` | `xsd:integer` |
| `text?` | `xsd:string` |
| `type?` | `xsd:string` |

### crm:Person  (35 properties)

| `address1?` | `xsd:string` |
| `address2?` | `xsd:string` |
| `birthday` | `xsd:integer` |
| `birthmonth` | `xsd:integer` |
| `birthyear?` | `xsd:integer` |
| `cellphone?` | `xsd:string` |
| `city?` | `xsd:string` |
| `clsId` | `xsd:integer` |
| `country?` | `xsd:string` |
| `dateentered` | `xsd:dateTime` |
| `datelastedited?` | `xsd:dateTime` |
| `editedby?` | `xsd:integer` |
| `email?` | `xsd:string` |
| `enteredby` | `xsd:integer` |
| `envelope?` | `xsd:integer` |
| `facebook?` | `xsd:string` |
| `famId` | `xsd:integer` |
| `firstname?` | `xsd:string` |
| `flags` | `xsd:integer` |
| `fmrId` | `xsd:integer` |
| `frienddate?` | `xsd:date` |
| `gender` | `xsd:integer` |
| `homephone?` | `xsd:string` |
| `id` | `xsd:integer` |
| `lastname?` | `xsd:string` |
| `linkedin?` | `xsd:string` |
| `membershipdate?` | `xsd:date` |
| `middlename?` | `xsd:string` |
| `state?` | `xsd:string` |
| `suffix?` | `xsd:string` |
| `title?` | `xsd:string` |
| `twitter?` | `xsd:string` |
| `workemail?` | `xsd:string` |
| `workphone?` | `xsd:string` |
| `zip?` | `xsd:string` |

### crm:PersonCustom  (1 properties)

| `id` | `xsd:integer` |

### crm:PersonCustomMaster  (6 properties)

| `customField` | `xsd:integer` |
| `customFieldsec` | `xsd:integer` |
| `customName` | `xsd:string` |
| `customOrder` | `xsd:integer` |
| `customSpecial?` | `xsd:integer` |
| `typeId` | `xsd:integer` |

### crm:PersonGroupRole  (2 properties)

| `p2g2rGrpId` | `xsd:integer` |
| `p2g2rRleId` | `xsd:integer` |

### crm:PersonVolunteerOpportunity  (3 properties)

| `p2voId` | `xsd:integer` |
| `p2voPerId?` | `xsd:integer` |
| `p2voVolId?` | `xsd:integer` |

### crm:Pledge  (21 properties)

| `amount?` | `xsd:decimal` |
| `autCleared` | `xsd:boolean` |
| `autId` | `xsd:integer` |
| `autResultid` | `xsd:integer` |
| `checkno?` | `xsd:integer` |
| `comment?` | `xsd:string` |
| `date?` | `xsd:date` |
| `datelastedited` | `xsd:date` |
| `depid?` | `xsd:integer` |
| `editedby` | `xsd:integer` |
| `famid?` | `xsd:integer` |
| `fundid?` | `xsd:integer` |
| `fyid?` | `xsd:integer` |
| `groupkey` | `xsd:string` |
| `method?` | `xsd:string` |
| `nondeductible` | `xsd:decimal` |
| `pledgeorpayment` | `xsd:string` |
| `plgid` | `xsd:integer` |
| `problem?` | `xsd:boolean` |
| `scanstring?` | `xsd:string` |
| `schedule?` | `xsd:string` |

### crm:PredefinedReports  (5 properties)

| `qryCount` | `xsd:boolean` |
| `qryDescription` | `xsd:string` |
| `qryId` | `xsd:integer` |
| `qryName` | `xsd:string` |
| `qrySql` | `xsd:string` |

### crm:Property  (6 properties)

| `proClass` | `xsd:string` |
| `proDescription` | `xsd:string` |
| `proId` | `xsd:integer` |
| `proName` | `xsd:string` |
| `proPrompt?` | `xsd:string` |
| `proPrtId` | `xsd:integer` |

### crm:PropertyType  (4 properties)

| `prtClass` | `xsd:string` |
| `prtDescription` | `xsd:string` |
| `prtId` | `xsd:integer` |
| `prtName` | `xsd:string` |

### crm:QueryParameterOptions  (4 properties)

| `display` | `xsd:string` |
| `id` | `xsd:integer` |
| `qrpId` | `xsd:integer` |
| `value` | `xsd:string` |

### crm:QueryParameters  (15 properties)

| `alias?` | `xsd:string` |
| `alphamaxlength?` | `xsd:integer` |
| `alphaminlength?` | `xsd:integer` |
| `default?` | `xsd:string` |
| `description?` | `xsd:string` |
| `id` | `xsd:integer` |
| `inputboxsize` | `xsd:integer` |
| `name?` | `xsd:string` |
| `numericmax?` | `xsd:integer` |
| `numericmin?` | `xsd:integer` |
| `optionsql?` | `xsd:string` |
| `qryId` | `xsd:integer` |
| `required` | `xsd:integer` |
| `type` | `xsd:integer` |
| `validation` | `xsd:string` |

### crm:RecordProperty  (2 properties)

| `recordId` | `xsd:integer` |
| `value` | `xsd:string` |

### crm:Token  (5 properties)

| `referenceId?` | `xsd:integer` |
| `remaininguses?` | `xsd:integer` |
| `token` | `xsd:integer` |
| `type` | `xsd:string` |
| `validUntilDate?` | `xsd:date` |

### crm:User  (34 properties)

| `addrecords` | `xsd:boolean` |
| `admin` | `xsd:boolean` |
| `apikey?` | `xsd:string` |
| `calend?` | `xsd:date` |
| `calnoschool1?` | `xsd:date` |
| `calnoschool2?` | `xsd:date` |
| `calnoschool3?` | `xsd:date` |
| `calnoschool4?` | `xsd:date` |
| `calnoschool5?` | `xsd:date` |
| `calnoschool6?` | `xsd:date` |
| `calnoschool7?` | `xsd:date` |
| `calnoschool8?` | `xsd:date` |
| `calstart?` | `xsd:date` |
| `currentdeposit` | `xsd:integer` |
| `defaultfy` | `xsd:integer` |
| `deleterecords` | `xsd:boolean` |
| `editrecords` | `xsd:boolean` |
| `editself` | `xsd:boolean` |
| `failedlogins` | `xsd:integer` |
| `finance` | `xsd:boolean` |
| `lastlogin` | `xsd:dateTime` |
| `logincount` | `xsd:integer` |
| `managegroups` | `xsd:boolean` |
| `menuoptions` | `xsd:boolean` |
| `needpasswordchange` | `xsd:boolean` |
| `notes` | `xsd:boolean` |
| `password` | `xsd:string` |
| `perId` | `xsd:integer` |
| `searchfamily?` | `xsd:integer` |
| `style?` | `xsd:string` |
| `twofactorauthlastkeytimestamp?` | `xsd:integer` |
| `twofactorauthrecoverycodes?` | `xsd:string` |
| `twofactorauthsecret?` | `xsd:string` |
| `username` | `xsd:string` |

### crm:UserConfig  (7 properties)

| `cat` | `xsd:string` |
| `id` | `xsd:integer` |
| `name` | `xsd:string` |
| `permission` | `xsd:string` |
| `tooltip` | `xsd:string` |
| `type` | `xsd:string` |
| `value?` | `xsd:string` |

### crm:UserSetting  (2 properties)

| `settingName` | `xsd:integer` |
| `settingValue?` | `xsd:string` |

### crm:Version  (4 properties)

| `verId` | `xsd:integer` |
| `verUpdateEnd?` | `xsd:dateTime` |
| `verUpdateStart?` | `xsd:dateTime` |
| `verVersion` | `xsd:string` |

### crm:VolunteerOpportunity  (5 properties)

| `active` | `xsd:string` |
| `description?` | `xsd:string` |
| `id` | `xsd:integer` |
| `name?` | `xsd:string` |
| `order` | `xsd:integer` |

### crm:WhyCame  (6 properties)

| `come` | `xsd:string` |
| `hearofus` | `xsd:string` |
| `id` | `xsd:integer` |
| `join` | `xsd:string` |
| `perId` | `xsd:integer` |
| `suggest` | `xsd:string` |

---

## 7. 关键语义关系

### 7.1 人员-家庭（多对一）
```
crm:Person  ──crm:belongsToFamily──►  crm:Family
crm:Family  ──crm:hasFamilyMember───►  crm:Person  (inverse)
```
外键: `Person.per_fam_ID → Family.fam_ID`

### 7.2 人员-群组（多对多）
```
crm:Person  ──crm:memberOfGroup──►  crm:Group
crm:Group   ──crm:hasGroupMember──►  crm:Person  (inverse)
```
桥接表: `PersonGroupRole` (per_ID, grp_ID, rle_ID)

### 7.3 人员-活动（多对多）
```
crm:Person  ──crm:attendsEvent──►  crm:Event
crm:Event   ──crm:hasEventAttendee──►  crm:Person  (inverse)
```
桥接表: `EventAttend` (person_id, event_id, checkin_date, checkout_date)

### 7.4 活动-群组（活动面向群组）
```
crm:Event  ──crm:hasAudienceGroup──►  crm:Group
crm:Group  ──crm:eventInAudience──►  crm:Event  (inverse)
```
桥接表: `EventAudience` (event_id, group_id)

### 7.5 活动-日历
```
crm:Calendar  ──crm:eventOnCalendar──►  crm:Event
crm:Event     ──crm:calendarOfEvent──►  crm:Calendar  (inverse)
```
桥接表: `CalendarEvent` (calendar_id, event_id)

### 7.6 人员-捐款承诺
```
crm:Person  ──crm:hasPledge──►  crm:Pledge
crm:Family  ──crm:hasFamilyPledge──►  crm:Pledge
crm:Pledge  ──crm:fundedByFund──►  crm:DonationFund
```

### 7.7 人员-用户
```
crm:User  ──crm:linkedToPerson──►  crm:Person
```
外键: `User.usr_per_ID → Person.per_ID`

### 7.8 人员/家庭-笔记
```
crm:Person  ──crm:noteAboutPerson──►  crm:Note
crm:Family  ──crm:noteAboutFamily──►  crm:Note
```
外键: `Note.nte_per_ID → Person.per_ID`, `Note.nte_fam_ID → Family.fam_ID`

### 7.9 活动-位置/联系人
```
crm:Event  ──crm:atLocation──►  crm:Location
crm:Event  ──crm:primaryContact──►  crm:Person
crm:Event  ──crm:secondaryContact──►  crm:Person
```

---

## 8. SQL → XSD 类型映射

| SQL 类型 | XSD 类型 | 说明 |
|---------|---------|------|
| VARCHAR, TEXT, CHAR, LONGVARCHAR | xsd:string | 字符串 |
| TINYINT, SMALLINT, INT, BIGINT | xsd:integer | 整数 |
| DECIMAL, DOUBLE, FLOAT | xsd:decimal | 小数 |
| DATE | xsd:date | 日期（YYYY-MM-DD） |
| DATETIME, TIMESTAMP | xsd:dateTime | 日期时间（ISO 8601） |
| BOOLEAN | xsd:boolean | 布尔值 |

---

## 9. 命名规范

| 元素类型 | 命名格式 | 示例 |
|---------|---------|------|
| Class | PascalCase + crm: 前缀 | `crm:Person`, `crm:EventAttend` |
| ObjectProperty | camelCase + crm: 前缀 | `crm:belongsToFamily`, `crm:attendsEvent` |
| DatatypeProperty | camelCase + crm: 前缀 | `crm:firstName`, `crm:eventTitle` |
| Named Individual | PascalCase | `crm:Role_Admin` |

---

## 10. SPARQL 查询示例

```sparql
PREFIX crm: <http://churchcrm.org/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

# 查询某个家庭的所有成员姓名
SELECT ?person ?firstName ?lastName ?email
WHERE {
    ?person  rdf:type        crm:Person .
    ?person  crm:firstName   ?firstName .
    ?person  crm:lastName    ?lastName .
    ?person  crm:email       ?email .
    ?person  crm:belongsToFamily ?family .
    ?family  crm:familyName  "Smith" .
}

# 查询某活动的所有参与人员
SELECT ?person ?firstName ?lastName ?checkinDate
WHERE {
    ?event   rdf:type         crm:Event .
    ?event   crm:eventTitle   "主日崇拜" .
    ?event   crm:hasEventAttendee ?person .
    ?person  crm:firstName   ?firstName .
    ?person  crm:lastName    ?lastName .
    ?attend  rdf:type        crm:EventAttend .
    ?attend  crm:personId    ?person .
    ?attend  crm:eventId     ?event .
    ?attend  crm:checkinDate ?checkinDate .
}

# 查询所有捐款超过1000元的捐款人
SELECT ?person ?firstName ?lastName ?amount
WHERE {
    ?pledge  rdf:type    crm:Pledge .
    ?pledge  crm:amount  ?amount .
    FILTER(?amount > 1000) .
    ?pledge  crm:hasPledge ?person .
    ?person  crm:firstName ?firstName .
    ?person  crm:lastName  ?lastName .
}
```

---

## 11. 文件清单

| 文件 | 说明 |
|------|------|
| `crm_ontology.ttl` | 完整 RDF/Turtle 本体（43 类，33 对象属性，329 数据属性） |
| `crm_ontology_context.json` | JSON-LD @context 文件，可直接用于 JSON-LD 数据序列化 |
| `docs/ONTOLOGY_DESIGN.md` | 本设计文档 |

---

*本文档由 ChurchCRM ER 图自动生成 (generate_ontology.py, 2026-04-05)*
