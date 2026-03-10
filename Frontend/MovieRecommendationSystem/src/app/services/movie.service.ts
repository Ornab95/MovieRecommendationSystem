import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, provideHttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';


export interface MovieRecommendationResponse {
    movie: string;
    recommendations: string[];
    error?: string;
}

@Injectable({
    providedIn: 'root'
})
export class MovieService {
    private apiUrl = 'http://localhost:8000';

    constructor(private http: HttpClient) { }

    getRecommendations(movieName: string): Observable<MovieRecommendationResponse> {
        return this.http.get<MovieRecommendationResponse>(`${this.apiUrl}/recommend?movie_name=${encodeURIComponent(movieName)}`)
            .pipe(
                catchError((error: HttpErrorResponse) => {
                    let errorMsg = 'An unknown error occurred';
                    if (error.error instanceof ErrorEvent) {
                        // Client-side error
                        errorMsg = `Error: ${error.error.message}`;
                    } else {
                        // Server-side error
                        if (error.status === 404) {
                            errorMsg = 'Movie not found. Try another title.';
                        } else if (error.error && error.error.error) {
                            errorMsg = error.error.error;
                        } else {
                            errorMsg = `Error Code: ${error.status}\nMessage: ${error.message}`;
                        }
                    }
                    return throwError(() => new Error(errorMsg));
                })
            );
    }
}
