from odoo import models, fields


class PartnerXlsx(models.AbstractModel):
    _name = 'report.apotek.report_obat_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_laporan = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, supplier):
        # One sheet by partner
        sheet = workbook.add_worksheet('Daftar Obat')
        # Menambahkan informasi tanggal laporan
        sheet.write(0, 0, str(self.tgl_laporan))
        sheet.write(1, 0, 'ID Obat')
        sheet.write(1, 1, 'Nama Obat')
        sheet.write(1, 2, 'Katagori Obat')
        sheet.write(1, 3, 'Harga Obat')
        sheet.write(1, 4, 'Stok')
        sheet.write(1, 5, 'Supplier')
        
        row = 2
        col = 0
        for obj in supplier:
            col = 0
            # Text style bold, jjika tidak perlu bisa dihapus
            # bold = workbook.add_format({'bold': True})

            # write(row, col, title, style)
            # style bersifat opsional
            # sheet.write(0, 0, obj.name, bold)
            sheet.write(row, col, obj.id_obat)
            sheet.write(row, col + 1, obj.name)
            # sheet.write(row, col + 2, obj.kategoriobat_id)
            sheet.write(row, col + 3, obj.harga)
            sheet.write(row, col + 4, obj.stok)

            for item in obj.supplier_id:
                sheet.write(row, col + 5, item.name)
                col += 1
            row += 1