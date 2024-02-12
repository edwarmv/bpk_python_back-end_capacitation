"""Initial migration.

Revision ID: 1dedd179cc99
Revises: 
Create Date: 2024-02-01 22:30:43.778516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1dedd179cc99'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flights',
    sa.Column('uuid', sa.Uuid(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('airlane_name', sa.String(length=20), nullable=False),
    sa.Column('from_location', sa.String(length=60), nullable=False),
    sa.Column('to_location', sa.String(length=60), nullable=False),
    sa.Column('departure_time', sa.DateTime(), nullable=False),
    sa.Column('arrival_time', sa.DateTime(), nullable=False),
    sa.Column('total_seats', sa.SmallInteger(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('canceled', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('hotels',
    sa.Column('uuid', sa.Uuid(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('country', sa.String(length=30), nullable=False),
    sa.Column('city', sa.String(length=40), nullable=False),
    sa.Column('address', sa.String(length=60), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('users',
    sa.Column('uuid', sa.Uuid(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('full_name', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.Column('role', sa.String(length=20), nullable=False),
    sa.Column('deleted', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('flights_booking',
    sa.Column('uuid', sa.Uuid(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('number_seats', sa.SmallInteger(), nullable=False),
    sa.Column('canceled', sa.Boolean(), nullable=False),
    sa.Column('flight_uuid', sa.Uuid(), nullable=False),
    sa.Column('user_uuid', sa.Uuid(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['flight_uuid'], ['flights.uuid'], ),
    sa.ForeignKeyConstraint(['user_uuid'], ['users.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('rooms',
    sa.Column('uuid', sa.Uuid(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('room_type', sa.String(length=30), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('number_guests', sa.SmallInteger(), nullable=False),
    sa.Column('available', sa.Boolean(), nullable=False),
    sa.Column('deleted', sa.Boolean(), nullable=False),
    sa.Column('hotel_uui', sa.Uuid(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['hotel_uui'], ['hotels.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('rooms_booking',
    sa.Column('uuid', sa.Uuid(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('from_date', sa.Date(), nullable=False),
    sa.Column('to_date', sa.Date(), nullable=False),
    sa.Column('canceled', sa.Boolean(), nullable=False),
    sa.Column('user_uuid', sa.Uuid(), nullable=False),
    sa.Column('room_uuid', sa.Uuid(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['room_uuid'], ['rooms.uuid'], ),
    sa.ForeignKeyConstraint(['user_uuid'], ['users.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rooms_booking')
    op.drop_table('rooms')
    op.drop_table('flights_booking')
    op.drop_table('users')
    op.drop_table('hotels')
    op.drop_table('flights')
    # ### end Alembic commands ###