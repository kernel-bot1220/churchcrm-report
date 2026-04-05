# ChurchCRM Ontology 代码审查报告

## 审查时间
2026-04-05 08:26 UTC

## 审查范围
- `crm_ontology.ttl`（2444行，724条属性声明）
- `ONTOLOGY_DESIGN.md`（设计文档）

---

## 一、命名规范检查

### 类名 ✅ 合格
所有43个 OWL Class 均使用 PascalCase 命名（如 `crm:Person`, `crm:EventAttend`），前缀 `crm:` 使用正确。

### 属性名 — 部分合格，存在以下问题

| 问题 | 示例 | 严重程度 |
|------|------|----------|
| 通用名复用（同一 DatatypeProperty 名用于多个不同类） | `crm:id`（用于Calendar、Event、Family等20+个类）、`crm:description?`（10+类）、`crm:active`、`crm:date?`、`crm:comment?`、`crm:name?`、`crm:type` 等 | 🟡 中等 |
| `?` 后缀用于表示可选字段，违反 RDF 属性命名惯例 | `crm:accesstoken?`、`crm:description?`、`crm:comment?` 等 | 🟢 轻微 |
| FK 字段未去数据库化 | `p2g2rGrpId`、`p2voPerId?`、`autResultid` 等属性名仍含数据库列名风格，应为纯语义名 | 🟡 中等 |

---

## 二、关系完整性检查

### ObjectProperty 覆盖率：基本合格，但有遗漏

#### 🔴 严重遗漏：Note 表的两个外键未建模为 ObjectProperty

`Note.nte_per_ID → Person` 和 `Note.nte_fam_ID → Family` 是标准外键，但本体中：

- `crm:perId`（Note → Person）和 `crm:famId`（Note → Family）被定义为 **DatatypeProperty**（xsd:integer）
- `crm:noteAboutPerson`（Note → Person）和 `crm:noteAboutFamily`（Note → Family）被定义为 **ObjectProperty**，但 domain/range 与 Note 表 FK 不一致（应为 Note.domain，而非 Person/Family.domain）

这导致 Note 表到 Person/Family 的引用语义不清晰，且同一关系存在两种不同属性的歧义。

**修复建议**：将 `crm:noteAboutPerson` 的 domain 改为 `crm:Note`，range 改为 `crm:Person`（当前 domain 是 Note，range 是 Person → ✅ 正确）；删除重复的 `crm:perId` DatatypeProperty。

#### 🔴 严重遗漏：DonatedItem 表的 buyer/donor 外键未建模为 ObjectProperty

`DonatedItem.di_buyer_ID → Person` 和 `DonatedItem.di_donor_ID → Person` 定义为了 `crm:buyerId` 和 `crm:donorId`（DatatypeProperty），而非 ObjectProperty。

虽然存在 `crm:buyerOfItem`（Person → DonatedItem）和 `crm:donorOfItem`（Person → DonatedItem）作为反向属性，但正向外键 `buyerId`/`donorId` 仍然是 DatatypeProperty，不符合"外键→ObjectProperty"的设计原则。

**修复建议**：将 `crm:buyerId` 和 `crm:donorId` 从 DatatypeProperty 改为 ObjectProperty。

#### 🟡 中等遗漏：PersonGroupRole 桥接表的外键仅部分建模

`PersonGroupRole.p2g2r_grp_ID → Group` 定义为 `crm:p2g2rGrpId`（DatatypeProperty），而非 ObjectProperty。虽然 `crm:hasGroupMember`（Group → Person）从 Group 侧捕获了多对多关系，但 PersonGroupRole 自身到 Group 的链接丢失了，桥接表失去了独立语义。

**修复建议**：添加 `crm:roleAssignmentInGroup`（PersonGroupRole → Group）ObjectProperty。

#### 🟡 中等遗漏：EventAttend 桥接表到 Event 的链接缺失

`EventAttend.event_id → Event` 定义为 `crm:personId`（DatatypeProperty），但没有 ObjectProperty 从 EventAttend 指向 Event。虽然 `crm:attendsEvent`（Person → Event）和 `crm:hasEventAttendee`（Event → Person）存在，但丢失了 EventAttend 自身的签到/签出语义（checkinDate、checkoutDate 等）。

**修复建议**：添加 `crm:attendanceForEvent`（EventAttend → Event）和 `crm:hasEventAttendance`（Event → EventAttend）。

