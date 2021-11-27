from django.db import models

# Create your models here.

class Koerperschaften(models.Model):
    """
    Liste der verwalteten Körperschaftstypen
    """
    koerperschaft = models.TextField(max_length = 150, unique=True, primary_key=True )
    
    def __str__(self):
        return self.koerperschaft

class Gemeinde(models.Model):
    """
    Stammdaten der verwalteten Gemeinden. Die Zahlen sollten mit der Nomenklatur im HKR übereinstimmen
    """
    gemeindenummer = models.IntegerField(primary_key=True, unique=True)
    koerperschaft = models.ForeignKey(Koerperschaften, on_delete = models.CASCADE)
    koerperschaft_ort = models.TextField(max_length=150, unique=False)

    def __str__(self):
        rueck = str(self.gemeindenummer) + "-" + str(self.koerperschaft) + " - " + str(self.koerperschaft_ort)
        return rueck
    

class Gemeindestatistik(models.Model):
    gemeinde = models.ForeignKey(Gemeinde, on_delete=models.CASCADE)
    haushaltsjahr = models.IntegerField()
    ew30_06 = models.IntegerField()
  

class DocxTemplates(models.Model):
    """
    Liste der Docx Templates die verwendet werden könnnen
    """

    gemeinde = models.ForeignKey(Gemeinde, on_delete=models.CASCADE)
    bezeichn = models.CharField(max_length=10)
    docxtemplate = models.FileField()
    
    def __str__(self):
        return self.bezeichn

class Datafiles(models.Model):
    
    datafilebez = models.CharField(max_length=100)
    datafile = models.FileField(upload_to='hh/data')
    datafileuploaddate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.datafilebez} - upload {self.datafileuploaddate}' 
    
    
