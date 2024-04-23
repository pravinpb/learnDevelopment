import { Component } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrl: './contact.component.scss'
})
export class ContactComponent {
  userForm = new FormGroup({
    firstname: new FormControl(''),
    lastname: new FormControl(''),
    email: new FormControl(''),
    mobile: new FormControl(''),
    grade: new FormControl(''),
    gender: new FormControl('')
  });
  // ...

  constructor(private http: HttpClient) {}

  onSubmit() {
    debugger;
    const obj = this.userForm.value;
    // this.http.post('http://localhost:4200/', obj).subscribe((result:any) => {
    //   alert('User is created successfully');
    // });
  }
}
