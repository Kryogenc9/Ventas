"""empty message

Revision ID: 566f2cef1701
Revises: 8eb48cbe0546
Create Date: 2020-07-22 14:51:34.184832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '566f2cef1701'
down_revision = '8eb48cbe0546'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('venta_producto_id_venta_pk_fkey', 'venta_producto', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('venta_producto_id_venta_pk_fkey', 'venta_producto', 'ventas', ['id_venta_pk'], ['id_venta'])
    # ### end Alembic commands ###
