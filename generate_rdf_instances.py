#!/usr/bin/env python3
"""
ChurchCRM RDF Instance Data Generator
Generates crm_data.ttl and graph.json from ontology definitions.
Usage: python3 generate_rdf_instances.py
Output: crm_data.ttl, graph.json
"""

import json
from datetime import date, datetime

# ─── Namespaces ───────────────────────────────────────────────────────────────
PREFIXES = """\
@prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl:   <http://www.w3.org/2002/07/owl#> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix crm:   <http://churchcrm.org/ontology/> .
@prefix crmres: <http://churchcrm.org/resource/> .
"""

OUT_TTL = "/home/sk/Downloads/ChurchCRM/crm_data.ttl"
OUT_JSON = "/home/sk/Downloads/ChurchCRM/graph.json"

f = open(OUT_TTL, "w", encoding="utf-8")
f.write(PREFIXES + "\n")

def res(entity_type, idx):
    return f"<http://churchcrm.org/resource/{entity_type}_{idx:03d}>"

def dt(val, dtype="string"):
    if dtype == "date":
        return f'"{val}"^^xsd:date'
    elif dtype == "dateTime":
        return f'"{val}"^^xsd:dateTime'
    elif dtype == "boolean":
        return f'"{val}"^^xsd:boolean'
    elif dtype == "integer":
        return f'"{val}"^^xsd:integer'
    elif dtype == "decimal":
        return f'"{val}"^^xsd:decimal'
    else:
        return f'"{val}"@en'

def dp(prop, val, dtype="string"):
    if val is None:
        return None
    return f"    crm:{prop} {dt(val, dtype)} ;"

def op(prop, target):
    return f"    crm:{prop} {target} ;"

def rdf_type(cls):
    return f"    rdf:type crm:{cls} ;"

def emit_entity(f, lines):
    """Write a block, closing with a period."""
    for l in lines:
        if l:
            f.write(l + "\n")
    f.write("    .\n\n")

# ─── CALENDAR ─────────────────────────────────────────────────────────────────
cal_instances = []
cal_data = [
    (1, "Main Church Calendar", "#4A90E2", "#FFFFFF", "church_main_token"),
    (2, "Sunday School Calendar", "#50C878", "#FFFFFF", "sunday_school_token"),
]
for (cid, name, bg, fg, token) in cal_data:
    uri = res("Calendar", cid)
    lines = [
        f"{uri}",
        rdf_type("Calendar"),
        dp("name", name),
        dp("backgroundcolor?", bg),
        dp("foregroundcolor?", fg),
        dp("accesstoken?", token),
        dp("id", cid, "integer"),
    ]
    emit_entity(f, lines)
    cal_instances.append(uri)

# ─── CONFIG ────────────────────────────────────────────────────────────────────
configs = [
    (1, "systype",          "Church",      "integer"),
    (2, "site_address",     "123 Faith Avenue, Springfield", "string"),
    (3, "church_name",      "Grace Community Church",        "string"),
    (4, "church_phone",     "+1-555-0100",                  "string"),
    (5, "church_email",     "info@gracecommunity.org",       "string"),
    (6, "aiga_bulk_mail",   "150",                            "string"),
]
for (cfgid, cfgname, cfgval, dtype) in configs:
    uri = res("Config", cfgid)
    lines = [
        f"{uri}",
        rdf_type("Config"),
        dp("cfgName", cfgname),
        dp("cfgValue?", cfgval, dtype),
        dp("cfgId", cfgid, "integer"),
    ]
    emit_entity(f, lines)

# ─── FAMILY ───────────────────────────────────────────────────────────────────
families = [
    (1, "Thompson Family", "45 Maple Street", None, "Springfield", "IL", "62701", "USA",
     "+1-555-0101", "thompson@email.com", "2015-06-20", "2020-03-15T10:00:00", "TRUE", 101),
    (2, "Williams Family", "78 Oak Avenue", None, "Springfield", "IL", "62702", "USA",
     "+1-555-0102", "williams@email.com", "2012-09-14", "2019-07-22T14:00:00", "TRUE", 102),
    (3, "Chen Family",     "12 Pine Road",  None, "Springfield", "IL", "62703", "USA",
     "+1-555-0103", "chen@email.com",      None,           "2021-01-10T09:00:00", "FALSE",103),
]
fam_instances = []
for fam in families:
    (famid, fname, addr1, addr2, city, state, zipc, country, hphone, email,
     wedding, dateentered, newsletter, envelope) = fam
    uri = res("Family", famid)
    lines = [
        f"{uri}",
        rdf_type("Family"),
        dp("name?", fname),
        dp("address1?", addr1),
        dp("address2?", addr2),
        dp("city?", city),
        dp("state?", state),
        dp("zip?", zipc),
        dp("country?", country),
        dp("homePhone?", hphone),
        dp("email?", email),
        dp("weddingDate?", wedding, "date"),
        dp("dateEntered", dateentered, "dateTime"),
        dp("sendNewsLetter", newsletter, "string"),
        dp("envelope", envelope, "integer"),
    ]
    emit_entity(f, lines)
    fam_instances.append(uri)

