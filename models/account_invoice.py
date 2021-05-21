from odoo import fields, models, api


class AccountInvoice(models.Model):
  _inherit = "account.move"

  is_export = fields.Boolean(string='Es Exportación', required=False)
  fob_value = fields.Monetary(string='Valor Fob', compute='value_export', readonly=True, required=False)
  freight_value = fields.Monetary(string='Valor Carga', compute='value_export', readonly=True, required=False)
  insurance_value = fields.Monetary(string='Seguro', compute='value_export', readonly=True, required=False)
  cif_value = fields.Monetary(string='Valor CIF', compute='value_export', readonly=True, required=False)
  freight_exp = fields.Char(string='Carga', required=False)
  steam_besel = fields.Char(string='Barco', required=False)
  bl_nro = fields.Char(string='B/L #', required=False)
  shipment_point = fields.Char(string='Punto Envio', required=False)
  destination_final = fields.Char(string='Destino Final', required=False)
  shipped_via = fields.Char(string='Enviado Via', required=False)
  container = fields.Char(string='Contenedor', required=False)
  country_origin = fields.Many2one('res.country', string='Pais de Origen', required=False)
  discharged_port = fields.Char(string='Puerto de Descarga', required=False)

  manifest = fields.Char(string='Manifiesto', required=False)
  bundles = fields.Char(string='Valor Fob', required=False)
  pieces_total = fields.Float(string='Total Piezas', compute='total_pieces', readonly=True, required=False)
  custom_agent = fields.Char(string='Agente', required=False)
  landing = fields.Char(string='Landing', required=False)
  landing_type = fields.Char(string='Landing Type', required=False)
  ship_owner = fields.Char(string='Naviera', required=False)
  seal_ship = fields.Char(string='Sello #', required=False)

  exempt_purchase_nro = fields.Char(string="Nº Correlativo de orden de compra exenta:", required=False)
  record_sag = fields.Char(string='Nº Identificativo de registro de la SAG:	', required=False)
  const_record_exonerated = fields.Char(string='Nº Correlativo de constancia de registro exonerado:', required=False)

  @api.depends('amount_untaxed')
  def value_export(self):
    for r in self:
      if r.amount_untaxed and r.is_export:
        r.cif_value = r.amount_untaxed
        r.fob_value = r.amount_untaxed / 1.115
        r.freight_value = r.amount_untaxed * 0.10
        r.insurance_value = r.amount_untaxed * 0.015
      else:
        r.cif_value = 0
        r.fob_value = 0
        r.freight_value = 0
        r.insurance_value = 0

  @api.depends('amount_untaxed')
  def total_pieces(self):
    for r in self:
      total_pieces = 0.0
      for line in r.invoice_line_ids:
        total_pieces += line.quantity
      r.pieces_total = total_pieces