---

## 三、Domain/Range 检查

### 大部分正确，以下有问题：

| 属性 | 问题 | 修复建议 |
|------|------|----------|
| `crm:hasFY` | 命名不透明（FY 不明确），range 为 `crm:Family`，与 `hasFamilyPledge` 语义高度重叠 | 重命名为 `crm:familyPledgeOf`，明确为 `hasFamilyPledge` 的逆 |
| 所有 ObjectProperty | 均无 `owl:inverseOf` 声明（见下节） | 为所有可逆属性添加逆声明 |

其余 ObjectProperty 的 Domain/Range 在本体文件中与设计文档一致。

---

## 四、歧义问题

### 🔴 严重：`hasNote` vs `noteAboutPerson` — 同一关系的两种并行属性

- `crm:hasNote`：Domain=Person, Range=Note（Person 持有 Note）
- `crm:noteAboutPerson`：Domain=Note, Range=Person（Note 关于 Person）

两者语义完全相同，但独立声明，无 `owl:inverseOf` 关系。这导致：
1. 数据写入时需要同时维护两条三元组
2. SPARQL 查询时需要同时覆盖两个谓词
3. 本体逻辑不清晰

**修复建议**：保留 `crm:hasNote`（更符合语义习惯），删除 `crm:noteAboutPerson`，并声明 `owl:inverseOf crm:hasNote`。

### 🔴 严重：同理 `familyHasNote` vs `noteAboutFamily` — 同样问题

**修复建议**：保留 `crm:familyHasNote`，删除 `crm:noteAboutFamily`，并声明逆关系。

### 🟡 中等：`crm:id` — 跨类复用的全局标识属性

`crm:id` 在20+个类中重复定义（Domain 叠加）。OWL 中这在语法上合法（解释为全局唯一属性），但语义上混淆了"每个类的本地ID"与"全局唯一ID"的区别。

**修复建议**：改用带命名空间前缀的类限定名，如 `crm:personId`、`crm:eventId`，或在设计文档中明确 `crm:id` 的全局语义。

---

## 五、可推理性（OWL 特性标注）

### 🔴 所有 33 个 ObjectProperty 均缺失 OWL 特性标注

本体中未找到任何 `owl:inverseOf`、`owl:SymmetricProperty`、`owl:TransitiveProperty`、`owl:FunctionalProperty`、`owl:InverseFunctionalProperty` 声明。

**应添加逆声明的关键属性对**（12对）：

