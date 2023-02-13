import polars as pl
from timeit import default_timer as timer

# col headers = 'cid,xcats,adjs,date,metric1,metric1,metric2,metric3,metric4

q_metrics = [f"METRIC_{i}" for i in range(5)]
q_dates = [f"DATE_{i}" for i in range(7000, 9500)]
q_cids = [f"CID_{i:03d}" for i in range(50, 75)]
q_xcats = [f"XCAT_{i}" for i in range(10)]
q_adj = [f"ADJ_{i}" for i in range(10)]

start = timer()

df = (
    pl.scan_csv("mock_db.csv")
    .filter(
        (pl.col("cid").is_in(q_cids))
        & (pl.col("xcats").is_in(q_xcats))
        & (pl.col("adjs").is_in(q_adj))
        & (pl.col("date").is_in(q_dates))
    )
    .select(q_metrics)
    .collect(streaming=True)
)

end = timer()
print(f"Time: {end - start}")
# Time: 15.347615900042001 seconds
