from numpy.random import rand as RandomFloatArray
from tqdm import tqdm


def generate_complete_dataset(
    outfile="mock_db.csv",
    max_cids=100,
    max_xcats=10,
    max_adjs=10,
    max_metrics=5,
    max_dates=12000,
):

    print(
        f"Generating dataset with {max_cids} cids, {max_xcats} xcats, {max_adjs} adjs, {max_metrics} metrics, {max_dates} dates"
    )

    cids = [f"CID_{i:03d}" for i in range(max_cids)]
    xcats = [f"XCAT_{i}" for i in range(max_xcats)]
    adjs = [f"ADJ_{i}" for i in range(max_adjs)]
    dates = [f"DATE_{n}" for n in range(n)]
    metrics = [f"METRIC_{i}" for i in range(n)]
    with open(outfile, "w", encoding="utf-8") as f:
        f.write("cid,xcats,adjs,date," + ",".join(metrics) + "\n")
        for cid in tqdm(cids):
            for xcat in xcats:
                for adj in adjs:
                    for date in dates:
                        rands = ((RandomFloatArray(max_metrics) - 1) * 10).tolist()
                        f.write(
                            ",".join([cid, xcat, adj, date] + [str(r) for r in rands])
                            + "\n"
                        )

    with open(outfile + ".meta", "w", encoding="utf-8") as f:
        f.write(f"max_cids={max_cids}\n")
        f.write(f"[{','.join([cids[0] + '...' + cids[-1]])}]\n")
        f.write(f"max_xcats={max_xcats}\n")
        f.write(f"[{','.join([xcats[0] + '...' + xcats[-1]])}]\n")
        f.write(f"max_adjs={max_adjs}\n")
        f.write(f"[{','.join([adjs[0] + '...' + adjs[-1]])}]\n")
        f.write(f"max_metrics={max_metrics}\n")
        f.write(f"[{','.join([metrics[0] + '...' + metrics[-1]])}]\n")
        f.write(f"max_dates={max_dates}\n")
        f.write(f"[{','.join([dates[0] + '...' + dates[-1]])}]\n")


generate_complete_dataset()
