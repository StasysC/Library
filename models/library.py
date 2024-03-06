from odoo import models, fields


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Books table'

    title = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description', required=True)
    page_no = fields.Integer(string='Pages', required=True)
    genre = fields.Selection([('fantasy', 'Fantasy'),
                              ('comic', 'Comic'),
                              ('drama', 'Drama'),
                              ('unknown', 'Unknown')], string='Genre', default='unknown')


