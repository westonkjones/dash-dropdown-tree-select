import dash_dropdown_tree_select
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash(__name__)

data = [
  {
    "label": "VP Accounting",
    "tagClassName": "special",
    "children": [
      {
        "label": "iWay",
        "children": [
          {
            "label": "Universidad de Especialidades del Espíritu Santo"
          },
          {
            "label": "Marmara University"
          },
          {
            "label": "Baghdad College of Pharmacy"
          }
        ]
      },
      {
        "label": "KDB",
        "children": [
          {
            "label": "Latvian University of Agriculture"
          },
          {
            "label": "Dublin Institute of Technology"
          }
        ]
      },
      {
        "label": "Justice",
        "children": [
          {
            "label": "Baylor University"
          },
          {
            "label": "Massachusetts College of Art"
          },
          {
            "label": "Universidad Técnica Latinoamericana"
          },
          {
            "label": "Saint Louis College"
          },
          {
            "label": "Scott Christian University"
          }
        ]
      },
      {
        "label": "Utilization Review",
        "children": [
          {
            "label": "University of Minnesota - Twin Cities Campus"
          },
          {
            "label": "Moldova State Agricultural University"
          },
          {
            "label": "Andrews University"
          },
          {
            "label": "Usmanu Danfodiyo University Sokoto"
          }
        ]
      },
      {
        "label": "Norton Utilities",
        "children": [
          {
            "label": "Universidad Autónoma del Caribe"
          },
          {
            "label": "National University of Uzbekistan"
          },
          {
            "label": "Ladoke Akintola University of Technology"
          },
          {
            "label": "Kohat University of Science and Technology  (KUST)"
          },
          {
            "label": "Hvanneyri Agricultural University"
          }
        ]
      }
    ]
  },
  {
    "label": "Database Administrator III",
    "children": [
      {
        "label": "TFS",
        "children": [
          {
            "label": "University of Jazeera"
          },
          {
            "label": "Technical University of Crete"
          },
          {
            "label":
              "Ecole Nationale Supérieure d'Agronomie et des Industries Alimentaires"
          },
          {
            "label": "Ho Chi Minh City University of Natural Sciences"
          }
        ]
      },
      {
        "label": "Overhaul",
        "children": [
          {
            "label": "Technological University (Taunggyi)"
          },
          {
            "label": "Universidad de Las Palmas de Gran Canaria"
          },
          {
            "label": "Olympia College"
          },
          {
            "label": "Franklin and Marshall College"
          },
          {
            "label":
              "State University of New York College of Environmental Science and Forestry"
          }
        ]
      },
      {
        "label": "GTK",
        "children": [
          {
            "label": "Salisbury State University"
          },
          {
            "label":
              "Evangelische Fachhochschule für Religionspädagogik, und Gemeindediakonie Moritzburg"
          },
          {
            "label": "Kilimanjaro Christian Medical College"
          }
        ]
      },
      {
        "label": "SRP",
        "children": [
          {
            "label": "Toyo Gakuen University"
          },
          {
            "label": "Riyadh College of Dentistry and Pharmacy"
          },
          {
            "label": "Aichi Gakusen University"
          }
        ]
      }
    ]
  },
  {
    "label": "Assistant Manager",
    "children": [
      {
        "label": "Risk Analysis",
        "children": [
          {
            "label": "Seijo University"
          },
          {
            "label": "University of Economics Varna"
          },
          {
            "label": "College of Technology at Riyadh"
          }
        ]
      },
      {
        "label": "UV Mapping",
        "children": [
          {
            "label": "Universidad de La Sabana"
          },
          {
            "label": "Pamukkale University"
          }
        ]
      }
    ]
  },
  {
    "label": "Quality Engineer",
    "children": [
      {
        "label": "Enzyme Kinetics",
        "children": [
          {
            "label": "Universidad del Valle de Guatemala"
          },
          {
            "label":
              "Ecole Nationale Supérieure d'Electronique, d'Electrotechnique, d'Informatique et d'Hydraulique de Toulouse"
          },
          {
            "label": "Kota Bharu Polytechnic"
          },
          {
            "label": "College of Technology at Kharj"
          }
        ]
      },
      {
        "label": "Gastroenterology",
        "children": [
          {
            "label":
              "Balochistan University of Engineering and Technology Khuzdar"
          },
          {
            "label": "Université de Cergy-Pontoise"
          },
          {
            "label": "Frederick University"
          }
        ]
      },
      {
        "label": "ADP Payroll",
        "children": [
          {
            "label": "National University"
          },
          {
            "label": "Ecole de l'Air"
          },
          {
            "label": "Vietnam National University of Agriculture"
          },
          {
            "label":
              "St. Petersburg State University of Aerospace Instrumentation"
          }
        ]
      }
    ]
  },
  {
    "label": "Senior Sales Associate",
    "children": [
      {
        "label": "RSVP",
        "children": [
          {
            "label": "Islamic Azad University, Ahar"
          },
          {
            "label": "Okinawa International University"
          },
          {
            "label": "Karlshochschule International University"
          }
        ]
      },
      {
        "label": "IxChariot",
        "children": [
          {
            "label": "Cambodia University of Specialties"
          },
          {
            "label":
              "Ecole Supérieure des Techniques Industrielles et des Textiles"
          }
        ]
      }
    ]
  },
  {
    "label": "Automation Specialist I",
    "children": [
      {
        "label": "Ffmpeg",
        "children": [
          {
            "label": "Christian Heritage College"
          },
          {
            "label": "Inha University"
          },
          {
            "label": "Khalifa University"
          }
        ]
      },
      {
        "label": "Mac OS",
        "children": [
          {
            "label": "Prague College"
          },
          {
            "label": "Wakayama Medical College"
          },
          {
            "label": "South University of Science and Technology of China "
          },
          {
            "label": "Campbell University"
          }
        ]
      },
      {
        "label": "Visual Communication",
        "children": [
          {
            "label": "University of the Cordilleras"
          },
          {
            "label": "University of Mohaghegh"
          }
        ]
      },
      {
        "label": "PCRF",
        "children": [
          {
            "label": "FPT University"
          },
          {
            "label": "Rakuno Gakuen University"
          },
          {
            "label": "Xiangtan Normal University"
          },
          {
            "label": "Rice University"
          },
          {
            "label": "Sapporo Gakuin University"
          }
        ]
      }
    ]
  },
  {
    "label": "Technical Writer",
    "children": [
      {
        "label": "NC-Verilog",
        "children": [
          {
            "label": "Etisalat University College"
          },
          {
            "label": "Newcastle University, Medicine Malaysia "
          },
          {
            "label": "University of Asia Pacific, Dhanmondi"
          },
          {
            "label": "Leading University"
          }
        ]
      },
      {
        "label": "Water Treatment",
        "children": [
          {
            "label":
              "Gorgan University of Agricultural Sciences and Natural Resources"
          },
          {
            "label": "Tianjin Polytechnic University"
          },
          {
            "label": "Universitas Bojonegoro"
          }
        ]
      },
      {
        "label": "FTO",
        "children": [
          {
            "label": "Université de Skikda"
          },
          {
            "label": "University College of Technology & Innovation (UCTI)"
          },
          {
            "label": "Ahmedabad University"
          },
          {
            "label": "Universidad Intercontinental"
          },
          {
            "label": "Atlantic Union College"
          }
        ]
      },
      {
        "label": "Vocational Rehabilitation",
        "children": [
          {
            "label": "Cambodia University of Specialties"
          },
          {
            "label": "Universiteit Antwerpen Management School"
          }
        ]
      },
      {
        "label": "DH+",
        "children": [
          {
            "label": "Universidad de Córdoba"
          },
          {
            "label": "Université Lumière de Bujumbura"
          },
          {
            "label": "Madonna University"
          },
          {
            "label": "University of Washington"
          }
        ]
      }
    ]
  },
  {
    "label": "Software Test Engineer IV",
    "children": [
      {
        "label": "Zero Waste",
        "children": [
          {
            "label": "University of Italian Studies for Foreigners of Siena"
          },
          {
            "label": "Klaipeda University"
          },
          {
            "label": "Tallinn University"
          }
        ]
      },
      {
        "label": "Fixed Assets",
        "children": [
          {
            "label": "North Carolina Central University"
          },
          {
            "label": "Universidad Nacional de San Luis"
          },
          {
            "label": "Baha'i Institute for Higher Education"
          }
        ]
      }
    ]
  },
  {
    "label": "Nuclear Power Engineer",
    "children": [
      {
        "label": "Woodworking",
        "children": [
          {
            "label": "National Chiayi University"
          },
          {
            "label": "Tokyo Kasei University"
          },
          {
            "label": "Auchi Polytechnic"
          },
          {
            "label": "Hashemite University"
          },
          {
            "label": "Thomas Jefferson University"
          }
        ]
      },
      {
        "label": "Psychotherapy",
        "children": [
          {
            "label": "Trident University"
          },
          {
            "label": "Université de N'Djamena"
          },
          {
            "label": "Parsons School of Design"
          },
          {
            "label": "University of San Diego"
          }
        ]
      },
      {
        "label": "Credit Unions",
        "children": [
          {
            "label": "Tilburg University"
          },
          {
            "label": "Miyazaki University"
          },
          {
            "label": "Ohio State University - Newark"
          }
        ]
      }
    ]
  },
  {
    "label": "Media Manager III",
    "children": [
      {
        "label": "BPL",
        "children": [
          {
            "label": "International Burch University"
          },
          {
            "label": "Trinity International University"
          },
          {
            "label": "Universidad Autónoma de Centro América"
          },
          {
            "label": "Evangelische Fachhochschule Nürnberg"
          },
          {
            "label": "Academy of Music, Dance and Fine Arts"
          }
        ]
      },
      {
        "label": "NVU",
        "children": [
          {
            "label": "University Institute of Modern Languages"
          },
          {
            "label": "Kyungil University"
          },
          {
            "label": "Jimma University"
          }
        ]
      },
      {
        "label": "Zooarchaeology",
        "children": [
          {
            "label": "Hebei Medical University"
          },
          {
            "label": "Bharath Institue Of Higher Education & Research"
          },
          {
            "label": "Universität Hannover"
          }
        ]
      }
    ]
  },
  {
    "label": "Safety Technician IV",
    "children": [
      {
        "label": "IOT",
        "children": [
          {
            "label": "Belarussian National Technical University"
          },
          {
            "label": "Tokyo University of Pharmacy and Life Science"
          },
          {
            "label": "Brickfields Asia College"
          },
          {
            "label": "Samar State University"
          },
          {
            "label": "West Bengal University of Technology"
          }
        ]
      },
      {
        "label": "Lymphatic Drainage",
        "children": [
          {
            "label": "Free University Amsterdam"
          },
          {
            "label": "Friedrich-Alexander Universität Erlangen-Nürnberg"
          },
          {
            "label": "Sinnar University"
          },
          {
            "label": "Okayama University of Science"
          }
        ]
      },
      {
        "label": "OLAP Cube Studio",
        "children": [
          {
            "label": "Liaoning Technical University"
          },
          {
            "label": "Instituto Superior D. Afonso III - INUAF"
          },
          {
            "label": "Kossuth Lajos University"
          }
        ]
      },
      {
        "label": "DSM-IV",
        "children": [
          {
            "label": "Daniel Webster College"
          },
          {
            "label": "University of Athens"
          }
        ]
      }
    ]
  },
  {
    "label": "Nuclear Power Engineer",
    "children": [
      {
        "label": "Guest Lecturing",
        "children": [
          {
            "label": "National Pingtung Teachers College"
          },
          {
            "label": "Advance Tertiary College"
          },
          {
            "label":
              "Louisiana State University Health Sciences Center New Orleans"
          },
          {
            "label": "University of Shiga Prefecture"
          }
        ]
      },
      {
        "label": "Ayurveda",
        "children": [
          {
            "label": "Paichai University"
          },
          {
            "label": "Universidad Sergio Arboleda"
          },
          {
            "label": "Lansbridge University"
          }
        ]
      },
      {
        "label": "Aeronautics",
        "children": [
          {
            "label":
              "Ecole Nationale Supérieure d'Ingénieurs en Mécanique et Energétique de Valenciennes"
          },
          {
            "label": "Ajou University"
          },
          {
            "label": "Islamic Azad University, Tehran Science & Research Branch"
          },
          {
            "label": "University of Michigan - Flint"
          },
          {
            "label": "University of Ferrara"
          }
        ]
      }
    ]
  },
  {
    "label": "Civil Engineer",
    "children": [
      {
        "label": "Architectural Illustration",
        "children": [
          {
            "label": "Detroit College of Law"
          },
          {
            "label": "European Carolus Magnus University"
          }
        ]
      },
      {
        "label": "Teaching Writing",
        "children": [
          {
            "label": "Virginia Intermont College"
          },
          {
            "label": "Polytechnic of Namibia"
          },
          {
            "label": "Kigali Independent University"
          },
          {
            "label": "Nepal Sanskrit University"
          }
        ]
      },
      {
        "label": "MS Excel Pivot Tables",
        "children": [
          {
            "label": "Newcastle University, Medicine Malaysia "
          },
          {
            "label": "National Fisheries University"
          },
          {
            "label": "Université d'Antsiranana"
          },
          {
            "label": "Shenyang Polytechnic University"
          }
        ]
      }
    ]
  },
  {
    "label": "Senior Editor",
    "children": [
      {
        "label": "Semantic HTML",
        "children": [
          {
            "label": "Southwest University of Finance and Economics"
          },
          {
            "label": "Civil Aviation University of China"
          },
          {
            "label": "Belarussian State Technological University"
          }
        ]
      },
      {
        "label": "ASP",
        "children": [
          {
            "label": "Kyoto Tachibana Women's University"
          },
          {
            "label": "Ursuline College"
          },
          {
            "label": "York University"
          },
          {
            "label": "Jewish University in Moscow"
          }
        ]
      },
      {
        "label": "OCLC Connexion",
        "children": [
          {
            "label": "New York University"
          },
          {
            "label": "Pittsburg State University"
          }
        ]
      },
      {
        "label": "Rural Marketing",
        "children": [
          {
            "label": "Universidad de Cartagena"
          },
          {
            "label": "Czech University of Agriculture Prague"
          },
          {
            "label": "Tohoku Women's College"
          },
          {
            "label": "Gunma University"
          },
          {
            "label": "Minsk State Linguistic University"
          }
        ]
      },
      {
        "label": "DDI",
        "children": [
          {
            "label": "Voronezh State Technical University"
          },
          {
            "label": "University Center \"César Ritz\""
          }
        ]
      }
    ]
  },
  {
    "label": "Media Manager IV",
    "children": [
      {
        "label": "Yamaha PM5D",
        "children": [
          {
            "label": "Mooreland University"
          },
          {
            "label": "Universidad de San Pablo CEU"
          },
          {
            "label": "Universidad Galileo"
          },
          {
            "label": "College of Technology at Abha"
          },
          {
            "label": "Cabrini College"
          }
        ]
      },
      {
        "label": "HSE Management Systems",
        "children": [
          {
            "label": "Grinnell College"
          },
          {
            "label": "Chinju National University of Education"
          },
          {
            "label": "Dokkyo University School of Medicine"
          },
          {
            "label": "University of New England, Westbrook College Campus"
          },
          {
            "label": "Miami University of Ohio - Hamilton"
          }
        ]
      }
    ]
  },
  {
    "label": "Product Engineer",
    "children": [
      {
        "label": "Multi-Unit",
        "children": [
          {
            "label": "Strayer University"
          },
          {
            "label": "National Kaohsiung University of Applied Sciences"
          },
          {
            "label": "Philadelphia University"
          },
          {
            "label": "National Institute of Mental Health and Neuro Sciences"
          },
          {
            "label": "Vardhaman Mahaveer Open University"
          }
        ]
      },
      {
        "label": "FX Trading",
        "children": [
          {
            "label": "Universidade Estácio de Sá"
          },
          {
            "label": "Manipal University"
          }
        ]
      }
    ]
  },
  {
    "label": "Account Coordinator",
    "children": [
      {
        "label": "Biostatistics",
        "children": [
          {
            "label": "Al-Bukhari International University"
          },
          {
            "label": "Technical University of Denmark"
          },
          {
            "label": "Postgraduate lnstitute of Medical Education and Research"
          }
        ]
      },
      {
        "label": "FM",
        "children": [
          {
            "label": "University of Oxford"
          },
          {
            "label": "Lawrence University"
          },
          {
            "label": "Okayama University"
          }
        ]
      },
      {
        "label": "Microsoft Certified Professional",
        "children": [
          {
            "label": "Universidade Católica de Brasília"
          },
          {
            "label": "Georgia Institute of Technology"
          },
          {
            "label": "University of Petrosani"
          }
        ]
      }
    ]
  },
  {
    "label": "Payment Adjustment Coordinator",
    "children": [
      {
        "label": "Federal Grants Management",
        "children": [
          {
            "label": "Christ University"
          },
          {
            "label": "Janos Selye University"
          },
          {
            "label": "Zagazig University"
          },
          {
            "label": "Constantin Brancoveanu University Pitesti"
          },
          {
            "label": "Southwest University of Political Science and Law"
          }
        ]
      },
      {
        "label": "Company Set-up",
        "children": [
          {
            "label": "Ball State University"
          },
          {
            "label": "Mustafa Kemal University"
          },
          {
            "label": "Transylvania University"
          }
        ]
      },
      {
        "label": "CDMA",
        "children": [
          {
            "label": "College of Telecommunication & Information "
          },
          {
            "label": "Nagasaki Prefectural University"
          },
          {
            "label": "Gustav-Siewerth-Akademie"
          }
        ]
      },
      {
        "label": "Overhead Cranes",
        "children": [
          {
            "label": "Universidad de Pamplona"
          },
          {
            "label": "Bindura University of Science Education"
          },
          {
            "label": "Daiichi University of Economics"
          },
          {
            "label": "Wirtschaftsuniversität Wien"
          }
        ]
      },
      {
        "label": "CDO",
        "children": [
          {
            "label": "Design Institute of San Diego"
          },
          {
            "label": "Wellspring University"
          },
          {
            "label": "Franciscan School of Theology"
          }
        ]
      }
    ]
  },
  {
    "label": "Assistant Manager",
    "children": [
      {
        "label": "SQL Server Management Studio",
        "children": [
          {
            "label": "University of Sudbury"
          },
          {
            "label":
              "Evangelische Fachhochschule Berlin, Fachhochschule für Sozialarbeit und Sozialpädagogik"
          },
          {
            "label": "Vitebsk State University"
          },
          {
            "label": "San Jose Christian College"
          },
          {
            "label": "Ivanovo State University"
          }
        ]
      },
      {
        "label": "Abstracting",
        "children": [
          {
            "label": "Adeyemi College of Education"
          },
          {
            "label": "Université de Sherbrooke"
          },
          {
            "label": "University College of Applied Sciences"
          },
          {
            "label": "Johns Hopkins University, SAIS Bologna Center"
          }
        ]
      },
      {
        "label": "WTL",
        "children": [
          {
            "label": "Universidad de Córdoba"
          },
          {
            "label": "Institut National Polytechnique de Grenoble"
          },
          {
            "label": "Kyonggi University"
          }
        ]
      }
    ]
  },
  {
    "label": "Professor",
    "children": [
      {
        "label": "People Skills",
        "children": [
          {
            "label": "University of Calcutta"
          },
          {
            "label": "Universidad del Valle del Cauca"
          },
          {
            "label":
              "FAST - National University of Computer and Emerging Sciences (NUCES)"
          }
        ]
      },
      {
        "label": "Workforce Development",
        "children": [
          {
            "label": "Shandong Medical University"
          },
          {
            "label": "Al Khawarizmi International College"
          },
          {
            "label": "Nippon Dental University"
          },
          {
            "label": "Komsomolsk-on-Amur State Technical University"
          },
          {
            "label": "Lingnan University"
          }
        ]
      },
      {
        "label": "Digital Journalism",
        "children": [
          {
            "label": "The College of St. Scholastica"
          },
          {
            "label": "Universidad Autónoma de la Ciudad de México"
          },
          {
            "label":
              "University of Information Technology and Management in Rzeszow"
          },
          {
            "label": "Liaquat University of Medical & Health Sciences Jamshoro"
          }
        ]
      },
      {
        "label": "Short Films",
        "children": [
          {
            "label": "Universidad Católica de Valencia"
          },
          {
            "label": "Columbia International University"
          },
          {
            "label": "Framingham State College"
          },
          {
            "label": "Gurukul University"
          },
          {
            "label": "NTI University"
          }
        ]
      },
      {
        "label": "XML Programming",
        "children": [
          {
            "label": "Victoria University"
          },
          {
            "label": "Andrews University"
          },
          {
            "label": "Centre Universitaire d'Oum El Bouaghi"
          },
          {
            "label": "Dilla University"
          }
        ]
      }
    ]
  }
]

app.layout = html.Div([
    dash_dropdown_tree_select.DashDropdownTreeSelect(
        data=data,
    )
])



if __name__ == '__main__':
    app.run_server(debug=False)
