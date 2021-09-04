from django.db import models

# Create your models here.

class Gemeinde(models):
    """
    Stammdaten der verwalteten Gemeinden. Die Zahlen sollten mit der Nomenklatur im HKR übereinstimmen
    """
    gemeindenummer = models.IntegerField(primary_key=True)
    koerperschaft = models.TextField(max_length = 50)
    koerperschaft_ort = models.TextField(max_length=150)

    def __str__(self):
        rueck = str(self.gemeindenummer) + "-" + str(self.koerperschaft) + " - " + str(self.koerperschaft_ort)
        return rueck


class Haushalt(models):
    """
    Stammdaten des verwalteten Haushaltsplans.
    """
    gemeinde = models.ForeignKey(Gemeinde)
    haushaltsjahr = models.IntegerField()
    nachtragshaushalt = models.BooleanField(default = False)
    nachtragsnummer = models.IntegerField(blank=True)
    veroeffbuergbet = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True)
    beschluss = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True)
    genehmigung = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True)
    veroeffhh = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True)
    angelegt = models.DateTimeField(auto_now_add=True)
    doppelhaushalt = models.BooleanField(default=False)

    def __str__(self):
        if self.nachtragshaushalt:
            nt = "NT" + str(self.nachtragsnummer)
        else:
            nt = "HH"
        rueck = str(self.gemeinde) + "-" + str(self.haushaltsjahr) + nt
        return rueck


# Modelle für den KFA







# Modelle für Gesamtübersichten

class Eigenkapital(models):
	gemeinde = models.ForeignKey('Gemeinde', on_delete=models.CASCADE,)
	haushaltsjahr = models.IntegerField()
	anfangsbestand = models.Decimal(max_digits=11, decimal_places=2)
	veraend = models.Decimal(max_digits=11, decimal_places=2)

class Ergebnisentwicklung(models):
	gemeinde = models.ForeignKey('Gemeinde', on_delete=models.CASCADE,)
	haushaltsjahr = models.IntegerField()
	


class Finanzentwicklung(models):
	gemeinde = models.ForeignKey('Gemeinde', on_delete=models.CASCADE,)
	haushaltsjahr = models.IntegerField()
	jahreserg = models.Decimal(max_digits=11, decimal_places=2)


class InvestKreditentwicklung(models):
	
    gemeinde = models.ForeignKey(Gemeinde, on_delete=models.CASCADE)
    haushaltsjahr = models.IntegerField()
    anfangsbestand = models.DecimalField(max_digits=11, decimal_places=2)
    aufnahme = models.DecimalField(max_digits=11, decimal_places=2)
    tilgung = models.DecimalField(max_digits=11, decimal_places=2)
	

class LiqKreditentwicklung(models):
	gemeinde = models.ForeignKey('Gemeinde', on_delete=models.CASCADE,)
	haushaltsjahr = models.IntegerField()



class Investitionsentwicklung(models):
	gemeinde = models.ForeignKey('Gemeinde', on_delete=models.CASCADE,)
	haushaltsjahr = models.IntegerField()



# Modelle für einzelen Einnahmearten










