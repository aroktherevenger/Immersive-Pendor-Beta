# Common constants and imports shared across all module files.
# Mirrors the vanilla M&B header_common.py with PoP-specific additions.

# ── Faction IDs ──────────────────────────────────────────────────────────────
fac_no_faction          = 0
fac_commoners           = 1
fac_outlaws             = 2
fac_kingdom_1           = 3   # Kingdom of Pendor
fac_kingdom_2           = 4   # Fierdsvain
fac_kingdom_3           = 5   # Empire
fac_kingdom_4           = 6   # D'Shar Principalities
fac_kingdom_5           = 7   # Ravenstern
fac_kingdom_6           = 8   # Barclay (minor)
fac_snake_cult          = 9
fac_noldor              = 10
fac_jatu                = 11
fac_heretics            = 12

# ── Troop Flags ───────────────────────────────────────────────────────────────
tf_male                 = 0x00000001
tf_female               = 0x00000002
tf_hero                 = 0x00000010    # Named unique character
tf_guarantee_boots      = 0x00000200
tf_guarantee_armor      = 0x00000400
tf_guarantee_gloves     = 0x00000800
tf_guarantee_helmet     = 0x00001000
tf_guarantee_ranged     = 0x00002000
tf_guarantee_horse      = 0x00004000
tf_guarantee_shield     = 0x00008000
tf_mounted              = 0x00010000
tf_no_cap_on_death      = 0x00020000
tf_is_merchant          = 0x00040000

# ── Item Kinds ────────────────────────────────────────────────────────────────
itp_type_horse          = 1
itp_type_one_handed     = 2
itp_type_two_handed     = 3
itp_type_polearm        = 4
itp_type_arrows         = 5
itp_type_bolts          = 6
itp_type_shield         = 7
itp_type_bow            = 8
itp_type_crossbow       = 9
itp_type_thrown         = 10
itp_type_goods          = 11
itp_type_head_armor     = 12
itp_type_body_armor     = 13
itp_type_foot_armor     = 14
itp_type_hand_armor     = 15
itp_type_pistol         = 16
itp_type_musket         = 17
itp_type_bullets        = 18
itp_type_animal         = 19
itp_type_book           = 20

# Common item property flags
itp_merchandise         = 0x00000001
itp_wooden_parry        = 0x00000002
itp_fit_to_head         = 0x00000008
itp_civilian            = 0x00000010
itp_next_item_as_melee  = 0x00000020
itp_covers_legs         = 0x00000040
itp_female_head         = 0x00000080
itp_couchable           = 0x00000100
itp_two_handed          = 0x00000200
itp_primary             = 0x00000400
itp_secondary           = 0x00000800
itp_cant_reload_on_horseback = 0x00001000
itp_no_parry            = 0x00002000
itp_charge              = 0x00004000
itp_unbalanced          = 0x00008000

# ── Weapon Proficiency Indices ────────────────────────────────────────────────
wp_one_handed           = 0
wp_two_handed           = 1
wp_polearm              = 2
wp_archery              = 3
wp_crossbow             = 4
wp_throwing             = 5

# ── Attribute Indices ─────────────────────────────────────────────────────────
ca_strength             = 0
ca_agility              = 1
ca_intelligence         = 2
ca_charisma             = 3
ca_level                = 4

# ── Skill IDs (PoP relevant) ──────────────────────────────────────────────────
# Skills are encoded as (skill_id << 4) | level  in troop definitions
skl_trade               = 0
skl_leadership          = 1
skl_prisoner_management = 2
skl_scouting            = 3
skl_tactics             = 4
skl_pathfinding         = 5
skl_spotting            = 6
skl_inventory_management= 7
skl_wound_treatment     = 8
skl_surgery             = 9
skl_first_aid           = 10
skl_engineer            = 11
skl_persuasion          = 12
skl_riding              = 14
skl_athletics           = 15
skl_shield              = 16
skl_weapon_master       = 17
skl_horse_archery       = 18
skl_power_draw          = 19
skl_power_throw         = 20
skl_power_strike        = 21
skl_ironflesh           = 22
skl_trainer             = 23

def encode_attr(strength, agility, intelligence, charisma, level):
    return (strength | (agility << 6) | (intelligence << 12) |
            (charisma << 18) | (level << 24))

def encode_skill(skill_id, level):
    return (skill_id << 4) | level

def encode_wp(one_handed=0, two_handed=0, polearm=0,
              archery=0, crossbow=0, throwing=0):
    return (one_handed | (two_handed << 10) | (polearm << 20) |
            (archery << 30) | (crossbow << 40) | (throwing << 50))
