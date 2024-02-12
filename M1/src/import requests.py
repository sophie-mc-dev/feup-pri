import requests

# List of URLs to download
urls = [
    "https://en.wikipedia.org/wiki/Acacia",
    "https://en.wikipedia.org/wiki/Acacia_ammobia",
    "https://en.wikipedia.org/wiki/Acacia_estrophiolata",
    "https://en.wikipedia.org/wiki/Acer_(genus)",
    "https://en.wikipedia.org/wiki/Acer_leucoderme",
    "https://en.wikipedia.org/wiki/Acer_negundo",
    "https://en.wikipedia.org/wiki/Acer_nigrum",
    "https://en.wikipedia.org/wiki/Acer_pensylvanicum",
    "https://en.wikipedia.org/wiki/Acer_saccharinum",
    "https://en.wikipedia.org/wiki/Acer_saccharum",
    "https://en.wikipedia.org/wiki/Achillea",
    "https://en.wikipedia.org/wiki/Achillea_filipendulina",
    "https://en.wikipedia.org/wiki/Achillea_millefolium",
    "https://en.wikipedia.org/wiki/Achillea_ptarmica",
    "https://en.wikipedia.org/wiki/Achillea_tomentosa",
    "https://en.wikipedia.org/wiki/Adansonia",
    "https://en.wikipedia.org/wiki/Adenanthos_obovatus",
    "https://en.wikipedia.org/wiki/Adenium_obesum",
    "https://en.wikipedia.org/wiki/Aesculus_californica",
    "https://en.wikipedia.org/wiki/Agapanthus_praecox",
    "https://en.wikipedia.org/wiki/Ajuga_reptans",
    "https://en.wikipedia.org/wiki/Alchemilla_mollis",
    "https://en.wikipedia.org/wiki/Alder",
    "https://en.wikipedia.org/wiki/Alliaria_petiolata",
    "https://en.wikipedia.org/wiki/Allium",
    "https://en.wikipedia.org/wiki/Allium_caeruleum",
    "https://en.wikipedia.org/wiki/Allium_canadense",
    "https://en.wikipedia.org/wiki/Allium_cernuum",
    "https://en.wikipedia.org/wiki/Allium_cristophii",
    "https://en.wikipedia.org/wiki/Allium_giganteum",
    "https://en.wikipedia.org/wiki/Allium_moly",
    "https://en.wikipedia.org/wiki/Almond",
    "https://en.wikipedia.org/wiki/Alnus",
    "https://en.wikipedia.org/wiki/Alnus_glutinosa",
    "https://en.wikipedia.org/wiki/Alnus_incana",
    "https://en.wikipedia.org/wiki/Alnus_rhombifolia",
    "https://en.wikipedia.org/wiki/Aloe_aristata",
    "https://en.wikipedia.org/wiki/Aloe_vera",
    "https://en.wikipedia.org/wiki/Amaranth",
    "https://en.wikipedia.org/wiki/Amaranthus_caudatus",
    "https://en.wikipedia.org/wiki/Ambrosia",
    "https://en.wikipedia.org/wiki/Ambrosia_artemisiifolia",
    "https://en.wikipedia.org/wiki/Ambrosia_trifida",
    "https://en.wikipedia.org/wiki/Amelanchier",
    "https://en.wikipedia.org/wiki/Amelanchier_alnifolia",
    "https://en.wikipedia.org/wiki/Amelanchier_arborea",
    "https://en.wikipedia.org/wiki/Amelanchier_canadensis",
    "https://en.wikipedia.org/wiki/Amphipappus",
    "https://en.wikipedia.org/wiki/Angel_trumpet",
    "https://en.wikipedia.org/wiki/Anisocapparis_speciosa",
    "https://en.wikipedia.org/wiki/Anthriscus_sylvestris",
    "https://en.wikipedia.org/wiki/Apocynum_cannabinum",
    "https://en.wikipedia.org/wiki/Apple",
    "https://en.wikipedia.org/wiki/Apricot",
    "https://en.wikipedia.org/wiki/Aquilegia_vulgaris",
    "https://en.wikipedia.org/wiki/Arbutus",
    "https://en.wikipedia.org/wiki/Arbutus_unedo",
    "https://en.wikipedia.org/wiki/Argyreia_nervosa",
    "https://en.wikipedia.org/wiki/Asclepias",
    "https://en.wikipedia.org/wiki/Asclepias_amplexicaulis",
    "https://en.wikipedia.org/wiki/Asclepias_incarnata",
    "https://en.wikipedia.org/wiki/Asclepias_syriaca",
    "https://en.wikipedia.org/wiki/Asclepias_tuberosa",
    "https://en.wikipedia.org/wiki/Asclepias_verticillata",
    "https://en.wikipedia.org/wiki/Asimina_triloba",
    "https://en.wikipedia.org/wiki/Asparagus_setaceus",
    "https://en.wikipedia.org/wiki/Asplenium_flabellifolium",
    "https://en.wikipedia.org/wiki/Atropa_belladonna",
    "https://en.wikipedia.org/wiki/Azadirachta_indica",
    "https://en.wikipedia.org/wiki/Azolla",
    "https://en.wikipedia.org/wiki/Azolla_caroliniana",
    "https://en.wikipedia.org/wiki/Bamboo",
    "https://en.wikipedia.org/wiki/Banana",
    "https://en.wikipedia.org/wiki/Barbarea_verna",
    "https://en.wikipedia.org/wiki/Barbarea_vulgaris",
    "https://en.wikipedia.org/wiki/Bay_laurel",
    "https://en.wikipedia.org/wiki/Bean",
    "https://en.wikipedia.org/wiki/Beech",
    "https://en.wikipedia.org/wiki/Bellis_perennis",
    "https://en.wikipedia.org/wiki/Betula",
    "https://en.wikipedia.org/wiki/Betula_alleghaniensis",
    "https://en.wikipedia.org/wiki/Betula_lenta",
    "https://en.wikipedia.org/wiki/Betula_nigra",
    "https://en.wikipedia.org/wiki/Betula_papyrifera",
    "https://en.wikipedia.org/wiki/Betula_pendula",
    "https://en.wikipedia.org/wiki/Black_alder",
    "https://en.wikipedia.org/wiki/Blackberry",
    "https://en.wikipedia.org/wiki/Blueberry",
    "https://en.wikipedia.org/wiki/Botrychium_boreale",
    "https://en.wikipedia.org/wiki/Brachystegia_spiciformis",
    "https://en.wikipedia.org/wiki/Brassica_oleracea",
    "https://en.wikipedia.org/wiki/Brugmansia_suaveolens",
    "https://en.wikipedia.org/wiki/Buckeye_(tree)",
    "https://en.wikipedia.org/wiki/Buxus",
    "https://en.wikipedia.org/wiki/California_bay",
    "https://en.wikipedia.org/wiki/California_buckeye",
    "https://en.wikipedia.org/wiki/Camellia_sinensis",
    "https://en.wikipedia.org/wiki/Camellia_yunnanensis",
    "https://en.wikipedia.org/wiki/Cannabis",
    "https://en.wikipedia.org/wiki/Cannabis_indica",
    "https://en.wikipedia.org/wiki/Cannabis_ruderalis",
    "https://en.wikipedia.org/wiki/Cannabis_sativa",
    "https://en.wikipedia.org/wiki/Cardamine_bulbosa",
    "https://en.wikipedia.org/wiki/Cardamine_concatenata",
    "https://en.wikipedia.org/wiki/Cardamine_hirsuta",
    "https://en.wikipedia.org/wiki/Cardamine_pratensis",
    "https://en.wikipedia.org/wiki/Carduus_nutans",
    "https://en.wikipedia.org/wiki/Castilleja",
    "https://en.wikipedia.org/wiki/Castilleja_mutis",
    "https://en.wikipedia.org/wiki/Cattleya_schroederae",
    "https://en.wikipedia.org/wiki/Cedrus",
    "https://en.wikipedia.org/wiki/Cedrus_atlantica",
    "https://en.wikipedia.org/wiki/Cedrus_deodara",
    "https://en.wikipedia.org/wiki/Cercis",
    "https://en.wikipedia.org/wiki/Cercis_occidentalis",
    "https://en.wikipedia.org/wiki/Cercis_siliquastrum",
    "https://en.wikipedia.org/wiki/Chestnut",
    "https://en.wikipedia.org/wiki/Chrysanthemum_morifolium",
    "https://en.wikipedia.org/wiki/Cinnamomum_verum",
    "https://en.wikipedia.org/wiki/Cirsium_arvense",
    "https://en.wikipedia.org/wiki/Cladrastis_lutea",
    "https://en.wikipedia.org/wiki/Clematis_virginiana",
    "https://en.wikipedia.org/wiki/Clove",
    "https://en.wikipedia.org/wiki/Clover",
    "https://en.wikipedia.org/wiki/Coconut",
    "https://en.wikipedia.org/wiki/Coffea",
    "https://en.wikipedia.org/wiki/Coincya_monensis",
    "https://en.wikipedia.org/wiki/Cornus_(genus)",
    "https://en.wikipedia.org/wiki/Cornus_amomum",
    "https://en.wikipedia.org/wiki/Cornus_florida",
    "https://en.wikipedia.org/wiki/Cornus_kousa",
    "https://en.wikipedia.org/wiki/Cornus_nuttallii",
    "https://en.wikipedia.org/wiki/Corydalis",
    "https://en.wikipedia.org/wiki/Corydalis_aurea",
    "https://en.wikipedia.org/wiki/Corydalis_chelidoniifolia",
    "https://en.wikipedia.org/wiki/Corydalis_flavula",
    "https://en.wikipedia.org/wiki/Corydalis_lutea",
    "https://en.wikipedia.org/wiki/Corydalis_sempervirens",
    "https://en.wikipedia.org/wiki/Cucumber",
    "https://en.wikipedia.org/wiki/Curcuma_domestica",
    "https://en.wikipedia.org/wiki/Curcuma_zedoaria",
    "https://en.wikipedia.org/wiki/Cynodon_dactylon",
    "https://en.wikipedia.org/wiki/Cyperus_alternifolius",
    "https://en.wikipedia.org/wiki/Daucus_carota",
    "https://en.wikipedia.org/wiki/Digitalis_purpurea",
    "https://en.wikipedia.org/wiki/Dillenia_indica",
    "https://en.wikipedia.org/wiki/Dioscorea",
    "https://en.wikipedia.org/wiki/Dracunculus_vulgaris",
    "https://en.wikipedia.org/wiki/Durio_dulcis",
    "https://en.wikipedia.org/wiki/Durio_grandiflorus",
    "https://en.wikipedia.org/wiki/Durio_kutejensis",
    "https://en.wikipedia.org/wiki/Durio_testudinarius",
    "https://en.wikipedia.org/wiki/Durio_zibethinus",
    "https://en.wikipedia.org/wiki/Eastern_redbud",
    "https://en.wikipedia.org/wiki/Echinacea_paradoxa",
    "https://en.wikipedia.org/wiki/Encalypta",
    "https://en.wikipedia.org/wiki/Encelia_farinosa",
    "https://en.wikipedia.org/wiki/Epacris_longiflora",
    "https://en.wikipedia.org/wiki/Erigeron_cavernensis",
    "https://en.wikipedia.org/wiki/Erythronium_dens-canis",
    "https://en.wikipedia.org/wiki/Eucalyptus",
    "https://en.wikipedia.org/wiki/Euphorbia_peplus",
    "https://en.wikipedia.org/wiki/Excoecaria_agallocha",
    "https://en.wikipedia.org/wiki/Fabaceae",
    "https://en.wikipedia.org/wiki/Ficus",
    "https://en.wikipedia.org/wiki/Ficus_carica",
    "https://en.wikipedia.org/wiki/Flax",
    "https://en.wikipedia.org/wiki/Foeniculum_vulgare",
    "https://en.wikipedia.org/wiki/Fraxinus",
    "https://en.wikipedia.org/wiki/Fraxinus_americana",
    "https://en.wikipedia.org/wiki/Fraxinus_excelsior",
    "https://en.wikipedia.org/wiki/Fraxinus_nigra",
    "https://en.wikipedia.org/wiki/Fraxinus_pennsylvanica",
    "https://en.wikipedia.org/wiki/Fraxinus_quadrangulata",
    "https://en.wikipedia.org/wiki/Galanthus",
    "https://en.wikipedia.org/wiki/Gossypium",
    "https://en.wikipedia.org/wiki/Grapefruit",
    "https://en.wikipedia.org/wiki/Hedera",
    "https://en.wikipedia.org/wiki/Hedyscepe_canterburyana",
    "https://en.wikipedia.org/wiki/Helenium_amarum",
    "https://en.wikipedia.org/wiki/Helianthella",
    "https://en.wikipedia.org/wiki/Helleborus",
    "https://en.wikipedia.org/wiki/Hemp",
    "https://en.wikipedia.org/wiki/Heritiera_fomes",
    "https://en.wikipedia.org/wiki/Hesperis_matronalis",
    "https://en.wikipedia.org/wiki/Horseradish",
    "https://en.wikipedia.org/wiki/Hyacinthoides_non-scripta",
    "https://en.wikipedia.org/wiki/Hydrangea_macrophylla",
    "https://en.wikipedia.org/wiki/Hylocereus",
    "https://en.wikipedia.org/wiki/Ilex",
    "https://en.wikipedia.org/wiki/Ilex_aquifolium",
    "https://en.wikipedia.org/wiki/Ilex_decidua",
    "https://en.wikipedia.org/wiki/Ilex_glabra",
    "https://en.wikipedia.org/wiki/Ilex_verticillata",
    "https://en.wikipedia.org/wiki/Impatiens_capensis",
    "https://en.wikipedia.org/wiki/Impatiens_pallida",
    "https://en.wikipedia.org/wiki/Ipomoea_batatas",
    "https://en.wikipedia.org/wiki/Jasminum_officinale",
    "https://en.wikipedia.org/wiki/Juglans_californica",
    "https://en.wikipedia.org/wiki/Juncus_kraussii",
    "https://en.wikipedia.org/wiki/Juniper",
    "https://en.wikipedia.org/wiki/Koelreuteria_paniculata",
    "https://en.wikipedia.org/wiki/Laburnum",
    "https://en.wikipedia.org/wiki/Lambertia",
    "https://en.wikipedia.org/wiki/Lambertia_echinata",
    "https://en.wikipedia.org/wiki/Lambertia_ericifolia",
    "https://en.wikipedia.org/wiki/Lambertia_fairallii",
    "https://en.wikipedia.org/wiki/Lambertia_formosa",
    "https://en.wikipedia.org/wiki/Lambertia_ilicifolia",
    "https://en.wikipedia.org/wiki/Lambertia_inermis",
    "https://en.wikipedia.org/wiki/Lambertia_multiflora",
    "https://en.wikipedia.org/wiki/Lambertia_orbifolia",
    "https://en.wikipedia.org/wiki/Lambertia_rariflora",
    "https://en.wikipedia.org/wiki/Lamium",
    "https://en.wikipedia.org/wiki/Lamium_amplexicaule",
    "https://en.wikipedia.org/wiki/Lamium_maculatum",
    "https://en.wikipedia.org/wiki/Lamium_purpureum",
    "https://en.wikipedia.org/wiki/Lavandula",
    "https://en.wikipedia.org/wiki/Lemon",
    "https://en.wikipedia.org/wiki/Lettuce",
    "https://en.wikipedia.org/wiki/Lilium_catesbaei",
    "https://en.wikipedia.org/wiki/Limnanthes_douglasii",
    "https://en.wikipedia.org/wiki/Ludisia_discolor",
    "https://en.wikipedia.org/wiki/Lunaria_annua",
    "https://en.wikipedia.org/wiki/Lupinus",
    "https://en.wikipedia.org/wiki/Lupinus_elegans",
    "https://en.wikipedia.org/wiki/Lyonothamnus_floribundus",
    "https://en.wikipedia.org/wiki/Lysichiton",
    "https://en.wikipedia.org/wiki/Maclura_pomifera",
    "https://en.wikipedia.org/wiki/Magnolia",
    "https://en.wikipedia.org/wiki/Magnolia_figo",
    "https://en.wikipedia.org/wiki/Magnolia_grandiflora",
    "https://en.wikipedia.org/wiki/Magnolia_splendens",
    "https://en.wikipedia.org/wiki/Magnolia_stellata",
    "https://en.wikipedia.org/wiki/Magnolia_virginiana",
    "https://en.wikipedia.org/wiki/Maize",
    "https://en.wikipedia.org/wiki/Malus_domestica",
    "https://en.wikipedia.org/wiki/Mango",
    "https://en.wikipedia.org/wiki/Marijuana",
    "https://en.wikipedia.org/wiki/Mimosa_pudica",
    "https://en.wikipedia.org/wiki/Moringa_oleifera",
    "https://en.wikipedia.org/wiki/Morus_(plant)",
    "https://en.wikipedia.org/wiki/Morus_alba",
    "https://en.wikipedia.org/wiki/Morus_rubra",
    "https://en.wikipedia.org/wiki/Mucuna_pruriens",
    "https://en.wikipedia.org/wiki/Myosotis_arvensis",
    "https://en.wikipedia.org/wiki/Nardostachys_jatamansi",
    "https://en.wikipedia.org/wiki/Nephrolepis_exaltata",
    "https://en.wikipedia.org/wiki/Nephrolepis_obliterata",
    "https://en.wikipedia.org/wiki/Nicotiana",
    "https://en.wikipedia.org/wiki/Nicotiana_glauca",
    "https://en.wikipedia.org/wiki/Olive",
    "https://en.wikipedia.org/wiki/Oncosiphon_suffruticosum",
    "https://en.wikipedia.org/wiki/Onion",
    "https://en.wikipedia.org/wiki/Orange_(fruit)",
    "https://en.wikipedia.org/wiki/Oryza_glaberrima",
    "https://en.wikipedia.org/wiki/Oryza_sativa",
    "https://en.wikipedia.org/wiki/Oxalis",
    "https://en.wikipedia.org/wiki/Papaveraceae",
    "https://en.wikipedia.org/wiki/Parsley",
    "https://en.wikipedia.org/wiki/Pastinaca_sativa",
    "https://en.wikipedia.org/wiki/Pea",
    "https://en.wikipedia.org/wiki/Peach",
    "https://en.wikipedia.org/wiki/Peanut",
    "https://en.wikipedia.org/wiki/Pear",
    "https://en.wikipedia.org/wiki/Pentzia_incana",
    "https://en.wikipedia.org/wiki/Phaseolus",
    "https://en.wikipedia.org/wiki/Phoenicophorium",
    "https://en.wikipedia.org/wiki/Phormium_colensoi",
    "https://en.wikipedia.org/wiki/Phormium_tenax",
    "https://en.wikipedia.org/wiki/Physostegia_virginiana",
    "https://en.wikipedia.org/wiki/Phytolacca_americana",
    "https://en.wikipedia.org/wiki/Pine",
    "https://en.wikipedia.org/wiki/Pineapple",
    "https://en.wikipedia.org/wiki/Pinus_taeda",
    "https://en.wikipedia.org/wiki/Pistachio",
    "https://en.wikipedia.org/wiki/Plantago_major",
    "https://en.wikipedia.org/wiki/Platanus",
    "https://en.wikipedia.org/wiki/Platanus_occidentalis",
    "https://en.wikipedia.org/wiki/Platanus_racemosa",
    "https://en.wikipedia.org/wiki/Poaceae",
    "https://en.wikipedia.org/wiki/Polygala_calcarea",
    "https://en.wikipedia.org/wiki/Polypodium_scouleri",
    "https://en.wikipedia.org/wiki/Polystichum",
    "https://en.wikipedia.org/wiki/Polystichum_acrostichoides",
    "https://en.wikipedia.org/wiki/Polystichum_munitum",
    "https://en.wikipedia.org/wiki/Pomaderris_kumeraho",
    "https://en.wikipedia.org/wiki/Poppy",
    "https://en.wikipedia.org/wiki/Populus",
    "https://en.wikipedia.org/wiki/Potato",
    "https://en.wikipedia.org/wiki/Primula_vulgaris",
    "https://en.wikipedia.org/wiki/Prosopis",
    "https://en.wikipedia.org/wiki/Prosopis_glandulosa",
    "https://en.wikipedia.org/wiki/Prunus",
    "https://en.wikipedia.org/wiki/Prunus_avium",
    "https://en.wikipedia.org/wiki/Prunus_serotina",
    "https://en.wikipedia.org/wiki/Ptisana_salicina",
    "https://en.wikipedia.org/wiki/Pueraria_montana",
    "https://en.wikipedia.org/wiki/Quercus",
    "https://en.wikipedia.org/wiki/Quercus_agrifolia",
    "https://en.wikipedia.org/wiki/Quercus_alba",
    "https://en.wikipedia.org/wiki/Quercus_bicolor",
    "https://en.wikipedia.org/wiki/Quercus_canariensis",
    "https://en.wikipedia.org/wiki/Quercus_chrysolepis",
    "https://en.wikipedia.org/wiki/Quercus_coccinea",
    "https://en.wikipedia.org/wiki/Quercus_douglasii",
    "https://en.wikipedia.org/wiki/Quercus_kelloggii",
    "https://en.wikipedia.org/wiki/Quercus_macrocarpa",
    "https://en.wikipedia.org/wiki/Quercus_palustris",
    "https://en.wikipedia.org/wiki/Quercus_petraea",
    "https://en.wikipedia.org/wiki/Quercus_robur",
    "https://en.wikipedia.org/wiki/Quercus_rubra",
    "https://en.wikipedia.org/wiki/Quercus_suber",
    "https://en.wikipedia.org/wiki/Quercus_tomentella",
    "https://en.wikipedia.org/wiki/Quercus_velutina",
    "https://en.wikipedia.org/wiki/Ragweed",
    "https://en.wikipedia.org/wiki/Rapeseed",
    "https://en.wikipedia.org/wiki/Redwood_sorrel",
    "https://en.wikipedia.org/wiki/Reynoutria_japonica",
    "https://en.wikipedia.org/wiki/Rhanterium_epapposum",
    "https://en.wikipedia.org/wiki/Rhubarb",
    "https://en.wikipedia.org/wiki/Rice",
    "https://en.wikipedia.org/wiki/Rorippa_sylvestris",
    "https://en.wikipedia.org/wiki/Rosa_multiflora",
    "https://en.wikipedia.org/wiki/Rosa_virginiana",
    "https://en.wikipedia.org/wiki/Rose",
    "https://en.wikipedia.org/wiki/Rosemary",
    "https://en.wikipedia.org/wiki/Rubus",
    "https://en.wikipedia.org/wiki/Rubus_hispidus",
    "https://en.wikipedia.org/wiki/Rubus_occidentalis",
    "https://en.wikipedia.org/wiki/Rubus_pensilvanicus",
    "https://en.wikipedia.org/wiki/Rubus_phoenicolasius",
    "https://en.wikipedia.org/wiki/Rudbeckia_fulgida",
    "https://en.wikipedia.org/wiki/Rudbeckia_hirta",
    "https://en.wikipedia.org/wiki/Rudbeckia_laciniata",
    "https://en.wikipedia.org/wiki/Rudbeckia_triloba",
    "https://en.wikipedia.org/wiki/Rye",
    "https://en.wikipedia.org/wiki/Saffron",
    "https://en.wikipedia.org/wiki/Salix",
    "https://en.wikipedia.org/wiki/Salix_exigua",
    "https://en.wikipedia.org/wiki/Salix_gooddingii",
    "https://en.wikipedia.org/wiki/Sambucus",
    "https://en.wikipedia.org/wiki/Scorzonera_hispanica",
    "https://en.wikipedia.org/wiki/Screwbean_Mesquite",
    "https://en.wikipedia.org/wiki/Sempervivum_tectorum",
    "https://en.wikipedia.org/wiki/Senecio",
    "https://en.wikipedia.org/wiki/Senecio_aquaticus",
    "https://en.wikipedia.org/wiki/Senecio_cineraria",
    "https://en.wikipedia.org/wiki/Senecio_erucifolius",
    "https://en.wikipedia.org/wiki/Senecio_jacobaea",
    "https://en.wikipedia.org/wiki/Senecio_squalidus",
    "https://en.wikipedia.org/wiki/Sinapis_arvensis",
    "https://en.wikipedia.org/wiki/Solanum_americanum",
    "https://en.wikipedia.org/wiki/Solanum_carolinense",
    "https://en.wikipedia.org/wiki/Solanum_dulcamara",
    "https://en.wikipedia.org/wiki/Solanum_nigrum",
    "https://en.wikipedia.org/wiki/Solanum_opacum",
    "https://en.wikipedia.org/wiki/Sonchus_arvensis",
    "https://en.wikipedia.org/wiki/Sonchus_asper",
    "https://en.wikipedia.org/wiki/Sonchus_oleraceus",
    "https://en.wikipedia.org/wiki/Spikenard",
    "https://en.wikipedia.org/wiki/Strawberry",
    "https://en.wikipedia.org/wiki/Strelitzia_reginae",
    "https://en.wikipedia.org/wiki/Streptocarpus_sect._Saintpaulia",
    "https://en.wikipedia.org/wiki/Sugarcane",
    "https://en.wikipedia.org/wiki/Sunflower",
    "https://en.wikipedia.org/wiki/Sycamore",
    "https://en.wikipedia.org/wiki/Symphytum",
    "https://en.wikipedia.org/wiki/Symplocarpus_foetidus",
    "https://en.wikipedia.org/wiki/Synonym_(taxonomy)",
    "https://en.wikipedia.org/wiki/Tanacetum_parthenium",
    "https://en.wikipedia.org/wiki/Tanacetum_vulgare",
    "https://en.wikipedia.org/wiki/Thyme",
    "https://en.wikipedia.org/wiki/Thymus_(plant)",
    "https://en.wikipedia.org/wiki/Thymus_vulgaris",
    "https://en.wikipedia.org/wiki/Tomato",
    "https://en.wikipedia.org/wiki/Toxicodendron_radicans",
    "https://en.wikipedia.org/wiki/Trillium",
    "https://en.wikipedia.org/wiki/Trillium_cernuum",
    "https://en.wikipedia.org/wiki/Trillium_grandiflorum",
    "https://en.wikipedia.org/wiki/Trillium_ovatum",
    "https://en.wikipedia.org/wiki/Tulip",
    "https://en.wikipedia.org/wiki/Umbellularia_californica",
    "https://en.wikipedia.org/wiki/Urtica_dioica",
    "https://en.wikipedia.org/wiki/Vaccinium",
    "https://en.wikipedia.org/wiki/Vaccinium_ovatum",
    "https://en.wikipedia.org/wiki/Vaccinium_parvifolium",
    "https://en.wikipedia.org/wiki/Valley_oak",
    "https://en.wikipedia.org/wiki/Vanilla_(genus)",
    "https://en.wikipedia.org/wiki/Veratrum_album",
    "https://en.wikipedia.org/wiki/Veratrum_nigrum",
    "https://en.wikipedia.org/wiki/Veratrum_viride",
    "https://en.wikipedia.org/wiki/Veronica_arvensis",
    "https://en.wikipedia.org/wiki/Veronica_bullii",
    "https://en.wikipedia.org/wiki/Veronica_chamaedrys",
    "https://en.wikipedia.org/wiki/Viburnum",
    "https://en.wikipedia.org/wiki/Viburnum_prunifolium",
    "https://en.wikipedia.org/wiki/Viburnum_rhytidophyllum",
    "https://en.wikipedia.org/wiki/Viola_(plant)",
    "https://en.wikipedia.org/wiki/Vitis",
    "https://en.wikipedia.org/wiki/Walnut",
    "https://en.wikipedia.org/wiki/Western_redbud",
    "https://en.wikipedia.org/wiki/Wheat",
]

# Loop through the list of URLs and download HTML content
for url in urls:
    try:
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            html_content = response.text
            # Save or process the HTML content as needed
            # For example, you can save it to a file
            with open(r'C:\Users\sanct\Documents\FEUP\MEIC\1st year\1st semester\PRI\htmls'+f'\{url.split("/")[-1]}.html', 'w', encoding='utf-8') as file:
                file.write(html_content)
            print(f'Successfully downloaded {url}')
        else:
            print(f'Failed to download {url}. Status code: {response.status_code}')
    except Exception as e:
        print(f'An error occurred while downloading {url}: {str(e)}')