# ─── PERSON ────────────────────────────────────────────────────────────────────
persons = [
    (1, "Mr.",   "James",  "Robert", "Thompson", "Jr.",
     "45 Maple Street", None, "Springfield", "IL", "62701", "USA",
     "+1-555-0101", "+1-555-1001", "james.thompson@email.com", None,
     3, 15, 1985, 1, "2020-03-20", "2020-03-15T10:00:00", 1),
    (2, "Mrs.",  "Sarah",  "Elizabeth", "Thompson", None,
     "45 Maple Street", None, "Springfield", "IL", "62701", "USA",
     "+1-555-0101", "+1-555-1002", "sarah.thompson@email.com", None,
     7, 22, 1987, 2, "2020-03-20", "2020-03-15T10:05:00", 1),
    (3, "Mr.",   "Michael","David",   "Williams", None,
     "78 Oak Avenue", None, "Springfield", "IL", "62702", "USA",
     "+1-555-0102", "+1-555-1003", "michael.williams@email.com", None,
     11, 5, 1990, 1, "2019-07-25", "2019-07-22T14:00:00", 1),
    (4, "Mrs.",  "Emily",  "Anne",    "Williams", None,
     "78 Oak Avenue", None, "Springfield", "IL", "62702", "USA",
     "+1-555-0102", "+1-555-1004", "emily.williams@email.com", None,
     2, 14, 1992, 2, "2019-07-25", "2019-07-22T14:10:00", 1),
    (5, "Mr.",   "Wei",    None,      "Chen",     None,
     "12 Pine Road", None, "Springfield", "IL", "62703", "USA",
     "+1-555-0103", "+1-555-1005", "wei.chen@email.com", None,
     8, 30, 1978, 1, "2021-01-15", "2021-01-10T09:00:00", 1),
    (6, "Mrs.",  "Lin",    None,      "Chen",     None,
     "12 Pine Road", None, "Springfield", "IL", "62703", "USA",
     "+1-555-0103", "+1-555-1006", "lin.chen@email.com", None,
     5, 12, 1980, 2, "2021-01-15", "2021-01-10T09:05:00", 1),
]
per_instances = []
for p in persons:
    (pid, title, first, middle, last, suffix, addr1, addr2, city, state, zipc,
     country, hphone, cphone, email, wemail, bmonth, bday, byear, gender,
     memberdate, dateentered, enteredby) = p
    uri = res("Person", pid)
    lines = [
        f"{uri}",
        rdf_type("Person"),
        dp("title?", title),
        dp("firstName?", first),
        dp("middleName?", middle),
        dp("lastName?", last),
        dp("suffix?", suffix),
        dp("address1?", addr1),
        dp("address2?", addr2),
        dp("city?", city),
        dp("state?", state),
        dp("zip?", zipc),
        dp("country?", country),
        dp("homePhone?", hphone),
        dp("cellPhone?", cphone),
        dp("email?", email),
        dp("workEmail?", wemail),
        dp("birthMonth", bmonth, "integer"),
        dp("birthDay", bday, "integer"),
        dp("birthYear?", byear, "integer"),
        dp("gender", gender, "integer"),
        dp("membershipDate?", memberdate, "date"),
        dp("dateEntered", dateentered, "dateTime"),
        dp("enteredBy", enteredby, "integer"),
        op("belongsToFamily", res("Family", (pid - 1) // 2 + 1)),
    ]
    emit_entity(f, lines)
    per_instances.append(uri)

# ─── GROUP ─────────────────────────────────────────────────────────────────────
groups = [
    (1, "Choir",               1, "Sing in the Sunday worship service"),
    (2, "Youth Fellowship",    1, "Weekly youth group for ages 13-18"),
    (3, "Welcome Committee",    1, "Greet newcomers and visitors"),
    (4, "Finance Committee",   1, "Oversee church finances and budgeting"),
    (5, "Sunday School Teachers", 1, "Lead Sunday school classes"),
]
grp_instances = []
for (gid, gname, gtype, gdesc) in groups:
    uri = res("Group", gid)
    lines = [
        f"{uri}",
        rdf_type("Group"),
        dp("name", gname),
        dp("type", gtype, "integer"),
        dp("description?", gdesc),
        dp("active", True, "boolean"),
        dp("includeEmailExport", True, "boolean"),
    ]
    emit_entity(f, lines)
    grp_instances.append(uri)

# ─── PERSON GROUP ROLE ─────────────────────────────────────────────────────────
pgr_data = [
    (1, 1, 1, 1),  # James: Choir, role 1
    (2, 1, 4, 1),  # James: Finance, role 1
    (3, 2, 1, 2),  # Sarah: Choir, role 2
    (4, 2, 3, 1),  # Sarah: Welcome, role 1
    (5, 3, 2, 1),  # Michael: Youth, role 1
    (6, 3, 4, 2),  # Michael: Finance, role 2
    (7, 4, 3, 2),  # Emily: Welcome, role 2
    (8, 5, 5, 1),  # Wei: Teachers, role 1
    (9, 6, 5, 2),  # Lin: Teachers, role 2
]
for (pgid, perid, grpid, roleid) in pgr_data:
    uri = res("PersonGroupRole", pgid)
    lines = [
        f"{uri}",
        rdf_type("PersonGroupRole"),
        dp("roleId", roleid, "integer"),
        op("memberOfGroup", res("Person", perid)),
        op("hasGroupMember", res("Group", grpid)),
    ]
    emit_entity(f, lines)

# ─── EVENT TYPE ───────────────────────────────────────────────────────────────
event_types = [
    (1, "Sunday Worship",    "10:00:00", "none", "0", "0", 1),
    (2, "Bible Study",       "19:00:00", "none", "0", "0", 1),
    (3, "Youth Meeting",     "18:30:00", "none", "0", "0", 1),
    (4, "Choir Practice",    "18:00:00", "none", "0", "0", 1),
    (5, "VBS",               "09:00:00", "none", "0", "0", 1),
]
for (tid, tname, defstart, recurtype, dow, dom, active) in event_types:
    uri = res("EventType", tid)
    lines = [
        f"{uri}",
        rdf_type("EventType"),
        dp("typeName", tname),
        dp("defstarttime", defstart, "string"),
        dp("defrecurtype", recurtype, "string"),
        dp("defrecurDOW", dow, "string"),
        dp("defrecurDOM", dom, "string"),
        dp("active", active, "integer"),
    ]
    emit_entity(f, lines)

# ─── LOCATION ─────────────────────────────────────────────────────────────────
locations = [
    (1, "Main Sanctuary",     "123 Faith Avenue", "Springfield", "IL", "62701",
     "USA", "+1-555-0100", "sanctuary@grace.org", "America/Chicago"),
    (2, "Fellowship Hall",    "123 Faith Avenue", "Springfield", "IL", "62701",
     "USA", "+1-555-0100", "hall@grace.org", "America/Chicago"),
    (3, "Youth Room",         "123 Faith Avenue", "Springfield", "IL", "62701",
     "USA", "+1-555-0100", "youth@grace.org", "America/Chicago"),
    (4, "Sunday School Wing", "123 Faith Avenue", "Springfield", "IL", "62701",
     "USA", "+1-555-0100", "school@grace.org", "America/Chicago"),
]
for loc in locations:
    uri = res("Location", loc[0])
    lines = [
        f"{uri}",
        rdf_type("Location"),
        dp("typeID", loc[0], "integer"),
        dp("name", loc[1]),
        dp("address", loc[2]),
        dp("city", loc[3]),
        dp("state", loc[4]),
        dp("zip", loc[5]),
        dp("country", loc[6]),
        dp("phone", loc[7]),
        dp("email", loc[8]),
        dp("timezone", loc[9]),
    ]
    emit_entity(f, lines)

# ─── EVENT ─────────────────────────────────────────────────────────────────────
events = [
    (1, 1, "Easter Sunday Service",     "2026-04-05T10:00:00", "2026-04-05T12:00:00",
     0, 1, 1, 2, None),
    (2, 2, "Wednesday Bible Study",    "2026-04-08T19:00:00", "2026-04-08T20:30:00",
     0, 2, 1, 2, None),
    (3, 3, "Youth Summer Camp Info",   "2026-04-10T18:30:00", "2026-04-10T20:00:00",
     0, 3, 3, 4, None),
    (4, 4, "Choir Easter Rehearsal",   "2026-04-04T18:00:00", "2026-04-04T20:00:00",
     0, 4, 1, 2, None),
    (5, 1, "Palm Sunday Procession",   "2026-03-29T10:00:00", "2026-03-29T11:30:00",
     0, 1, 1, 2, None),
]
for ev in events:
    (eid, etype, title, start, end, inactive, locid, pcpid, scpid, url) = ev
    uri = res("Event", eid)
    lines = [
        f"{uri}",
        rdf_type("Event"),
        dp("title", title),
        dp("start", start, "dateTime"),
        dp("end", end, "dateTime"),
        dp("type", etype, "integer"),
        dp("inactive", inactive, "integer"),
        dp("locationId", locid, "integer"),
        dp("primaryContactPersonId", pcpid, "integer"),
        dp("secondaryContactPersonId", scpid, "integer"),
        dp("url?", url),
        op("atLocation", res("Location", locid)),
        op("primaryContact", res("Person", pcpid)),
        op("secondaryContact", res("Person", scpid)),
    ]
    emit_entity(f, lines)

# ─── EVENT ATTEND ─────────────────────────────────────────────────────────────
ea_data = [
    (1, 1, 1, "2026-04-05T09:55:00", None),
    (2, 1, 2, "2026-04-05T09:50:00", None),
    (3, 1, 3, "2026-04-05T10:01:00", None),
    (4, 1, 4, "2026-04-05T09:58:00", None),
    (5, 1, 5, "2026-04-05T09:45:00", None),
    (6, 1, 6, "2026-04-05T09:47:00", None),
    (7, 4, 1, "2026-04-04T17:55:00", "2026-04-04T20:05:00"),
    (8, 4, 2, "2026-04-04T17:50:00", "2026-04-04T20:00:00"),
]
for (aid, eid, pid, ci, co) in ea_data:
    uri = res("EventAttend", aid)
    lines = [
        f"{uri}",
        rdf_type("EventAttend"),
        dp("checkinDate?", ci, "dateTime"),
        dp("checkoutDate?", co, "dateTime"),
        op("attendsEvent", res("Event", eid)),
        op("assignedToEvent", res("Person", pid)),
    ]
    emit_entity(f, lines)

# ─── EVENT COUNTS ─────────────────────────────────────────────────────────────
ec_data = [
    (1, 1, "Adult Attendance", 120, "Full sanctuary"),
    (2, 1, "Children",           35, "Sunday school concurrent"),
    (3, 5, "Total Attendance",   85, "Including procession participants"),
]
for (eid, cid, cname, ccount, cnotes) in ec_data:
    uri = res("EventCounts", eid * 10 + cid)
    lines = [
        f"{uri}",
        rdf_type("EventCounts"),
        dp("countName?", cname),
        dp("countCount?", ccount, "integer"),
        dp("notes?", cnotes),
    ]
    emit_entity(f, lines)

# ─── EVENT AUDIENCE ────────────────────────────────────────────────────────────
eaudi_data = [
    (1, 1, 2),  # Easter -> Youth Fellowship
    (2, 1, 3),  # Easter -> Welcome Committee
    (3, 3, 2),  # Youth event -> Youth Fellowship
]
for (i, evid, grpid) in eaudi_data:
    uri = res("EventAudience", i)
    lines = [
        f"{uri}",
        rdf_type("EventAudience"),
        op("hasAudienceGroup", res("Event", evid)),
        op("eventInAudience", res("Group", grpid)),
    ]
    emit_entity(f, lines)

# ─── CALENDAR EVENT ───────────────────────────────────────────────────────────
ce_data = [
    (1, 1, 1),  # Calendar 1 -> Event 1 (Easter)
    (2, 1, 5),  # Calendar 1 -> Event 5 (Palm Sunday)
    (3, 2, 3),  # Calendar 2 -> Event 3 (Youth)
]
for (i, calid, evid) in ce_data:
    uri = res("CalendarEvent", i)
    lines = [
        f"{uri}",
        rdf_type("CalendarEvent"),
        dp("id", i, "integer"),
        op("calendarOfEvent", res("Calendar", calid)),
        op("eventOnCalendar", res("Event", evid)),
    ]
    emit_entity(f, lines)

# ─── DONATION FUND ─────────────────────────────────────────────────────────────
funds = [
    (1, "T", "General Fund",   "Unrestricted gifts for general operations", 1),
    (2, "T", "Building Fund",  "For church building expansion and maintenance", 2),
    (3, "T", "Missions Fund", "Supports local and global mission work", 3),
    (4, "T", "Youth Fund",    "Youth activities and camp scholarships", 4),
]
for (fid, factive, fname, fdesc, forder) in funds:
    uri = res("DonationFund", fid)
    lines = [
        f"{uri}",
        rdf_type("DonationFund"),
        dp("active", factive),
        dp("name?", fname),
        dp("description?", fdesc),
        dp("order", forder, "integer"),
        dp("id", fid, "integer"),
    ]
    emit_entity(f, lines)

# ─── DEPOSIT ──────────────────────────────────────────────────────────────────
deposits = [
    (1, "2026-03-28", "Sunday collection - Easter prep", 1, False, "C"),
    (2, "2026-03-21", "Sunday collection",               1, True,  "C"),
]
for (did, ddate, dcomment, dentered, dclosed, dtype) in deposits:
    uri = res("Deposit", did)
    lines = [
        f"{uri}",
        rdf_type("Deposit"),
        dp("date?", ddate, "date"),
        dp("comment?", dcomment),
        dp("enteredby?", dentered, "integer"),
        dp("closed", dclosed, "boolean"),
        dp("type", dtype),
        dp("id", did, "integer"),
    ]
    emit_entity(f, lines)

# ─── PLEDGE ───────────────────────────────────────────────────────────────────
pledges = [
    (1, 1,  1, "2026-01-01",  500.00, "M",    "CHECK", "Monthly general tithes",
     "2026-01-01", 1, "Pledge", 1, 1,  1001, False, "G-2026-001"),
    (2, 2,  3, "2026-01-01",  250.00, "W",    "CASH",  "Weekly building fund",
     "2026-01-01", 1, "Pledge", 2, 2,  None, False, "G-2026-002"),
    (3, 1,  3, "2026-02-01",  600.00, "M",    "CHECK", "Monthly missions pledge",
     "2026-02-01", 1, "Pledge", 1, 1,  1002, False, "G-2026-003"),
    (4, 3,  4, "2026-02-15",  100.00, "M",    "ONLINE","Monthly youth fund",
     "2026-02-15", 1, "Pledge", 3, None, None, False, "G-2026-004"),
]
for plg in pledges:
    (pgid, pfid, pperid, pdate, pamt, psched, pmeth, pcomment,
     peddate, pedby, ptype, pfundid, pdepid, pcheckno, pproblem, pgrpkey) = plg
    uri = res("Pledge", pgid)
    lines = [
        f"{uri}",
        rdf_type("Pledge"),
        dp("date?", pdate, "date"),
        dp("amount?", pamt, "decimal"),
        dp("schedule?", psched),
        dp("method?", pmeth),
        dp("comment?", pcomment),
        dp("fundId?", pfundid, "integer"),
        dp("depId?", pdepid, "integer"),
        dp("checkNo?", pcheckno, "integer"),
        dp("problem?", pproblem, "boolean"),
        dp("groupKey", pgrpkey),
        dp("pledgeOrPayment", ptype),
        dp("dateLastEdited", peddate, "date"),
        dp("editedBy", pedby, "integer"),
        dp("cleared", False, "boolean"),
        dp("nonDeductible", 0, "decimal"),
        op("hasFY", res("Family", pfid)),
        op("fundedByFund", res("DonationFund", pfundid)),
    ]
    emit_entity(f, lines)

# ─── FUND RAISER ──────────────────────────────────────────────────────────────
fr_data = [(1, "2026-04-19", "Spring Bazaar & Auction",
              "Annual spring fundraising event", 1, "2026-03-01")]
for (frid, frdate, frtitle, frdesc, frenteredby, frenterdate) in fr_data:
    uri = res("FundRaiser", frid)
    lines = [
        f"{uri}",
        rdf_type("FundRaiser"),
        dp("date?", frdate, "date"),
        dp("title", frtitle),
        dp("description?", frdesc),
        dp("enteredBy", frenteredby, "integer"),
        dp("enteredDate", frenterdate, "date"),
        dp("id", frid, "integer"),
    ]
    emit_entity(f, lines)

# ─── DONATED ITEM ─────────────────────────────────────────────────────────────
di_data = [
    (1, "Vintage Hymn Book Collection", 1, 1, 2, 0,
     "Rare 1920s Hymnals Set",
     "A complete set of 50 vintage hymnals from 1923",
     150.00, 200.00, 100.00, 50.00, 1, "2026-03-15", None),
    (2, "Handmade Quilt", 1, 3, 4, 1,
     "Queen-Size Church Community Quilt",
     "Hand-stitched quilt made by the Women's Fellowship group",
     80.00, 120.00, 60.00, 30.00, 1, "2026-03-16", None),
    (3, "Antique Silver Candlesticks", 1, 5, 6, 0,
     "Pair of Victorian Silver Candlesticks",
     "Inherited Victorian-era silver-plated candlesticks",
     200.00, 350.00, 180.00, 100.00, 1, "2026-03-17", None),
]
for (diid, diitem, difrid, didonor, dibuyer, dimultibuy,
     dititle, didesc, disell, diest, dimin, dimatval,
     dientby, dientdate, dipic) in di_data:
    uri = res("DonatedItem", diid)
    lines = [
        f"{uri}",
        rdf_type("DonatedItem"),
        dp("item", diitem),
        dp("frId", difrid, "integer"),
        dp("title", dititle),
        dp("description?", didesc),
        dp("sellprice?", disell, "decimal"),
        dp("estprice?", diest, "decimal"),
        dp("minimum?", dimin, "decimal"),
        dp("materialvalue?", dimatval, "decimal"),
        dp("multibuy", dimultibuy, "integer"),
        dp("enteredBy", dientby, "integer"),
        dp("enteredDate", dientdate, "date"),
        dp("id", diid, "integer"),
        op("donorOfItem", res("Person", didonor)),
        op("buyerOfItem", res("Person", dibuyer)),
        op("hasDonatedItem", res("FundRaiser", difrid)),
    ]
    emit_entity(f, lines)

# ─── NOTE ─────────────────────────────────────────────────────────────────────
note_data = [
    (1, 1, None, 0,
     "James has been serving as a deacon for 2 years. Excellent contributor to the finance committee.",
     "2025-06-10T10:00:00", 1, None, "general"),
    (2, 3, None, 0,
     "Michael expressed interest in joining the choir. Will follow up in April.",
     "2026-01-15T14:30:00", 1, None, "pastoral"),
    (3, None, 1, 0,
     "Thompson family missed the last two Sundays. Send pastoral visit.",
     "2026-03-20T09:00:00", 1, None, "pastoral"),
]
for (nid, perid, famid, private, text, denter, enteredby, editedby, ntype) in note_data:
    uri = res("Note", nid)
    lines = [
        f"{uri}",
        rdf_type("Note"),
        dp("private", private, "integer"),
        dp("text?", text),
        dp("dateEntered", denter, "dateTime"),
        dp("enteredBy", enteredby, "integer"),
        dp("type?", ntype),
    ]
    if perid:
        lines.append(op("aboutPerson", res("Person", perid)))
    if famid:
        lines.append(op("aboutFamily", res("Family", famid)))
    emit_entity(f, lines)

# ─── USER ─────────────────────────────────────────────────────────────────────
user_data = [
    (1, "jthompson", True,  45, 0, True, True, True, True, True, True, True, True, 1, 1,
     "2026-01-01T08:00:00", 20),
    (2, "swilliams", False, 20, 0, True, True, False, True, True, False, True, False, 1, 1,
     "2026-02-01T08:00:00", 10),
]
for (uid, uname, needpwd, llcount, fcount, addrec, editrec, delrec,
     menuopt, mgrgrp, fin, notes, admin, editself, deffy, curdep, ulogin) in user_data:
    uri = res("User", uid)
    lines = [
        f"{uri}",
        rdf_type("User"),
        dp("userName", uname),
        dp("needPasswordChange", needpwd, "boolean"),
        dp("addRecords", addrec, "boolean"),
        dp("editRecords", editrec, "boolean"),
        dp("deleteRecords", delrec, "boolean"),
        dp("menuOptions", menuopt, "boolean"),
        dp("manageGroups", mgrgrp, "boolean"),
        dp("finance", fin, "boolean"),
        dp("notes", notes, "boolean"),
        dp("admin", admin, "boolean"),
        dp("editSelf", editself, "boolean"),
        dp("defaultFY", deffy, "integer"),
        dp("currentDeposit", curdep, "integer"),
        dp("loginCount", llcount, "integer"),
        dp("failedLogins", fcount, "integer"),
        dp("lastLogin", ulogin, "dateTime"),
        dp("calStart?", "2026-01-01", "date"),
        dp("calEnd?", "2026-12-31", "date"),
        op("linkedToPerson", res("Person", uid)),
    ]
    emit_entity(f, lines)

# ─── VOLUNTEER OPPORTUNITY ─────────────────────────────────────────────────────
vol_data = [
    (1, 1, "A", "Sunday Setup Team",    "Set up chairs and tables before Sunday service"),
    (2, 2, "A", "Welcome Desk Greeter", "Greet visitors at the welcome desk each Sunday"),
    (3, 3, "A", "Coffee Hour Host",      "Coordinate and host the coffee hour after service"),
    (4, 4, "A", "Sound Booth Operator",  "Run the sound system during worship services"),
]
for (void, vorder, vactive, vname, vdesc) in vol_data:
    uri = res("VolunteerOpportunity", void)
    lines = [
        f"{uri}",
        rdf_type("VolunteerOpportunity"),
        dp("order", vorder, "integer"),
        dp("active", vactive),
        dp("name?", vname),
        dp("description?", vdesc),
    ]
    emit_entity(f, lines)

# ─── PERSON VOLUNTEER OPPORTUNITY ─────────────────────────────────────────────
pvo_data = [
    (1, 3, 1),  # Michael -> Setup Team
    (2, 1, 2),  # James -> Greeter
    (3, 4, 3),  # Emily -> Coffee Hour
    (4, 2, 4),  # Sarah -> Sound Booth
]
for (i, perid, volid) in pvo_data:
    uri = res("PersonVolunteerOpportunity", i)
    lines = [
        f"{uri}",
        rdf_type("PersonVolunteerOpportunity"),
        op("hasVolunteerOp", res("Person", perid)),
        op("volunteerOf", res("VolunteerOpportunity", volid)),
    ]
    emit_entity(f, lines)

# ─── PROPERTY TYPE ─────────────────────────────────────────────────────────────
pt_data = [
    (1, "p", "Interest",    "General interest or concern flag"),
    (2, "p", "DoNotCall",   "Do not call flag"),
    (3, "p", "VIP",         "Very important person flag"),
]
for (ptid, ptclass, ptname, ptdesc) in pt_data:
    uri = res("PropertyType", ptid)
    lines = [
        f"{uri}",
        rdf_type("PropertyType"),
        dp("class", ptclass),
        dp("name", ptname),
        dp("description?", ptdesc),
    ]
    emit_entity(f, lines)

# ─── PROPERTY ─────────────────────────────────────────────────────────────────
prop_data = [
    (1, "p", 1, "VIP Member",      "Thompson family designated as long-term VIP supporters"),
    (2, "p", 2, "Do Not Call",     "Williams family requested no unsolicited calls"),
]
for (proid, proclass, proprtid, proname, prodesc) in prop_data:
    uri = res("Property", proid)
    lines = [
        f"{uri}",
        rdf_type("Property"),
        dp("class", proclass),
        dp("name", proname),
        dp("description?", prodesc),
        op("hasRecordProperty", res("PropertyType", proprtid)),
    ]
    emit_entity(f, lines)

# ─── RECORD PROPERTY ─────────────────────────────────────────────────────────
rp_data = [
    (1, 1, 1, "VIP Member - long-time supporter"),
    (2, 2, 1, "Do not call - family request"),
]
for (i, (rpid, recid, propid, rpval)) in enumerate(rp_data, 1):
    uri = res("RecordProperty", i)
    lines = [
        f"{uri}",
        rdf_type("RecordProperty"),
        dp("value?", rpval),
        op("propertyForRecord", res("Property", propid)),
    ]
    emit_entity(f, lines)

# ─── WHY CAME ─────────────────────────────────────────────────────────────────
wc_data = [
    (1, 1, "Was searching for a faith community",
            "Was invited by a friend",
            "More scripture-based teaching",
            "Friend invitation"),
    (2, 3, "Wanted my children to grow in faith",
            "Saw the youth program online",
            "Need more family activities",
            "Website search"),
]
for (i, (wcid, perid, wjoin, wcome, wsuggest, whear)) in enumerate(wc_data, 1):
    uri = res("WhyCame", i)
    lines = [
        f"{uri}",
        rdf_type("WhyCame"),
        dp("join?", wjoin),
        dp("come?", wcome),
        dp("suggest?", wsuggest),
        dp("hearOfUs?", whear),
        op("whyCameForPerson", res("Person", perid)),
    ]
    emit_entity(f, lines)

# ─── MENU LINK ────────────────────────────────────────────────────────────────
menu_data = [
    (1, "Financial Reports", "/ReportEngine.php",  1),
    (2, "People Management",  "/PersonList.php",   2),
    (3, "Event Calendar",     "/EventList.php",    3),
]
for (mlid, mlname, mluri, mlorder) in menu_data:
    uri = res("MenuLink", mlid)
    lines = [
        f"{uri}",
        rdf_type("MenuLink"),
        dp("name?", mlname),
        dp("uri?", mluri),
        dp("order?", mlorder, "integer"),
    ]
    emit_entity(f, lines)

# ─── VERSION ──────────────────────────────────────────────────────────────────
v_data = [(1, "5.0.0", "2025-11-01T00:00:00", None)]
for (vid, vver, vstart, vend) in v_data:
    uri = res("Version", vid)
    lines = [
        f"{uri}",
        rdf_type("Version"),
        dp("version", vver),
        dp("updateStart?", vstart, "dateTime"),
        dp("updateEnd?", vend, "dateTime"),
    ]
    emit_entity(f, lines)

# ─── TOKEN ─────────────────────────────────────────────────────────────────────
token_data = [
    (1, "abc123token", "password-reset", "2026-04-12", 1, 1),
    (2, "xyz789token", "magic-link",     "2026-04-10", 3, 1),
]
for (i, ttoken, ttype, tvld, trefid, tremuses) in token_data:
    uri = res("Token", i)
    lines = [
        f"{uri}",
        rdf_type("Token"),
        dp("token", ttoken),
        dp("type", ttype),
        dp("validUntilDate?", tvld, "date"),
        dp("referenceId?", trefid, "integer"),
        dp("remainingUses?", tremuses, "integer"),
    ]
    emit_entity(f, lines)

# ─── USER SETTING ──────────────────────────────────────────────────────────────
us_data = [
    (1, 1, "userTimeZone", "America/Chicago"),
    (2, 1, "userLanguage", "en-US"),
    (3, 2, "userTimeZone", "America/Chicago"),
    (4, 2, "userLanguage", "en-US"),
]
for (i, uid, usname, usval) in us_data:
    uri = res("UserSetting", i)
    lines = [
        f"{uri}",
        rdf_type("UserSetting"),
        dp("settingName", usname),
        dp("settingValue?", usval),
    ]
    emit_entity(f, lines)

# ─── KIOSK DEVICE ──────────────────────────────────────────────────────────────
kdev_data = [
    (1, "hashabc123", "Welcome Kiosk 1",  "tablet", "2026-04-04T09:00:00", True,  None),
    (2, "hashxyz789", "Check-in Kiosk 2","kiosk",  "2026-04-05T08:30:00", True,  None),
]
for (kdid, kdhash, kdname, kdtype, kdheart, kdaccept, kdpend) in kdev_data:
    uri = res("KioskDevice", kdid)
    lines = [
        f"{uri}",
        rdf_type("KioskDevice"),
        dp("guidHash?", kdhash),
        dp("name?", kdname),
        dp("deviceType?", kdtype),
        dp("lastHeartbeat?", kdheart, "dateTime"),
        dp("accepted?", kdaccept, "boolean"),
        dp("pendingCommands?", kdpend),
    ]
    emit_entity(f, lines)

# ─── KIOSK ASSIGNMENT ─────────────────────────────────────────────────────────
kas_data = [
    (1, 1, 1, 1),  # Kiosk 1 assigned to Event 1 (Easter)
    (2, 2, 2, 5),  # Kiosk 2 assigned to Event 5 (Palm Sunday)
]
for (kasid, kaskdev, kasastype, kaspevent) in kas_data:
    uri = res("KioskAssignment", kasid)
    lines = [
        f"{uri}",
        rdf_type("KioskAssignment"),
        dp("assignmentType?", kasastype, "integer"),
        op("hasKioskDevice", res("KioskDevice", kaskdev)),
        op("assignedToEvent", res("Event", kaspevent)),
    ]
    emit_entity(f, lines)

# ─── PREDEFINED REPORTS ───────────────────────────────────────────────────────
rep_data = [
    (1, "SELECT * FROM Person", "Active Members Report",
     "Lists all currently active church members", True),
    (2, "SELECT * FROM Family", "Family Directory Report",
     "Generates the church family directory", False),
]
for (qid, qsql, qname, qdesc, qcount) in rep_data:
    uri = res("PredefinedReports", qid)
    lines = [
        f"{uri}",
        rdf_type("PredefinedReports"),
        dp("sql?", qsql),
        dp("name", qname),
        dp("description?", qdesc),
        dp("count?", qcount, "boolean"),
    ]
    emit_entity(f, lines)

# ─── LIST OPTION ─────────────────────────────────────────────────────────────
lo_data = [
    (1, 1, 1, "Mr."),  (1, 2, 2, "Mrs."),  (1, 3, 3, "Ms."),  (1, 4, 4, "Dr."),
    (2, 1, 1, "Member"), (2, 2, 2, "Regular Attender"), (2, 3, 3, "Visitor"),
]
for (lid, oid, seq, oname) in lo_data:
    uri = res("ListOption", lid * 10 + oid)
    lines = [
        f"{uri}",
        rdf_type("ListOption"),
        dp("optionSequence", seq, "integer"),
        dp("optionName", oname),
    ]
    emit_entity(f, lines)

# ─── QUERY PARAMETERS (sample) ────────────────────────────────────────────────
qp_data = [
    (1, 1, 1, None, "Person Name", "Filter by person name",
     "per_Name", "John", 0, 0, None, None, None, None),
    (2, 1, 2, None, "Family Name", "Filter by family name",
     "fam_Name", "Smith", 0, 0, None, None, None, None),
]
for row in qp_data:
    (qpid, qryid, qrtype, qroptsql, qname, qdesc, qalias,
     qdefault, qrequired, qrb, qval, qnmax, qnmin, qamin) = row
    uri = res("QueryParameters", qpid)
    lines = [
        f"{uri}",
        rdf_type("QueryParameters"),
        dp("type", qrtype, "integer"),
        dp("optionSQL?", qroptsql),
        dp("name?", qname),
        dp("description?", qdesc),
        dp("alias?", qalias),
        dp("default?", qdefault),
        dp("required", qrequired, "integer"),
        dp("inputBoxSize", qrb, "integer"),
        dp("validation?", qval),
        dp("numericMax?", qnmax, "integer"),
        dp("numericMin?", qnmin, "integer"),
        dp("alphaMinLength?", qamin, "integer"),
    ]
    emit_entity(f, lines)

# ─── QUERY PARAMETER OPTIONS ─────────────────────────────────────────────────
qpo_data = [
    (1, 1, "Exact Match", "exact"),
    (2, 1, "Starts With", "starts"),
    (3, 1, "Contains",    "contains"),
]
for (i, (qpaid, qrp_id, qdisplay, qvalue)) in enumerate(qpo_data, 1):
    uri = res("QueryParameterOptions", i)
    lines = [
        f"{uri}",
        rdf_type("QueryParameterOptions"),
        dp("display", qdisplay),
        dp("value", qvalue),
    ]
    emit_entity(f, lines)

# ─── FAMILY CUSTOM MASTER ────────────────────────────────────────────────────
fcm_data = [
    ("Hobbies",     1, "Hobbies & Interests",   None, 1, 1),
    ("Anniversary", 2, "Anniversary Type",       None, 1, 2),
]
for (i, row) in enumerate(fcm_data, 1):
    (fcfield, fcorder, fcname, fcspec, fcsec, tid) = row
    uri = res("FamilyCustomMaster", i)
    lines = [
        f"{uri}",
        rdf_type("FamilyCustomMaster"),
        dp("order", fcorder, "integer"),
        dp("name", fcname),
        dp("special?", fcspec, "integer"),
        dp("fieldSec", fcsec, "integer"),
        dp("typeId", tid, "integer"),
    ]
    emit_entity(f, lines)

# ─── PERSON CUSTOM MASTER ────────────────────────────────────────────────────
pcm_data = [
    ("FacebookURL",  1, "Facebook Profile URL",  None, 1, 1),
    ("LinkedInURL",  2, "LinkedIn Profile URL",  None, 1, 1),
]
for (i, row) in enumerate(pcm_data, 1):
    (pcfield, pcorder, pcname, pcspec, pcsec, tid) = row
    uri = res("PersonCustomMaster", i)
    lines = [
        f"{uri}",
        rdf_type("PersonCustomMaster"),
        dp("order", pcorder, "integer"),
        dp("name", pcname),
        dp("special?", pcspec, "integer"),
        dp("fieldSec", pcsec, "integer"),
        dp("typeId", tid, "integer"),
    ]
    emit_entity(f, lines)

# ─── GROUP PROP MASTER ─────────────────────────────────────────────────────────
gpm_data = [
    (1, 1, "BaptismDate", "Date of Baptism",        None, 1, None, "p"),
    (2, 1, "SchoolGrade", "Current School Grade",   None, 1, None, "p"),
]
for (i, row) in enumerate(gpm_data, 1):
    (grpid, propid, propfield, propname, propdesc, typesid, propspec, persondisplay) = row
    uri = res("GroupPropMaster", i)
    lines = [
        f"{uri}",
        rdf_type("GroupPropMaster"),
        dp("propField", propfield),
        dp("propName?", propname),
        dp("propDescription?", propdesc),
        dp("typeId", typesid, "integer"),
        dp("special?", propspec, "integer"),
        dp("personDisplay", persondisplay),
    ]
    emit_entity(f, lines)

# ─── USER CONFIG ──────────────────────────────────────────────────────────────
ucfg_data = [
    (1, 1, "defaultStyle", "default", "string", "style", "s", "b"),
    (2, 1, "showTooltips", "true",    "bool",   "tips",  "s", "b"),
]
for (i, row) in enumerate(ucfg_data, 1):
    (perid, ucfgid, ucfgname, ucfgval, ucfgtype, ucfgtooltip, ucfgperm, ucfgcat) = row
    uri = res("UserConfig", i)
    lines = [
        f"{uri}",
        rdf_type("UserConfig"),
        dp("name", ucfgname),
        dp("value?", ucfgval),
        dp("type", ucfgtype),
        dp("tooltip?", ucfgtooltip),
        dp("permission", ucfgperm),
        dp("cat", ucfgcat),
    ]
    emit_entity(f, lines)

# ─── Close TTL file ───────────────────────────────────────────────────────────
f.close()
print(f"✅ crm_data.ttl written")

# ─── Generate graph.json ─────────────────────────────────────────────────────
DOMAIN_GROUPS = {
    "Person": 1, "Family": 1, "PersonGroupRole": 1, "PersonVolunteerOpportunity": 1,
    "User": 1, "UserConfig": 1, "UserSetting": 1,
    "Group": 4, "VolunteerOpportunity": 4, "GroupPropMaster": 4,
    "Event": 3, "EventType": 3, "EventAttend": 3, "EventAudience": 3,
    "EventCounts": 3, "EventCountName": 3, "Calendar": 3, "CalendarEvent": 3,
    "Location": 3,
    "Deposit": 2, "Pledge": 2, "DonationFund": 2, "FundRaiser": 2,
    "DonatedItem": 2,
    "Property": 5, "PropertyType": 5, "RecordProperty": 5,
    "Note": 1,
    "WhyCame": 1,
    "KioskDevice": 3, "KioskAssignment": 3,
    "Config": 0, "Version": 0, "Token": 0, "MenuLink": 0,
    "PredefinedReports": 0, "QueryParameters": 0, "QueryParameterOptions": 0,
    "ListOption": 0, "PersonCustom": 0, "PersonCustomMaster": 0,
    "FamilyCustom": 0, "FamilyCustomMaster": 0,
}

ontology_edges = [
    {"source": "Person",         "target": "Family",            "relation": "belongsToFamily"},
    {"source": "Family",        "target": "Person",            "relation": "hasFamilyMember"},
    {"source": "Person",        "target": "Group",             "relation": "memberOfGroup"},
    {"source": "Group",         "target": "Person",            "relation": "hasGroupMember"},
    {"source": "PersonGroupRole","target": "Person",            "relation": "memberOfGroup"},
    {"source": "PersonGroupRole","target": "Group",             "relation": "hasGroupMember"},
    {"source": "Person",        "target": "Event",             "relation": "attendsEvent"},
    {"source": "Event",         "target": "Person",             "relation": "hasEventAttendee"},
    {"source": "EventAttend",   "target": "Person",             "relation": "assignedToEvent"},
    {"source": "EventAttend",   "target": "Event",             "relation": "attendsEvent"},
    {"source": "Event",         "target": "Location",          "relation": "atLocation"},
    {"source": "Event",         "target": "EventType",         "relation": "hasType"},
    {"source": "Event",         "target": "Group",             "relation": "hasAudienceGroup"},
    {"source": "Group",         "target": "Event",             "relation": "eventInAudience"},
    {"source": "EventAudience", "target": "Event",             "relation": "hasAudienceGroup"},
    {"source": "EventAudience", "target": "Group",             "relation": "eventInAudience"},
    {"source": "CalendarEvent", "target": "Calendar",        "relation": "calendarOfEvent"},
    {"source": "CalendarEvent", "target": "Event",            "relation": "eventOnCalendar"},
    {"source": "Family",        "target": "Pledge",            "relation": "hasFamilyPledge"},
    {"source": "Pledge",        "target": "Family",            "relation": "hasFY"},
    {"source": "Pledge",        "target": "DonationFund",      "relation": "fundedByFund"},
    {"source": "Deposit",       "target": "Pledge",           "relation": "hasDepositSlip"},
    {"source": "FundRaiser",   "target": "DonatedItem",       "relation": "hasDonatedItem"},
    {"source": "Person",        "target": "DonatedItem",       "relation": "donorOfItem"},
    {"source": "Person",        "target": "DonatedItem",       "relation": "buyerOfItem"},
    {"source": "Person",        "target": "Note",               "relation": "hasNote"},
    {"source": "Note",          "target": "Person",            "relation": "noteAboutPerson"},
    {"source": "Family",        "target": "Note",              "relation": "familyHasNote"},
    {"source": "Note",          "target": "Family",            "relation": "noteAboutFamily"},
    {"source": "User",          "target": "Person",            "relation": "linkedToPerson"},
    {"source": "Person",        "target": "VolunteerOpportunity","relation": "hasVolunteerOp"},
    {"source": "VolunteerOpportunity","target": "Person",      "relation": "volunteerOf"},
    {"source": "PersonVolunteerOpportunity","target": "Person","relation": "hasVolunteerOp"},
    {"source": "PersonVolunteerOpportunity","target": "VolunteerOpportunity","relation": "volunteerOf"},
    {"source": "Event",         "target": "EventCounts",       "relation": "hasEventCounts"},
    {"source": "WhyCame",       "target": "Person",            "relation": "whyCameForPerson"},
    {"source": "Property",      "target": "PropertyType",      "relation": "hasRecordProperty"},
    {"source": "RecordProperty","target": "Property",          "relation": "propertyForRecord"},
    {"source": "KioskAssignment","target": "KioskDevice",      "relation": "hasKioskDevice"},
    {"source": "KioskAssignment","target": "Event",            "relation": "assignedToEvent"},
    {"source": "PredefinedReports","target": "QueryParameters","relation": "hasQueryParameter"},
    {"source": "QueryParameters","target": "QueryParameterOptions","relation": "hasOption"},
]

edge_count = {}
for e in ontology_edges:
    for k in [e["source"], e["target"]]:
        edge_count[k] = edge_count.get(k, 0) + 1

all_classes = [
    "Calendar", "CalendarEvent", "Config", "Deposit", "DonatedItem", "DonationFund",
    "Event", "EventAttend", "EventAudience", "EventCountName", "EventCounts",
    "EventType", "Family", "FamilyCustom", "FamilyCustomMaster", "FundRaiser",
    "Group", "GroupPropMaster", "KioskAssignment", "KioskDevice", "ListOption",
    "Location", "MenuLink", "Note", "Person", "PersonCustom", "PersonCustomMaster",
    "PersonGroupRole", "PersonVolunteerOpportunity", "Pledge", "PredefinedReports",
    "Property", "PropertyType", "QueryParameterOptions", "QueryParameters",
    "RecordProperty", "Token", "User", "UserConfig", "UserSetting", "Version",
    "VolunteerOpportunity", "WhyCame",
]

nodes = [{"id": cls, "group": DOMAIN_GROUPS.get(cls, 0), "connections": edge_count.get(cls, 0)}
         for cls in all_classes]

graph = {"nodes": nodes, "links": ontology_edges}
with open(OUT_JSON, "w", encoding="utf-8") as gf:
    json.dump(graph, gf, indent=2)

print(f"✅ graph.json written")
print(f"   Nodes: {len(nodes)}, Links: {len(ontology_edges)}")
