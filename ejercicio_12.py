# +-------------------------------------+
# |      EstructuraArqueologica         |
# +-------------------------------------+
# | codigo : String                     |
# | datacion : String                   |
# +-------------------------------------+
# |                                     |
# +-------------------------------------+
#         1        compuestaPor       0..*
# EstructuraArqueologica ◀───────────────◆ EstructuraArqueologica
#                  formaParteDe (0..1)

# EstructuraArqueologica ────────── 0..* Material
#                  materiales
