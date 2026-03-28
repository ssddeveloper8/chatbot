from executor import execute_sql


def resolve_entity(entity_type, entity_value):
    """
    Generic resolver for KPI, TAG, etc.
    """

    if entity_type == "kpi":
        sql = f"""
        SELECT alias
        FROM tbl_kpi_engine_kpi_calculation
        WHERE LOWER(kpi_name) = LOWER('{entity_value}')
        LIMIT 1;
        """
        db = "builder"

    elif entity_type == "tag":
        sql = f"""
        SELECT tag_id
        FROM tbl_cfg_opc_hda_tag_config
        WHERE LOWER(tag_name) = LOWER('{entity_value}')
        LIMIT 1;
        """
        db = "builder"

    else:
        return None

    result = execute_sql(db, sql)

    if result:
        return result[0]

    return None