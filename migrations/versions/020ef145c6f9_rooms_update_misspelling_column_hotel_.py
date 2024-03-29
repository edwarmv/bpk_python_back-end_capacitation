"""rooms - update misspelling column hotel_uui to hotel_uuid.

Revision ID: 020ef145c6f9
Revises: 1dedd179cc99
Create Date: 2024-02-18 22:24:31.745155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '020ef145c6f9'
down_revision = '1dedd179cc99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('rooms', schema=None) as batch_op:
        batch_op.add_column(sa.Column('hotel_uuid', sa.Uuid(), nullable=False))
        batch_op.drop_constraint('rooms_hotel_uui_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'hotels', ['hotel_uuid'], ['uuid'])
        batch_op.drop_column('hotel_uui')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('rooms', schema=None) as batch_op:
        batch_op.add_column(sa.Column('hotel_uui', sa.UUID(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('rooms_hotel_uui_fkey', 'hotels', ['hotel_uui'], ['uuid'])
        batch_op.drop_column('hotel_uuid')

    # ### end Alembic commands ###
