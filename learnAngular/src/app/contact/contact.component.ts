import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrl: './contact.component.scss'
})
export class ContactComponent {
  userForm = new FormGroup({
     firstname: new FormControl('', Validators.required),
     lastname: new FormControl('', Validators.required),
     email: new FormControl('', [Validators.required, Validators.email]),
     mobile: new FormControl('', [Validators.required, Validators.minLength(10), Validators.maxLength(15)]),
     grade: new FormControl('', Validators.required),
     gender: new FormControl('', Validators.required)
  });
  private studentDetails: any = [];

  constructor(private http: HttpClient) { }

  onSubmit() {
    if (this.userForm.valid) {
        this.http.post('http://localhost/5000', this.userForm.value).subscribe(
            response => {
                console.log('Success:', response);
                // Handle success response
            },
            error => {
                console.error('Error:', error);
                // Handle error response
            }
        );
    } else {
        console.log('Form is invalid');
    }
}
}
