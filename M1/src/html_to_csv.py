import csv
from bs4 import BeautifulSoup
import pandas as pd
import os

# Initialize an empty list to store DataFrames for each HTML file
dfs = []

# List of HTML files to process
htmls = [
"Acacia.html",
"Acacia_ammobia.html",
"Acacia_estrophiolata.html",
"Acer_(genus).html",
"Acer_leucoderme.html",
"Acer_negundo.html",
"Acer_nigrum.html",
"Acer_pensylvanicum.html",
"Acer_saccharinum.html",
"Acer_saccharum.html",
"Achillea.html",
"Achillea_filipendulina.html",
"Achillea_millefolium.html",
"Achillea_ptarmica.html",
"Achillea_tomentosa.html",
"Adansonia.html",
"Adenanthos_obovatus.html",
"Adenium_obesum.html",
"Aesculus_californica.html",
"Agapanthus_praecox.html",
"Ajuga_reptans.html",
"Alchemilla_mollis.html",
"Alder.html",
"Alliaria_petiolata.html",
"Allium.html",
"Allium_caeruleum.html",
"Allium_canadense.html",
"Allium_cernuum.html",
"Allium_cristophii.html",
"Allium_giganteum.html",
"Allium_moly.html",
"Almond.html",
"Alnus.html",
"Alnus_glutinosa.html",
"Alnus_incana.html",
"Alnus_rhombifolia.html",
"Aloe_aristata.html",
"Aloe_vera.html",
"Amaranth.html",
"Amaranthus_caudatus.html",
"Ambrosia.html",
"Ambrosia_artemisiifolia.html",
"Ambrosia_trifida.html",
"Amelanchier.html",
"Amelanchier_alnifolia.html",
"Amelanchier_arborea.html",
"Amelanchier_canadensis.html",
"Amphipappus.html",
"Angel_trumpet.html",
"Anisocapparis_speciosa.html",
"Anthriscus_sylvestris.html",
"Apocynum_cannabinum.html",
"Apple.html",
"Apricot.html",
"Aquilegia_vulgaris.html",
"Arbutus.html",
"Arbutus_unedo.html",
"Argyreia_nervosa.html",
"Asclepias.html",
"Asclepias_amplexicaulis.html",
"Asclepias_incarnata.html",
"Asclepias_syriaca.html",
"Asclepias_tuberosa.html",
"Asclepias_verticillata.html",
"Asimina_triloba.html",
"Asparagus_setaceus.html",
"Asplenium_flabellifolium.html",
"Atropa_belladonna.html",
"Azadirachta_indica.html",
"Azolla.html",
"Azolla_caroliniana.html",
"Bamboo.html",
"Banana.html",
"Barbarea_verna.html",
"Barbarea_vulgaris.html",
"Bay_laurel.html",
"Bean.html",
"Beech.html",
"Bellis_perennis.html",
"Betula.html",
"Betula_alleghaniensis.html",
"Betula_lenta.html",
"Betula_nigra.html",
"Betula_papyrifera.html",
"Betula_pendula.html",
"Blackberry.html",
"Black_alder.html",
"Blueberry.html",
"Botrychium_boreale.html",
"Brachystegia_spiciformis.html",
"Brassica_oleracea.html",
"Brugmansia_suaveolens.html",
"Buckeye_(tree).html",
"Buxus.html",
"California_bay.html",
"California_buckeye.html",
"Camellia_sinensis.html",
"Camellia_yunnanensis.html",
"Cannabis.html",
"Cannabis_indica.html",
"Cannabis_ruderalis.html",
"Cannabis_sativa.html",
"Cardamine_bulbosa.html",
"Cardamine_concatenata.html",
"Cardamine_hirsuta.html",
"Cardamine_pratensis.html",
"Carduus_nutans.html",
"Castilleja.html",
"Castilleja_mutis.html",
"Cattleya_schroederae.html",
"Cedrus.html",
"Cedrus_atlantica.html",
"Cedrus_deodara.html",
"Cercis.html",
"Cercis_occidentalis.html",
"Cercis_siliquastrum.html",
"Chestnut.html",
"Chrysanthemum_morifolium.html",
"Cinnamomum_verum.html",
"Cirsium_arvense.html",
"Cladrastis_lutea.html",
"Clematis_virginiana.html",
"Clove.html",
"Clover.html",
"Coconut.html",
"Coffea.html",
"Coincya_monensis.html",
"Cornus_(genus).html",
"Cornus_amomum.html",
"Cornus_florida.html",
"Cornus_kousa.html",
"Cornus_nuttallii.html",
"Corydalis.html",
"Corydalis_aurea.html",
"Corydalis_chelidoniifolia.html",
"Corydalis_flavula.html",
"Corydalis_lutea.html",
"Corydalis_sempervirens.html",
"Cucumber.html",
"Curcuma_domestica.html",
"Curcuma_zedoaria.html",
"Cynodon_dactylon.html",
"Cyperus_alternifolius.html",
"Daucus_carota.html",
"Digitalis_purpurea.html",
"Dillenia_indica.html",
"Dioscorea.html",
"Dracunculus_vulgaris.html",
"Durio_dulcis.html",
"Durio_grandiflorus.html",
"Durio_kutejensis.html",
"Durio_testudinarius.html",
"Durio_zibethinus.html",
"Eastern_redbud.html",
"Echinacea_paradoxa.html",
"Encalypta.html",
"Encelia_farinosa.html",
"Epacris_longiflora.html",
"Erigeron_cavernensis.html",
"Erythronium_dens-canis.html",
"Eucalyptus.html",
"Euphorbia_peplus.html",
"Excoecaria_agallocha.html",
"Fabaceae.html",
"Ficus.html",
"Ficus_carica.html",
"Flax.html",
"Foeniculum_vulgare.html",
"Fraxinus.html",
"Fraxinus_americana.html",
"Fraxinus_excelsior.html",
"Fraxinus_nigra.html",
"Fraxinus_pennsylvanica.html",
"Fraxinus_quadrangulata.html",
"Galanthus.html",
"Gossypium.html",
"Grapefruit.html",
"Hedera.html",
"Hedyscepe_canterburyana.html",
"Helenium_amarum.html",
"Helianthella.html",
"Helleborus.html",
"Hemp.html",
"Heritiera_fomes.html",
"Hesperis_matronalis.html",
"Horseradish.html",
"Hyacinthoides_non-scripta.html",
"Hydrangea_macrophylla.html",
"Hylocereus.html",
"Ilex.html",
"Ilex_aquifolium.html",
"Ilex_decidua.html",
"Ilex_glabra.html",
"Ilex_verticillata.html",
"Impatiens_capensis.html",
"Impatiens_pallida.html",
"Ipomoea_batatas.html",
"Jasminum_officinale.html",
"Juglans_californica.html",
"Juncus_kraussii.html",
"Juniper.html",
"Koelreuteria_paniculata.html",
"Laburnum.html",
"Lambertia.html",
"Lambertia_echinata.html",
"Lambertia_ericifolia.html",
"Lambertia_fairallii.html",
"Lambertia_formosa.html",
"Lambertia_ilicifolia.html",
"Lambertia_inermis.html",
"Lambertia_multiflora.html",
"Lambertia_orbifolia.html",
"Lambertia_rariflora.html",
"Lamium.html",
"Lamium_amplexicaule.html",
"Lamium_maculatum.html",
"Lamium_purpureum.html",
"Lavandula.html",
"Lemon.html",
"Lettuce.html",
"Lilium_catesbaei.html",
"Limnanthes_douglasii.html",
"Ludisia_discolor.html",
"Lunaria_annua.html",
"Lupinus.html",
"Lupinus_elegans.html",
"Lyonothamnus_floribundus.html",
"Lysichiton.html",
"Maclura_pomifera.html",
"Magnolia.html",
"Magnolia_figo.html",
"Magnolia_grandiflora.html",
"Magnolia_splendens.html",
"Magnolia_stellata.html",
"Magnolia_virginiana.html",
"Maize.html",
"Malus_domestica.html",
"Mango.html",
"Marijuana.html",
"Mimosa_pudica.html",
"Moringa_oleifera.html",
"Morus_(plant).html",
"Morus_alba.html",
"Morus_rubra.html",
"Mucuna_pruriens.html",
"Myosotis_arvensis.html",
"Nardostachys_jatamansi.html",
"Nephrolepis_exaltata.html",
"Nephrolepis_obliterata.html",
"Nicotiana.html",
"Nicotiana_glauca.html",
"Olive.html",
"Oncosiphon_suffruticosum.html",
"Onion.html",
"Orange_(fruit).html",
"Oryza_glaberrima.html",
"Oryza_sativa.html",
"Oxalis.html",
"Papaveraceae.html",
"Parsley.html",
"Pastinaca_sativa.html",
"Pea.html",
"Peach.html",
"Peanut.html",
"Pear.html",
"Pentzia_incana.html",
"Phaseolus.html",
"Phoenicophorium.html",
"Phormium_colensoi.html",
"Phormium_tenax.html",
"Physostegia_virginiana.html",
"Phytolacca_americana.html",
"Pine.html",
"Pineapple.html",
"Pinus_taeda.html",
"Pistachio.html",
"Plantago_major.html",
"Platanus.html",
"Platanus_occidentalis.html",
"Platanus_racemosa.html",
"Poaceae.html",
"Polygala_calcarea.html",
"Polypodium_scouleri.html",
"Polystichum.html",
"Polystichum_acrostichoides.html",
"Polystichum_munitum.html",
"Pomaderris_kumeraho.html",
"Poppy.html",
"Populus.html",
"Potato.html",
"Primula_vulgaris.html",
"Prosopis.html",
"Prosopis_glandulosa.html",
"Prunus.html",
"Prunus_avium.html",
"Prunus_serotina.html",
"Ptisana_salicina.html",
"Pueraria_montana.html",
"Quercus.html",
"Quercus_agrifolia.html",
"Quercus_alba.html",
"Quercus_bicolor.html",
"Quercus_canariensis.html",
"Quercus_chrysolepis.html",
"Quercus_coccinea.html",
"Quercus_douglasii.html",
"Quercus_kelloggii.html",
"Quercus_macrocarpa.html",
"Quercus_palustris.html",
"Quercus_petraea.html",
"Quercus_robur.html",
"Quercus_rubra.html",
"Quercus_suber.html",
"Quercus_tomentella.html",
"Quercus_velutina.html",
"Ragweed.html",
"Rapeseed.html",
"Redwood_sorrel.html",
"Reynoutria_japonica.html",
"Rhanterium_epapposum.html",
"Rhubarb.html",
"Rice.html",
"Rorippa_sylvestris.html",
"Rosa_multiflora.html",
"Rosa_virginiana.html",
"Rose.html",
"Rosemary.html",
"Rubus.html",
"Rubus_hispidus.html",
"Rubus_occidentalis.html",
"Rubus_pensilvanicus.html",
"Rubus_phoenicolasius.html",
"Rudbeckia_fulgida.html",
"Rudbeckia_hirta.html",
"Rudbeckia_laciniata.html",
"Rudbeckia_triloba.html",
"Rye.html",
"Saffron.html",
"Salix.html",
"Salix_exigua.html",
"Salix_gooddingii.html",
"Sambucus.html",
"Scorzonera_hispanica.html",
"Screwbean_Mesquite.html",
"Sempervivum_tectorum.html",
"Senecio.html",
"Senecio_aquaticus.html",
"Senecio_cineraria.html",
"Senecio_erucifolius.html",
"Senecio_jacobaea.html",
"Senecio_squalidus.html",
"Sinapis_arvensis.html",
"Solanum_americanum.html",
"Solanum_carolinense.html",
"Solanum_dulcamara.html",
"Solanum_nigrum.html",
"Solanum_opacum.html",
"Sonchus_arvensis.html",
"Sonchus_asper.html",
"Sonchus_oleraceus.html",
"Spikenard.html",
"Strawberry.html",
"Strelitzia_reginae.html",
"Streptocarpus_sect._Saintpaulia.html",
"Sugarcane.html",
"Sunflower.html",
"Sycamore.html",
"Symphytum.html",
"Symplocarpus_foetidus.html",
"Synonym_(taxonomy).html",
"Tanacetum_parthenium.html",
"Tanacetum_vulgare.html",
"Thyme.html",
"Thymus_(plant).html",
"Thymus_vulgaris.html",
"Tomato.html",
"Toxicodendron_radicans.html",
"Trillium.html",
"Trillium_cernuum.html",
"Trillium_grandiflorum.html",
"Trillium_ovatum.html",
"Tulip.html",
"Umbellularia_californica.html",
"Urtica_dioica.html",
"Vaccinium.html",
"Vaccinium_ovatum.html",
"Vaccinium_parvifolium.html",
"Valley_oak.html",
"Vanilla_(genus).html",
"Veratrum_album.html",
"Veratrum_nigrum.html",
"Veratrum_viride.html",
"Veronica_arvensis.html",
"Veronica_bullii.html",
"Veronica_chamaedrys.html",
"Viburnum.html",
"Viburnum_prunifolium.html",
"Viburnum_rhytidophyllum.html",
"Viola_(plant).html",
"Vitis.html",
"Walnut.html",
"Western_redbud.html",
"Wheat.html"
]

