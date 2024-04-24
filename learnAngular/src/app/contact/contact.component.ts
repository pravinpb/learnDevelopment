import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';

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
     mobile: new FormControl('', [Validators.required, Validators.minLength(10), Validators.maxLength(10),Validators.pattern('^[0-9]*$'),]),
     grade: new FormControl('', Validators.required),
     gender: new FormControl('', Validators.required)
  });
  private studentDetails: any = [];
  genders = ['Male', 'Female', 'Other'];
  constructor(private http: HttpClient, private router: Router) { }

  onSubmit() {
    if (this.userForm.valid) {
       const httpOptions = {
         headers: new HttpHeaders({
           'Content-Type': 'application/json'
         }),
         responseType: 'text' as 'json'
       };
   
       this.http.post('http://localhost:5000/student', this.userForm.value, httpOptions).subscribe(
         response => {
           console.log('Success:', response);
           alert('Student added successfully');
           this.userForm.reset();
           this.router.navigate(['/about']);
         },
         error => {
           console.error('Error:', error);
           console.log('Failed to add student');
         }
       );
    }
    else {
       alert('Please fill all the details');
    }
   }
}