class Haushalt(models.Model):
    """
    Stammdaten des verwalteten Haushaltsplans.
    """
    gemeinde = models.ForeignKey(Gemeinde, on_delete=models.CASCADE)
    haushaltsjahr = models.IntegerField()
    nachtragshaushalt = models.BooleanField(default = False)
    nachtragsnummer = models.IntegerField(blank=True, null=True)
    veroeffbuergbet = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    beschluss = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    genehmigung = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    veroeffhh = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    angelegt = models.DateTimeField(auto_now_add=True)
    doppelhaushalt = models.BooleanField(default=False)
    docxtemplate = models.ForeignKey(DocxTemplates, on_delete=models.CASCADE, blank=True, null=True)
    datendatei = models.ForeignKey(Datafiles, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        if self.nachtragshaushalt:
            nt = "NT" + str(self.nachtragsnummer)
        else:
            nt = "HH"
        rueck = str(self.gemeinde) + "-" + str(self.haushaltsjahr) + nt
        return rueck

# Modelle für die Haushaltssatzung

class Abgaben(models.Model):
    haushalt = models.ForeignKey(Haushalt, on_delete=models.CASCADE)
    gliederung = models.IntegerField()
    text = models.CharField(max_length=200)
    abgabesatz = models.DecimalField(max_digits=11, decimal_places=2)
    einheit = models.CharField(max_length=50)


# Modelle für den KFA


class Berechnungsgrundlagen(models.Model):
    haushaltsjahr = models.IntegerField(unique=True)
    nivellierungssatz_GrStA = models.IntegerField()
    nivellierungssatz_GrStB = models.IntegerField()
    nivellierungssatz_GewSt = models.IntegerField()
    landesdurchschnittliche_stk = models.DecimalField(max_digits=8, decimal_places=2)
    achwellenwertSZA = models.DecimalField(max_digits=8, decimal_places=2)
    schwellensatzSZA = models.DecimalField(max_digits=5, decimal_places=2)
    schluesselsatzb1 = models.DecimalField(max_digits=8, decimal_places=2)
    einheitlgrundbetragb2 = models.DecimalField(max_digits=8, decimal_places=2)
    einheitlgrundbetragb2inv = models.DecimalField(max_digits=8, decimal_places=2)
    landesdurchschnGebietsfl = models.DecimalField(max_digits=6, decimal_places=4)
    landesdurchschnittliche_stkFinAUmlage = models.DecimalField(max_digits=14, decimal_places=2)
    umlageZVS = models.DecimalField(max_digits=4, decimal_places=2)
    gewStumlageverf = models.DecimalField(max_digits=5, decimal_places=2)
    vgumlage = models.DecimalField(max_digits=5, decimal_places=2)
    kreisumlage = models.DecimalField(max_digits=5, decimal_places=2)
    
     


class Steuerkraft(models.Model):
    # Datenhaltung der Steuerkraftzahlen
	
    gemeinde = models.ForeignKey(Gemeinde, on_delete=models.CASCADE)
    haushaltsjahr = models.IntegerField()
    stk_grundsteuera = models.IntegerField()
    stk_grundsteuerb = models.IntegerField()
    stk_gewerbesteuer = models.IntegerField()
    stk_eksteuer = models.IntegerField()
    stk_usteuer = models.IntegerField()
    stk_ausgl = models.IntegerField()

    class Meta:
        unique_together = ['gemeinde', 'haushaltsjahr']
        

class Steuerkraftgrunddaten(models.Model):
    # Datenhaltung für die Steuerkraftberechnung. Herleitung der Steuerkraftzahlen aus den Werten der vierteljährlichen Finanzstatistik
	gemeinde = models.ForeignKey(Gemeinde, on_delete=models.CASCADE)
	haushaltsjahr = models.IntegerField()
	
	#GrundsteuerA
	ist1_grundsteuera = models.IntegerField()
	ist2_grundsteuera = models.IntegerField()
	ist3_grundsteuera = models.IntegerField()
	ber_grundsteuera = models.IntegerField()
	hs_grundsteuera = models.IntegerField()
	gz2_grundsteuera = models.IntegerField()

	ist4_grundsteueravj = models.IntegerField()
	ber_grundsteueravj = models.IntegerField()
	hs_grundsteueravj = models.IntegerField()
	gz1_grundsteueravj = models.IntegerField()
	nivs_grundsteuera = models.IntegerField()

	#GrundsteuerB	
	ist1_grundsteuerb = models.IntegerField()
	ist2_grundsteuerb = models.IntegerField()
	ist3_grundsteuerb = models.IntegerField()
	ber_grundsteuerb = models.IntegerField()
	hs_grundsteuerb = models.IntegerField()
	gz2_grundsteuerb = models.IntegerField()
	ist4vj_grundsteuerb = models.IntegerField()
	ber_grundsteuerbvj = models.IntegerField()
	hs_grundsteuerbvj = models.IntegerField()
	gz1_grundsteuerbvj = models.IntegerField()
	nivs_grundsteuerb = models.IntegerField()

	#Gewerbesteuer
	ist1_gewerbesteuer = models.IntegerField()
	ist2_gewserbeteuer = models.IntegerField()
	ist3_gewerbesteuer = models.IntegerField()
	hs_gewerbesteuer = models.IntegerField()

	ist4vj_gewerbesteuer = models.IntegerField()
	hs_gewerbesteuervj = models.IntegerField()

	# Einkommensteur
	ist1_eksteuer = models.IntegerField()
	ist2_eksteuer = models.IntegerField()
	ist3_eksteuer = models.IntegerField()
	ist4vj_eksteuer = models.IntegerField()

	# Umsatzsteuer
	ist1_usteuer = models.IntegerField()
	ist2_usteuer = models.IntegerField()
	ist3_usteuer = models.IntegerField()
	ist4vj_usteuer = models.IntegerField()

	# Ausgleichsleistungen gem. § 18 LFAG
	ist1_ausgl = models.IntegerField()
	ist2_ausgl = models.IntegerField()
	ist3_ausgl = models.IntegerField()
	ist4vj_ausgl = models.IntegerField()

class SchluesselzuweisungA(models.Model):
    """
    Verlauf der Schlüsselzuweisungen A
    """
    gemeinde = models.ForeignKey(Gemeinde, on_delete=models.CASCADE)
    haushaltsjahr = models.IntegerField()
    steuerkraftmesszahl = models.IntegerField()
    einwohner = models.IntegerField()
    stkproew = models.DecimalField(max_digits=11, decimal_places=2)
    landesdurchschnstkproew = models.DecimalField(max_digits=11, decimal_places=2)
    schwellenwert = models.DecimalField(max_digits=11, decimal_places=2)
    diff_stkproewschwellenwert = models.DecimalField(max_digits=11, decimal_places=2)
    schluesselzuw = models.IntegerField()

class SchluesselzuweisungB1(models.Model):
	gemeinde = models.ForeignKey(Gemeinde, on_delete=models.CASCADE)
	haushaltsjahr = models.IntegerField()
	szb1_satz = models.DecimalField(max_digits=11, decimal_places=2)
	szb1_betrag = models.IntegerField()

class SchluesselzuweisungB2(models.Model):
	gemeinde = models.ForeignKey(Gemeinde, on_delete=models.CASCADE)
	haushaltsjahr = models.IntegerField()
    
class SonderumlageGSgrundlagen(models.Model):
    haushaltsjahr = models.IntegerField()
    aufwandschulen = models.IntegerField()
    zinsaufwand = models.IntegerField()
    abrechnung = models.IntegerField()
    umlagesatz = models.DecimalField(max_digits=5, decimal_places=2)
    


# Modelle für die Haushaltsstatistik

class Eigenkapital(models.Model):
    """
    Eigenkpaital der Gemeinde im Zeitablauf und dessen Veränderung
    """
    gemeinde = models.ForeignKey(Gemeinde, on_delete=models.CASCADE, default=1)
    haushaltsjahr = models.IntegerField()
    anfangsbestand = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    veraend = models.DecimalField(max_digits=11, decimal_places=2)

class Ergebnisentwicklung(models.Model):
    gemeinde = models.ForeignKey(Gemeinde, on_delete=models.CASCADE)
    haushaltsjahr = models.IntegerField()
    ergvw = models.DecimalField(max_digits=11, decimal_places=2)
    ergfin = models.DecimalField(max_digits=11, decimal_places=2)
    ergao = models.DecimalField(max_digits=11, decimal_places=2)

class Finanzentwicklung(models.Model):
    """
    Pflichtangabe zum Vorbericht
    """
    gemeinde = models.ForeignKey(Gemeinde, on_delete=models.CASCADE)
    haushaltsjahr = models.IntegerField()
    jahreserg = models.DecimalField(max_digits=11, decimal_places=2)

class InvestKreditentwicklung(models.Model):
	
    gemeinde = models.ForeignKey(Gemeinde, on_delete=models.CASCADE)
    haushaltsjahr = models.IntegerField()
    anfangsbestand = models.DecimalField(max_digits=11, decimal_places=2)
    aufnahme = models.DecimalField(max_digits=11, decimal_places=2)
    tilgung = models.DecimalField(max_digits=11, decimal_places=2)
	

class LiqKreditentwicklung(models.Model):
    gemeinde = models.ForeignKey(Gemeinde, on_delete=models.CASCADE)
    haushaltsjahr = models.IntegerField()
    anfangsbestand = models.DecimalField(max_digits=11, decimal_places=2)
    aufnahme = models.DecimalField(max_digits=11, decimal_places=2)
    tilgung = models.DecimalField(max_digits=11, decimal_places=2)


class Investitionsentwicklung(models.Model):
    """
    Kennzahlen zu den Investitionen Statistik und Zeitreihenvergleich
    """
    
    gemeinde = models.ForeignKey(Gemeinde, on_delete=models.CASCADE,)
    haushaltsjahr = models.IntegerField()
    planinv = models.DecimalField(max_digits=11, decimal_places=2)
    istinv = models.DecimalField(max_digits=11, decimal_places=2)
    afa = models.DecimalField(max_digits=11, decimal_places=2)


# Modelle für einzelen Einnahmearten