html_files = []

current_dir = os.getcwd()
print(current_dir)

for html in htmls:
    html_files.append(os.path.join(current_dir, 'htmls', html))


for html_file in html_files:
    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the element with class "infobox biota"
    infobox = soup.find(class_='infobox biota')

    firstHeading = soup.find(id='firstHeading')

    # Extract the title from the firstHeading element
    name = firstHeading.text

    # Initialize lists to store header and content
    headers = []
    content = []

    headers.append("Name")
    content.append(name)

    if infobox:
        # Extract text from <tr> elements within the infobox
        clade_counter = {}  # To keep track of the number of occurrences for each "clade" header
        for row in infobox.find_all('tr'):
            # Remove content inside <small> tags
            for small in row.find_all('small'):
                small.extract()  # Remove the <small> tag and its content
            cells = row.find_all(['th', 'td'])
            if len(cells) == 2:
                header, value = [cell.get_text(strip=True) for cell in cells]
                if header == "Clade:":
                    if header in clade_counter:
                        clade_counter[header] += 1
                        header = f"{header}_{clade_counter[header]}"
                    else:
                        clade_counter[header] = 1
                headers.append(header)
                content.append(value)

                
    paragraphs = []
    headers.append("Text")
    for p_element in soup.find_all('p'):
        for ref_element in p_element.find_all('sup'):
            ref_element.extract()  # Remove the element
        # Check if the parent element is not a <td> tag
        if p_element.find_parent('td') is None:
            previous_element = p_element.find_previous_sibling()
            if previous_element is not None: 
                if previous_element.name == 'h2':
                    for edit_element in previous_element.find_all(class_='mw-editsection'):
                        edit_element.extract()  # Remove the element
                    header_text = previous_element.get_text(strip=True)
                    headers.append(header_text)
                    content.append('\n'.join(paragraphs))
                    paragraphs = []
                paragraphs.append(p_element.get_text())

    # Create a DataFrame for the current HTML file
    if headers and content:
        data_dict = dict(zip(headers, content))
        df = pd.DataFrame(data_dict, index=[0])
        dfs.append(df)

# Concatenate all DataFrames into a single DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# Save the combined data to a single CSV file
combined_df.to_csv(
    os.path.join(current_dir, '../data/combined_data.csv'),
    index=False,
    quoting=csv.QUOTE_ALL
)

print("Data from multiple HTML files extracted and saved to 'combined_data.csv'")
