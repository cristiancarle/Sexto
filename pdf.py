# Como no podemos usar `set_doc_option`, cambiamos a una fuente que soporte UTF-8 explícitamente (como DejaVuSans)
# Primero cargamos una fuente TTF personalizada que soporte caracteres Unicode

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Cargar fuente TrueType con soporte UTF-8
pdf.add_font("DejaVu", "", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", uni=True)
pdf.set_font("DejaVu", "", 11)

for title, body in content:
    pdf.set_font("DejaVu", "B", 12)
    pdf.chapter_title(title)
    pdf.set_font("DejaVu", "", 11)
    pdf.chapter_body(body)

filename = "/mnt/data/Guia_apktool_WhatsApp_Cristian.pdf"
pdf.output(filename)
