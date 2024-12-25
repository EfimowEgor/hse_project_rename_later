from database import SessionLocal
from services.student_service import get_users
from services.program_service import get_programs
from services.stats_service import create_stats
import asyncio
from parse.parse_stats import main


async def run_parser():
    results = await main()
    db = SessionLocal()

    try:
        for pg_res in results:
            for res in pg_res:
                name, rating, g_mean, g_min, percentile, gpa, course, years, tp, modules, pg = res
                # name to id
                name_id = get_users(db, name)
                # program to id
                pg_id = get_programs(db, pg)

                stats = create_stats(db, 
                                     name_id, 
                                     rating,
                                     g_mean,
                                     g_min,
                                     percentile,
                                     gpa,
                                     course,
                                     years,
                                     tp,
                                     modules,
                                     pg_id)

            db.commit()
    except Exception as e:
        db.rollback()
        print(f"An error occurred: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    asyncio.run(run_parser())