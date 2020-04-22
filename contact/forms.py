from django import forms


class ContactForm(forms.Form):
    nama = forms.CharField(
        max_length=20,
        label="Nama",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nama anda',
            }
        )
    )

    JENIS_KELAMIN = (
        ('P', 'Pria'),
        ('W', 'Wanita')
    )
    gender = forms.ChoiceField(
        widget=forms.RadioSelect(
            attrs={
                'class': 'form-check-input',
            }
        ),
        choices=JENIS_KELAMIN
    )

    email = forms.EmailField(
        label="Alamat Email",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan email anda'
            }
        )
    )

    alamat = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        )
    )

    # agree = forms.BooleanField(
    #    required=False,
    #    widget=forms.CheckboxInput(
    #        attrs={
    #            'class': 'form-check-input',
    #        }
    #    )
    # )

    #TAHUN = range(1945, 2021, 1)
    # tanggal_lahir = forms.DateField(
    #    widget=forms.SelectDateWidget(
    #        attrs={
    #            'class': 'form-control col-sm-2'
    #        },
    #        years=TAHUN,
    #    )
    # )

    def clean_nama(self):
        nama_input = self.cleaned_data.get('nama')

        if nama_input == "memek":
            raise forms.ValidationError("nama tidak boleh memek")

        return nama_input
