"""
seed_data.py
Run this after running db_setup.py to populate the cloud_kitchen database with sample test data.
Usage: python seed_data.py
"""

import mysql.connector
from mysql.connector import Error

# ---- CONFIG: match your MySQL setup ----
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "root"
DB_NAME = "cloud_kitchen"


def get_connection():
    return mysql.connector.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME
    )


def seed_database():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        print("🌱 Seeding data into Cloud Kitchen database...\n")

        # 1. Customers
        customers_data = [
            ("Rahul Sharma", "9876543210", "rahul@gmail.com", "Salt Lake, Sector V, Kolkata"),
            ("Priya Sen", "9123456789", "priya.sen@yahoo.com", "Jadavpur, Kolkata"),
            ("Amit Das", "9988776655", "amit.das@gmail.com", "New Town, Action Area I, Kolkata")
        ]
        cursor.executemany(
            """INSERT INTO Customers (name, phone, email, address) 
               VALUES (%s, %s, %s, %s)""",
            customers_data
        )
        print("  ✅ Customers seeded.")

        # 2. Restaurants
        restaurants_data = [
            ("Spice Route Kitchen", "North Indian", 4.5, "Park Street, Kolkata", 120),
            ("Wok & Roll", "Chinese", 4.2, "Ballygunge, Kolkata", 85),
            ("Bakes & Burgers", "Fast Food", 4.7, "Salt Lake, Sector I, Kolkata", 210)
        ]
        cursor.executemany(
            """INSERT INTO Restaurants (name, cuisine_type, rating, location, total_orders) 
               VALUES (%s, %s, %s, %s, %s)""",
            restaurants_data
        )
        print("  ✅ Restaurants seeded.")

        # 3. Menus (restaurant_id 1, 2, 3)
        menus_data = [
            (1, "Butter Chicken", 350.00, "Main Course", True),
            (1, "Garlic Naan", 60.00, "Breads", True),
            (1, "Paneer Tikka", 280.00, "Starter", True),
            (2, "Veg Hakka Noodles", 220.00, "Main Course", True),
            (2, "Chicken Manchurian", 290.00, "Starter", True),
            (3, "Cheese Burger", 199.00, "Fast Food", True),
            (3, "French Fries", 120.00, "Sides", True)
        ]
        cursor.executemany(
            """INSERT INTO Menus (restaurant_id, item_name, price, category, is_available) 
               VALUES (%s, %s, %s, %s, %s)""",
            menus_data
        )
        print("  ✅ Menus seeded.")

        # 4. Drivers
        drivers_data = [
            ("Suresh Roy", "9055443322", "WB-02-AB-1234", True),
            ("Manoj Kumar", "9811223344", "WB-01-XY-5678", True),
            ("Subrata Ghosh", "9733221100", "WB-04-CD-9876", False)
        ]
        cursor.executemany(
            """INSERT INTO Drivers (name, phone, vehicle_no, is_available) 
               VALUES (%s, %s, %s, %s)""",
            drivers_data
        )
        print("  ✅ Drivers seeded.")

        # 5. Coupons
        coupons_data = [
            ("WELCOME50", 50.00, "2026-12-31"),
            ("SAVE20", 20.00, "2026-09-30")
        ]
        cursor.executemany(
            """INSERT INTO Coupons (code, discount_percent, valid_till) 
               VALUES (%s, %s, %s)""",
            coupons_data
        )
        print("  ✅ Coupons seeded.")

        # 6. Offers
        offers_data = [
            (1, "Flat 20% off on North Indian combos", 20.00),
            (3, "Free fries with every burger above ₹300", 15.00)
        ]
        cursor.executemany(
            """INSERT INTO Offers (restaurant_id, description, discount_percent) 
               VALUES (%s, %s, %s)""",
            offers_data
        )
        print("  ✅ Offers seeded.")

        # 7. Orders (customer_id, restaurant_id, total_amount, status, coupon_id)
        orders_data = [
            (1, 1, 410.00, 'Delivered', 1),
            (2, 2, 510.00, 'Preparing', None),
            (3, 3, 319.00, 'Placed', 2)
        ]
        cursor.executemany(
            """INSERT INTO Orders (customer_id, restaurant_id, total_amount, status, coupon_id) 
               VALUES (%s, %s, %s, %s, %s)""",
            orders_data
        )
        print("  ✅ Orders seeded.")

        # 8. Deliveries (order_id, driver_id, pickup_time, delivery_time, delivery_status)
        deliveries_data = [
            (1, 1, '2026-09-03 12:30:00', '2026-09-03 13:00:00', 'Delivered'),
            (2, 2, '2026-09-03 13:10:00', None, 'Assigned')
        ]
        cursor.executemany(
            """INSERT INTO Deliveries (order_id, driver_id, pickup_time, delivery_time, delivery_status) 
               VALUES (%s, %s, %s, %s, %s)""",
            deliveries_data
        )
        print("  ✅ Deliveries seeded.")

        # 9. Payments (order_id, amount, payment_mode, payment_status)
        payments_data = [
            (1, 410.00, 'UPI', 'Completed'),
            (2, 510.00, 'Card', 'Pending'),
            (3, 319.00, 'COD', 'Pending')
        ]
        cursor.executemany(
            """INSERT INTO Payments (order_id, amount, payment_mode, payment_status) 
               VALUES (%s, %s, %s, %s)""",
            payments_data
        )
        print("  ✅ Payments seeded.")

        # 10. Ratings (order_id, restaurant_id, customer_id, rating_value, review)
        ratings_data = [
            (1, 1, 1, 4.5, "Delicious butter chicken and hot naans!")
        ]
        cursor.executemany(
            """INSERT INTO Ratings (order_id, restaurant_id, customer_id, rating_value, review) 
               VALUES (%s, %s, %s, %s, %s)""",
            ratings_data
        )
        print("  ✅ Ratings seeded.")

        conn.commit()
        cursor.close()
        conn.close()
        print("\n🎉 Database successfully seeded with test data!")

    except Error as e:
        print(f"❌ Error seeding database: {e}")


if __name__ == "__main__":
    seed_database()