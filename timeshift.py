#!/usr/bin/python
import sys

def main():
    print(' '.join(sys.argv))
    if (len(sys.argv)<3):
        print('opening timeshift ui')
        startUI()
        return None
    [time, zonecode, newZonecode]=sys.argv[len(sys.argv)-3:]
    answer = convert(time, zonecode, newZonecode)
    print(answer)
    return answer

#converts a string containing a time in hh:mm or h:mm format
#to a string containing the same time format converted from
#given zonecode to given newZonecode
def convert(time, zonecode, newZonecode):
    if (zonecode not in zones):
        print('the first zonecode was not recognized')
        return None
    if (newZonecode not in zones):
        print('the second zonecode was not recognized')
        return None
    totalSeconds=0
    if (":" in time):
        [hours,minutes]=time.split(":")
        totalSeconds=int(hours)*60*60+int(minutes)*60
    else:
        totalSeconds=float(time)*60*60
    convertedSeconds=totalSeconds+zones[newZonecode]-zones[zonecode]
    minutestring=str(int((60+convertedSeconds/60)%60));
    if (len(minutestring)==1):
        minutestring="0"+minutestring
    answer = str(int((convertedSeconds)/(60*60)))+":"+minutestring
    return answer

def startUI():
    import wx
    
    wxapp = wx.App()
    wxFrame = wx.Frame(None, -1 , 'Switch Time Zones', (0,0),(320,64))
    wxFrame.Centre()
    mainBox = wx.BoxSizer(wx.VERTICAL)
    wxFrame.SetSizer(mainBox)
    
    inputBox = wx.BoxSizer(wx.HORIZONTAL)
    mainBox.Add(inputBox, 1, wx.ALIGN_TOP | wx.EXPAND)
    outputBox = wx.BoxSizer(wx.HORIZONTAL)
    mainBox.Add(outputBox, 1, wx.ALIGN_BOTTOM | wx.EXPAND)
    
    inputBox.Add(wx.StaticText(wxFrame, label='Time:'), 0, wx.ALIGN_CENTRE_VERTICAL)
    timeText = wx.TextCtrl(wxFrame)
    timeText.SetValue('12:00')
    inputBox.Add(timeText,1)
    
    inputBox.Add(wx.StaticText(wxFrame, label='From:'), 0, wx.ALIGN_CENTRE_VERTICAL)
    fromZone = wx.TextCtrl(wxFrame)
    fromZone.SetValue('GMT')
    inputBox.Add(fromZone,1)
    
    inputBox.Add(wx.StaticText(wxFrame, label='To:'), 0, wx.ALIGN_CENTRE_VERTICAL)
    toZone = wx.TextCtrl(wxFrame)
    toZone.SetValue('GMT')
    inputBox.Add(toZone,1)
    
    submitButton = wx.Button(wxFrame,label='solve:')
    outputBox.Add(submitButton,0)
    outputText = wx.TextCtrl(wxFrame)
    outputText.SetEditable(False)
    outputBox.Add(outputText,1)

    def submit(event):
        outputText.SetValue(convert(timeText.GetValue(),fromZone.GetValue(),toZone.GetValue()))
    
    submitButton.Bind(wx.EVT_BUTTON, submit)
    
    wxFrame.Show()
    wxapp.MainLoop()