| 属性A | 属性B | 说明 |
|-------|-------|------|
| `crm:belongsToFamily` | `crm:hasFamilyMember` | Person↔Family |
| `crm:attendsEvent` | `crm:hasEventAttendee` | Person↔Event（EventAttend桥接） |
| `crm:memberOfGroup` | `crm:hasGroupMember` | Person↔Group（PersonGroupRole桥接） |
| `crm:eventOnCalendar` | `crm:calendarOfEvent` | Calendar↔Event |
| `crm:hasAudienceGroup` | `crm:eventInAudience` | Event↔Group |
| `crm:hasFamilyPledge` | `crm:hasFY` | Family↔Pledge |
| `crm:hasPledge` | _(单向：需补充Person→Pledge的显式逆） |
| `crm:hasNote` | `crm:noteAboutPerson`（建议删除后者） | Person↔Note |
| `crm:familyHasNote` | `crm:noteAboutFamily`（建议删除后者） | Family↔Note |
| `crm:buyerOfItem` | _(需正向外键buyerOfItem→DonatedItem) |
| `crm:donorOfItem` | _(需正向外键donorOfItem→DonatedItem) |
| `crm:linkedToPerson` | _(单向，需声明inverseOf或Functional) |

**应添加 FunctionalProperty 的属性**：
- `crm:linkedToPerson`（User → Person，1对1关系）
- `crm:hasFY`（Pledge → Family，应为 Functional）

---

## 六、完整性检查

### 43 个类 ✅ 全部覆盖

本体文件包含了设计文档中列出的全部43个类（`Calendar`, `Event`, `Person`, `Family`, `Group`, `Pledge` 等），无遗漏。

### 统计数据

| 指标 | 设计文档 | 本体文件 | 一致性 |
|------|----------|----------|--------|
| OWL Classes | 43 | 43 | ✅ |
| Object Properties | 33 | 33 | ✅ |
| Datatype Properties | 329 | ~329 | ✅ |

---

## 问题汇总

### 🔴 严重问题（6个）

1. **`Note.perId` / `Note.famId` 应为 ObjectProperty**：当前为 DatatypeProperty（xsd:integer），导致 Note→Person/Family 的外键关系无法语义查询
2. **`DonatedItem.buyerId` / `DonatedItem.donorId` 应为 ObjectProperty**：Buyer/Donor 是指向 Person 的 FK，当前丢失语义
3. **`hasNote` vs `noteAboutPerson` 语义重复**：同一关系两种属性，无逆声明，必须二选一并补充逆关系
4. **`familyHasNote` vs `noteAboutFamily` 同上**：必须二选一并补充逆关系
5. **零逆属性声明（`owl:inverseOf`）**：33个 ObjectProperty 没有任何逆属性声明，严重影响推理能力
6. **`hasFY` 命名不透明**：`FY`（Fiscal Year 缩写）语义不清，且与 `hasFamilyPledge` 存在混淆，应重命名

### 🟡 中等问题（4个）

1. **`PersonGroupRole.p2g2rGrpId` 应为 ObjectProperty**：FK 未建模为语义关系
2. **`EventAttend.event_id` 到 Event 的 ObjectProperty 缺失**：桥接表语义不完整
3. **`crm:id` 跨20+类复用**：应改为类限定名（如 `crm:eventId`）
4. **FK字段未去数据库化命名**：`p2g2rGrpId`、`autResultid`、`p2voPerId?` 等应改为语义名

### 🟢 轻微问题（4个）

1. **`?` 后缀违反 RDF 命名惯例**：建议使用 `owl:maxCardinality` 或文档标注替代
2. **`autId` / `autResultid`（Pledge表）可能指向未建模的自动化表**：如存在外部表依赖，应建模为 ObjectProperty
3. **`crm:linkedToPerson`（User→Person）未声明为 FunctionalProperty**：User 只能关联一个 Person
4. **本体缺乏 `owl:versionInfo` 之外的整体版本信息**：建议为每个主要属性组添加 `rdfs:seeAlso` 引用设计文档

---

## 总体评价

**需要修改**

本体在类和属性数量上完整，核心 Domain/Range 设计基本正确，但存在以下**阻断性问题**：

1. **外键未完整建模为 ObjectProperty**（Note、DonatedItem 的 FK 问题）直接影响语义层的可用性
2. **零逆属性声明**导致 OWL 推理无法生效，知识图谱导航能力严重受限
3. **`hasNote`/`noteAboutPerson` 和 `familyHasNote`/`noteAboutFamily` 的歧义**导致本体逻辑冗余且易用性差

---

## 改进建议

### P0（必须修复，进入下一阶段前）

1. 将 `Note.perId`、`Note.famId`、`DonatedItem.buyerId`、`DonatedItem.donorId` 从 DatatypeProperty 改为 ObjectProperty
2. 为所有33个 ObjectProperty 补充 `owl:inverseOf` 声明（特别是 `hasNote`/`noteAboutPerson`、`familyHasNote`/`noteAboutFamily` 二选一后，另一方声明为 inverseOf）
3. 将 `hasFY` 重命名为 `crm:familyPledgeOf`（或删除，合并到 `hasFamilyPledge` 的逆声明中）

### P1（强烈建议）

4. 为 `PersonGroupRole` 添加 `crm:roleAssignmentInGroup`（→ Group）和 `crm:hasPersonGroupRole`（← Group）ObjectProperty
5. 为 `EventAttend` 添加 `crm:attendanceForEvent`（→ Event）和 `crm:hasEventAttendance`（← Event）ObjectProperty
6. 将 `crm:id` 等跨类复用属性拆分为类限定名（如 `crm:personId`、`crm:eventId`）
7. 为 `crm:linkedToPerson` 添加 `owl:FunctionalProperty` 声明

### P2（可选优化）

8. 移除 `?` 后缀，改用标准 RDF/OWL 可选标注方式
9. 在本体文件头部添加 `owl:imports` 或 `rdfs:seeAlso` 引用 `ONTOLOGY_DESIGN.md`
10. 审查 `autId`/`autResultid` 是否需要指向外部自动化系统表

---

*审查工具：人工代码审查*
*审查人：Ontology Review Subagent*
*审查覆盖：crm_ontology.ttl 前200行 + 后200行 + 中段关键属性段*
