import sys
import csv
import pygal

required_fields = ["Skeleton ID","Sex Assessment","Age Assessment","C ratio (collagen)","N ratio","Cemetery"]

def has_all_fields(d):
    for field in required_fields:
        if d[field] == '':
            return False
    return True

with open(sys.argv[1]) as f:
    rows = csv.DictReader(f)
    reduced_rows = map((lambda d: dict((k,d[k]) for k in required_fields if k in d)), rows)
    filtered_rows = list(filter((lambda d: has_all_fields(d)), reduced_rows))

    fig2_chart = pygal.XY(stroke=False,x_title="δ 13 C (‰ VPDB)",y_title="δ 15 N (‰ AIR)",xrange=(-24,-12),range=(1,15))
    fig2_chart.title = "Fig. 2"
    cemeteries = set(map((lambda d: d["Cemetery"]), list(filtered_rows)))
    for cemetery in cemeteries:
        rows_for_cemetery = filter(lambda d: d["Cemetery"] == cemetery, filtered_rows)
        xy_vals = list(map(lambda d: (float(d["C ratio (collagen)"]),float(d["N ratio"])), rows_for_cemetery))
        fig2_chart.add(cemetery, xy_vals)
    fig2_chart.render_to_png('./fig2.png')
