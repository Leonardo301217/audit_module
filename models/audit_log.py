from odoo import models, fields, api

class AuditLog(models.Model):
    _name = 'audit.log'
    _description = 'Registro de Auditoría'

    user_id = fields.Many2one('res.users', string='Usuario')
    action = fields.Char(string='Acción')
    model_name = fields.Char(string='Modelo')
    record_id = fields.Integer(string='ID del registro')
    date = fields.Datetime(string='Fecha', default=fields.Datetime.now)

# --- Listeners automáticos ---
class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def create(self, vals):
        record = super(SaleOrder, self).create(vals)
        self.env['audit.log'].create({
            'user_id': self.env.user.id,
            'action': 'Se creó un pedido de venta',
            'model_name': 'sale.order',
            'record_id': record.id
        })
        return record

    def write(self, vals):
        res = super(SaleOrder, self).write(vals)
        for record in self:
            self.env['audit.log'].create({
                'user_id': self.env.user.id,
                'action': 'Se modificó un pedido de venta',
                'model_name': 'sale.order',
                'record_id': record.id
            })
        return res

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model
    def create(self, vals):
        record = super(AccountMove, self).create(vals)
        self.env['audit.log'].create({
            'user_id': self.env.user.id,
            'action': 'Se creó una factura',
            'model_name': 'account.move',
            'record_id': record.id
        })
        return record

    def write(self, vals):
        res = super(AccountMove, self).write(vals)
        for record in self:
            self.env['audit.log'].create({
                'user_id': self.env.user.id,
                'action': 'Se modificó una factura',
                'model_name': 'account.move',
                'record_id': record.id
            })
        return res

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.model
    def create(self, vals):
        record = super(StockPicking, self).create(vals)
        self.env['audit.log'].create({
            'user_id': self.env.user.id,
            'action': 'Se creó un movimiento de inventario',
            'model_name': 'stock.picking',
            'record_id': record.id
        })
        return record

    def write(self, vals):
        res = super(StockPicking, self).write(vals)
        for record in self:
            self.env['audit.log'].create({
                'user_id': self.env.user.id,
                'action': 'Se modificó un movimiento de inventario',
                'model_name': 'stock.picking',
                'record_id': record.id
            })
        return res