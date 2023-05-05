import numpy as np
from matplotlib import pyplot as plt

from simulation import pbb_adv_win
from theoretical_analysis import pbb_adv_win_nakamoto, pbb_adv_win_grunspan, find_n

def save_plot(data: dict, title: str, xlabel: str, ylabel: str, filename: str, scatter: bool = True) -> None:
    plt.figure()
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if scatter:
        for p in data['plots']:
            plt.scatter(x=data['x'], y=p['y'], label=p['label'], s=10)
    else:
        for p in data['plots']:
            plt.plot(data['x'], p['y'], label=p['label'])

    plt.grid(visible=True)
    plt.legend(loc='upper left')
    plt.savefig(filename)
    plt.close()

def plot_pbb():
    n_values = [1, 3, 6, 12, 24, 48]
    q_values = [*np.arange(0.0, 0.5, 0.01)]

    for n in n_values:
        print(f"n={n}")
        nakamoto = list(map(lambda q: pbb_adv_win_nakamoto(n=n, q=q), q_values))
        grunspan = list(map(lambda q: pbb_adv_win_grunspan(n=n, q=q), q_values))
        data = {'x': q_values, 'plots':[{'y': nakamoto, 'label': "Nakamoto"},
                                        {'y': grunspan, 'label': "Grunspan"}]}
        save_plot(data=data, title=fr"$n={n}$", xlabel=r"$q$", ylabel=r"$P(n, q)$",
                  filename=f"plots/pbb_adversary_win_n={n}.png", scatter=False)
        save_plot(data=data, title=fr"$n={n}$", xlabel=r"$q$", ylabel=r"$P(n, q)$",
                  filename=f"plots/pbb_adversary_win_n={n}_scatter.png")

        experimental = list(map(lambda q: pbb_adv_win(n=n, q=q), q_values))
        data['plots'].append({'y': experimental, 'label': "Simulation"})
        save_plot(data=data, title=fr"$n={n}$", xlabel=r"$q$", ylabel=r"$P(n, q)$",
                  filename=f"plots/pbb_adversary_win_n={n}_with_simulation.png", scatter=False)
        save_plot(data=data, title=fr"$n={n}$", xlabel=r"$q$", ylabel=r"$P(n, q)$",
                  filename=f"plots/pbb_adversary_win_n={n}_with_simulation_scatter.png")
        data['plots'] = [{'y': experimental, 'label': "Simulation"}]
        save_plot(data=data, title=fr"$n={n}$", xlabel=r"$q$", ylabel=r"$P(n, q)$",
                  filename=f"plots/pbb_adversary_win_n={n}_only_simulation.png", scatter=False)
        save_plot(data=data, title=fr"$n={n}$", xlabel=r"$q$", ylabel=r"$P(n, q)$",
                  filename=f"plots/pbb_adversary_win_n={n}_only_simulation_scatter.png")
def plot_n():
    q_values = [*np.arange(0.0, 0.43, 0.01)]
    pbb_values = [0.001, 0.01, 0.1]
    for pbb in pbb_values:
        nakamoto = list(map(lambda q: find_n(pbb_adv_win=pbb, calc_pbb_method="nakamoto", q=q), q_values))
        grunspan = list(map(lambda q: find_n(pbb_adv_win=pbb, calc_pbb_method="grunspan", q=q), q_values))
        data = {'x': q_values, 'plots':[{'y': nakamoto, 'label': "Nakamoto"}, {'y': grunspan, 'label': "Grunspan"}]}
        save_plot(data=data, title=fr"$P(n, q)={pbb * 100}\%$", xlabel=r"$q$", ylabel=r"$n$",
                  filename=f"plots/find_n_pbb={pbb * 100}%.png", scatter=False)
        save_plot(data=data, title=fr"$P(n, q)={pbb * 100}\%$", xlabel=r"$q$", ylabel=r"$n$",
                  filename=f"plots/find_n_pbb={pbb * 100}%_scatter.png")

if __name__ == '__main__':
    plot_pbb()
    plot_n()

