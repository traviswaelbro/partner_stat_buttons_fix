from openerp.osv import fields,osv

class res_partner(osv.osv):
    _inherit = 'res.partner'

    def _sale_order_count(self, cr, uid, ids, field_name, arg, context=None):
        res = dict(map(lambda x: (x,0), ids))
        # The current user may not have access rights for sale orders
        try:
            for partner in self.browse(cr, uid, ids, context):
                res[partner.id] = self.get_partner_sales(cr, uid, partner)
                for child in partner.mapped('child_ids'):
                    res[partner.id] += self.get_partner_sales(cr, uid, child)
        except Exception, e:
            pass

        return res

    def _sale_quote_count(self, cr, uid, ids, field_name, arg, context=None):
        res = dict(map(lambda x: (x,0), ids))
        # The current user may not have access rights for sale orders
        try:
            for partner in self.browse(cr, uid, ids, context):
                res[partner.id] = self.get_partner_quotes(cr, uid, partner)
                for child in partner.mapped('child_ids'):
                    res[partner.id] += self.get_partner_quotes(cr, uid, child)
        except Exception, e:
            print e
            pass
        return res

    _columns = {
        'sale_order_count': fields.function(_sale_order_count, string='# of Sales Order', type='integer'),
        'sale_quote_count': fields.function(_sale_quote_count, string='# of Quotes', type='integer'),
    }