#the remainder of this file is a dictionary of time zones,
#followed by a call to main()
zones={
'WET':0,
'CET':3600,
'CEST':7200,
'LMT':13272,
'GST':14400,
'AFT':14400,
'EST':-18000,
'AST':-14400,
'YERT':10800,
'YERST':18000,
'AMST':14400,
'AMT':10800,
'AOT':3124,
'WAT':3600,
'NZST':43200,
'NZDT':46800,
'ROTT':-10800,
'ARST':-10800,
'ART':-14400,
'CLT':-14400,
'CLST':-10800,
'MAWT':21600,
'DAVT':25200,
'WST':28800,
'CAST':39600,
'VOST':21600,
'PMT':36000,
'DDUT':36000,
'SYOT':10800,
'CMT':-15408,
'WART':-14400,
'WARST':-10800,
'SAMT':-41400,
'NST':-39600,
'BST':-39600,
'SST':-39600,
'LHST':37800,
'MIST':39600,
'CST':34200,
'CWST':31500,
'ANT':-16200,
'HMT':5992,
'EET':7200,
'EEST':10800,
'BAKT':10800,
'BAKST':18000,
'AZST':14400,
'AZT':10800,
'BMT':-14309,
'ADT':-10800,
'BURT':23400,
'IST':19800,
'DACT':21600,
'BDT':21600,
'BDST':25200,
'WEST':3600,
'GMT':0,
'CAT':7200,
'BNT':27000,
'BOST':-12756,
'BOT':-14400,
'FNT':-7200,
'FNST':-3600,
'BRT':-10800,
'BRST':-7200,
'ACT':-18000,
'ACST':-14400,
'EDT':-14400,
'BTT':21600,
'SAST':5400,
'MMT':6600,
'MSK':10800,
'MSD':14400,
'FET':10800,
'CHDT':-19800,
'CDT':-18000,
'NDT':-9052,
'NWT':-9000,
'NPT':-9000,
'NDDT':-5400,
'AWT':-10800,
'APT':-10800,
'ADDT':-7200,
'EWT':-14400,
'EPT':-14400,
'EDDT':-10800,
'CDDT':-14400,
'CWT':-18000,
'CPT':-18000,
'MST':-25200,
'MDT':-21600,
'MWT':-21600,
'MPT':-21600,
'MDDT':-18000,
'PST':-28800,
'PDDT':-21600,
'PDT':-25200,
'PWT':-25200,
'PPT':-25200,
'YST':-32400,
'YDT':-28800,
'YWT':-28800,
'YPT':-28800,
'YDDT':-25200,
'CCT':23400,
'CKT':-37800,
'CKHST':-34200,
'SMT':-16966,
'EMT':-26248,
'EASST':-21600,
'EAST':-25200,
'CHAT':30600,
'LONT':25200,
'URUT':21600,
'KAST':19800,
'COT':-18000,
'COST':-14400,
'SJMT':-20173,
'CVT':-7200,
'CVST':-3600,
'CXT':25200,
'CEMT':10800,
'EAT':10800,
'SDMT':-16800,
'EHDT':-16200,
'QMT':-18840,
'ECT':-18000,
'GALT':-21600,
'TMT':5940,
'ADMT':9320,
'WEMT':7200,
'CANT':-3600,
'FJT':43200,
'FJST':46800,
'FKT':-14400,
'FKST':-10800,
'CHUT':36000,
'PONT':39600,
'KOST':39600,
'TBMT':10756,
'TBIT':10800,
'TBIST':18000,
'GEST':14400,
'GET':10800,
'GFT':-14400,
'GHST':1200,
'WGT':-10800,
'WGST':-7200,
'CGT':-7200,
'CGST':-3600,
'EGST':0,
'EGT':-3600,
'ChST':36000,
'GBGT':-13500,
'GYT':-13500,
'HKT':28800,
'HKST':32400,
'JST':32400,
'PPMT':-17340,
'JMT':25632,
'JAVT':26400,
'WIT':27000,
'CIT':28800,
'EIT':32400,
'DMT':-1521,
'IDT':10800,
'IDDT':14400,
'IOT':18000,
'IRST':12600,
'IRDT':18000,
'RMT':-5268,
'ISST':0,
'KMT':-18432,
'CJT':32400,
'JDT':36000,
'BEAT':9000,
'BEAUT':9900,
'FRUT':18000,
'FRUST':25200,
'KGT':18000,
'KGST':21600,
'ICT':25200,
'GILT':43200,
'PHOT':-43200,
'LINT':-38400,
'KST':30600,
'KDT':32400,
'ALMT':18000,
'ALMST':25200,
'KIZT':14400,
'KIZST':21600,
'QYZT':18000,
'QYZST':25200,
'AKTT':14400,
'AKTST':21600,
'AQTT':18000,
'AQTST':21600,
'FORT':14400,
'SHET':18000,
'SHEST':21600,
'URAT':14400,
'URAST':21600,
'ORAT':14400,
'ORAST':18000,
'IHST':21600,
'LKT':23400,
'LRT':-2670,
'WMT':5040,
'LST':9384,
'MHT':39600,
'KWAT':-43200,
'ULAT':25200,
'ULAST':32400,
'HOVT':21600,
'HOVST':28800,
'CHOST':36000,
'CHOT':32400,
'MOT':28800,
'MOST':32400,
'FFMT':-14660,
'MUT':14400,
'MUST':18000,
'MVT':18000,
'MALT':25200,
'MALST':26400,
'MYT':28800,
'BORT':27000,
'BORTST':30000,
'SWAT':5400,
'WAST':7200,
'NCT':39600,
'NCST':43200,
'NMT':40320,
'NFT':41400,
'NEST':4800,
'NET':1200,
'NRT':41400,
'NUT':-40800,
'NZMT':41400,
'CHAST':45900,
'CHADT':49500,
'PET':-18000,
'PEST':-14400,
'TAHT':-36000,
'MART':-34200,
'GAMT':-32400,
'PGT':36000,
'PHT':28800,
'PHST':32400,
'KART':18000,
'PKT':18000,
'PKST':21600,
'PMST':-10800,
'PMDT':-7200,
'PNT':-30600,
'FMT':-4056,
'MADT':-3600,
'MADST':0,
'MADMT':3600,
'AZOT':-7200,
'AZOST':-3600,
'AZOMT':0,
'PYT':-14400,
'PYST':-10800,
'RET':14400,
'MDST':16248,
'TSAT':10800,
'STAT':10800,
'VOLT':14400,
'VOLST':18000,
'KUYT':14400,
'KUYST':18000,
'SAMST':18000,
'SVET':14400,
'SVEST':21600,
'YEKT':18000,
'YEKST':21600,
'OMST':18000,
'OMSST':25200,
'NOVT':21600,
'NOVST':28800,
'KRAT':21600,
'KRAST':28800,
'IMT':25040,
'IRKT':25200,
'IRKST':32400,
'YAKT':28800,
'YAKST':36000,
'VLAT':36000,
'VLAST':39600,
'VLASST':36000,
'SAKT':39600,
'SAKST':43200,
'MAGST':43200,
'MAGT':39600,
'PETT':39600,
'PETST':46800,
'ANAT':43200,
'ANAST':50400,
'SBT':39600,
'SCT':14400,
'SGT':27000,
'SLST':-1200,
'NEGT':-12600,
'SRT':-12600,
'TFT':18000,
'DUST':18000,
'DUSST':25200,
'TJT':18000,
'TKT':-39600,
'TLT':28800,
'ASHT':14400,
'ASHST':21600,
'TOT':44400,
'TOST':50400,
'TRST':14400,
'TRT':10800,
'TVT':43200,
'CUT':8400,
'HST':-36000,
'WAKT':43200,
'CAWT':-32400,
'CAPT':-32400,
'AHST':-36000,
'AHDT':-32400,
'AKST':-32400,
'AKDT':-28800,
'HAST':-36000,
'HADT':-32400,
'MeST':-28800,
'HDT':-34200,
'UYT':-12600,
'UYHST':-10800,
'UYST':-7200,
'TAST':21600,
'UZST':21600,
'UZT':18000,
'TASST':25200,
'VET':-16200,
'VUT':39600,
'VUST':43200,
'WFT':43200,
'WSDT':-36000
}

main()
