# =================================================== DESCRIPTION =====================================================
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# =================================================== DESCRIPTION =====================================================


# =================================================== EXAMPLES ========================================================
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# =================================================== EXAMPLES ========================================================


# =====================================================================================================================
SUB = str.maketrans('0123456789a', '₀₁₂₃₄₅₆₇₈₉\u2090')
# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------
def sub(s):
    if isinstance(s, int):
        s = str(s)

    return s.translate(SUB)
# -------------------------------------------------------------------------------------------------