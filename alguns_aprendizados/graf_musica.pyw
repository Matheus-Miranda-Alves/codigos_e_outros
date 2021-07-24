import matplotlib.pyplot as plt;
plt.rcdefaults
import numpy as np;
musica = ('Lib Provisória','Sentadão','Combatchy','Surtada', 'Cheirosa');
indice = np.arange(len(musica));
acessos = [1068254,866216,849895,763652,758198];
plt.bar(indice,acessos);
plt.xticks(indice,musica);
plt.ylabel('Acessos');
plt.title('Ranking do Spotify 31.dez.2019');
plt.show()