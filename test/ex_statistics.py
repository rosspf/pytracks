import pytracks.input
import pytracks.stats

tracks_wrapper = pytracks.input.TrackWrapper("event_25/Event_5.out", id_column=2, x_column=5, y_column=7, weight_column=3, worth_column=4, g_column=12, m_column=13, extra_ids=[12])

trackset = tracks_wrapper.gen_trackset()

print(pytracks.stats.gen_stats_trackset(trackset))